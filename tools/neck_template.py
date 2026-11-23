"""Stamp the STANDARD neckline cut (model 5 small girl) onto an image.

The cut is defined once, normalised to the neck width W (u = dx/W from the centre, v = dy/W below the flat level):
flat high edge as wide as the neck, two soft arcs, one small notch 0.137*W deep.
Usage: python3 -I neck_template.py SRC OUTPREFIX CX Y0 W BOTTOM "fx,fy" "sx,sy" ["lx,ly;lx2,ly2" "rx,ry;rx2,ry2"]
  CX,Y0  centre x and y of the flat part of the edge;  W neck width at its base (full-res pixels)
  BOTTOM y below the old neckline (everything skin-coloured between the new edge and BOTTOM becomes fabric)
  fx,fy / sx,sy  sample points of plain fabric / bare skin
  optional left/right continuation points of the edge beyond the neck corners (going outwards and up)
Writes OUTPREFIX-pre.jpg (pre-painted source), OUTPREFIX-mask.png (white = regenerate), OUTPREFIX-pv.jpg (preview).
"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

HALF = [(0.0, 0.137), (0.035, 0.105), (0.09, 0.055), (0.15, 0.025), (0.22, 0.010), (0.33, 0.0), (0.42, -0.02), (0.5, -0.06)]


def pts(s):
    return [tuple(float(v) for v in p.split(',')) for p in s.split(';') if p]


src, out = sys.argv[1], sys.argv[2]
cx, y0, W, bottom = (float(a) for a in sys.argv[3:7])
(fx, fy), (sx, sy) = pts(sys.argv[7])[0], pts(sys.argv[8])[0]
left = pts(sys.argv[9]) if len(sys.argv) > 9 else []
right = pts(sys.argv[10]) if len(sys.argv) > 10 else []

# dense smooth edge through the template points
u = np.array([-p[0] for p in HALF[::-1]] + [p[0] for p in HALF[1:]])
v = np.array([p[1] for p in HALF[::-1]] + [p[1] for p in HALF[1:]])
uu = np.linspace(-0.5, 0.5, 201)
vv = np.interp(uu, u, v)
k = np.ones(7) / 7  # light smoothing, keep the tiny point of the notch
sm = np.convolve(np.pad(vv, 3, mode='edge'), k, mode='valid')
mid = np.abs(uu) < 0.03
vv = np.where(mid, vv, sm)
edge = [(cx + a * W, y0 + b * W) for a, b in zip(uu, vv)]
edge = left[::-1] + edge + right

im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(np.float32)
H, Wd = a.shape[:2]


def med(x, y, r=25):
    return np.median(a[int(y) - r:int(y) + r, int(x) - r:int(x) + r].reshape(-1, 3), axis=0)


fab, skin = med(fx, fy), med(sx, sy)
poly = edge + [(edge[-1][0], bottom), (edge[0][0], bottom)]
pm = Image.new('L', im.size, 0)
ImageDraw.Draw(pm).polygon(poly, fill=255)
inside = np.asarray(pm) > 0
skinlike = np.linalg.norm(a - skin, axis=2) < np.linalg.norm(a - fab, axis=2)
fill = inside & skinlike
fill = np.asarray(Image.fromarray((fill * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(9))) > 0
fill &= inside
b = a.copy()
# fill with real fabric texture cloned from straight below (shift D px), colour-matched to the fabric sample
D = int(bottom - y0 + W * 0.15)
# whole region under the new edge (down to BOTTOM) is replaced by the cloned fabric; feathered at the bottom
alpha = np.asarray(pm.filter(ImageFilter.GaussianBlur(30))).astype(np.float32) / 255.0
alpha[: int(y0 - W * 0.3)] = 0
top_hard = np.asarray(pm) > 0  # keep the new edge itself sharp
yy = np.arange(H)[:, None]
alpha = np.where(top_hard & (yy < bottom - 40), 1.0, alpha)
sh = np.vstack([a[D:], np.repeat(a[-1:], D, axis=0)])
# low-frequency colour correction: make the cloned fabric match the original fabric's local colour/shading
isfab = (~skinlike).astype(np.float32)
bg = (a.min(axis=2) > 232)
isfab[bg] = 0
diff = (a - sh) * isfab[..., None]
r = int(W * 0.08)
def blur(x):
    # separable box blur x3 (~gaussian) on a downsampled grid, then upsampled
    k = 8
    h2, w2 = H // k, Wd // k
    sm = x[:h2 * k, :w2 * k].reshape(h2, k, w2, k).mean(axis=(1, 3))
    rr = max(1, r // k)
    for _ in range(3):
        c = np.cumsum(np.pad(sm, ((rr + 1, rr), (0, 0)), mode='edge'), axis=0)
        sm = (c[2 * rr + 1:] - c[:-2 * rr - 1]) / (2 * rr + 1)
        c = np.cumsum(np.pad(sm, ((0, 0), (rr + 1, rr)), mode='edge'), axis=1)
        sm = (c[:, 2 * rr + 1:] - c[:, :-2 * rr - 1]) / (2 * rr + 1)
    up = np.asarray(Image.fromarray(sm.astype(np.float32), mode='F').resize((Wd, H), Image.BILINEAR))
    return up
den = blur(isfab) + 1e-3
corr = np.stack([blur(diff[..., c]) / den for c in range(3)], axis=2)
far = den < 0.05
corr[far] = 0
sh = sh + corr
alpha[bg] = 0
b = a * (1 - alpha[..., None]) + sh * alpha[..., None]
fill = alpha > 0.02
pre = Image.fromarray(np.clip(b, 0, 255).astype(np.uint8))
pre.save(out + '-pre.jpg', quality=96, subsampling=0)

# mask: the filled area, grown, plus a band along the new edge (a little skin above it)
g = max(15, int(W * 0.022)) | 1
m = Image.fromarray((inside * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(2 * (g // 2) + 1)).filter(ImageFilter.GaussianBlur(g / 3)).point(lambda t: 255 if t > 40 else 0)
band = Image.new('L', im.size, 0)
ImageDraw.Draw(band).line(edge, fill=255, width=int(W * 0.05))
for ex, ey in (edge[0], edge[-1]):
    rr = W * 0.08
    ImageDraw.Draw(band).ellipse((ex - rr, ey - rr, ex + rr, ey + rr), fill=255)
if '--band-only' in sys.argv:
    m = band
else:
    m = Image.fromarray(np.maximum(np.asarray(m), np.asarray(band)))
m.convert('RGB').save(out + '-mask.png')

pv = pre.copy()
ImageDraw.Draw(pv).line(edge, fill=(255, 0, 0), width=6)
mk = np.asarray(m) > 0
ov = np.asarray(pv).astype(np.float32)
ov[mk] = ov[mk] * 0.75 + np.array([0, 90, 255]) * 0.25
x0, x1 = int(max(0, cx - W * 1.3)), int(min(Wd, cx + W * 1.3))
yA, yB = int(max(0, y0 - W * 0.6)), int(min(H, bottom + W * 0.3))
Image.fromarray(ov.astype(np.uint8)).crop((x0, yA, x1, yB)).resize((1300, int(1300 * (yB - yA) / (x1 - x0)))).save(out + '-pv.jpg', quality=88)
print('filled px', int(fill.sum()), 'mask px', int(mk.sum()), 'size', im.size)
