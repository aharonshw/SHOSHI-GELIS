"""Builds deliverables/shoshi-gelis-approval.html: a self-contained review page for the client.

Usage: python3 -I tools/build_review.py tools/review_template.html
Images come from catalog-refs/ (models made with the closeup-first method) and
catalog-refs/earlier/ (models approved in earlier rounds: 2, 3, 4, 8, 11, 14).
"""
import base64, io, json, os, sys
from PIL import Image

R = '/home/user/SHOSHI-GELIS/catalog-refs/'
E = R + 'earlier/'
OUT = '/home/user/SHOSHI-GELIS/deliverables/shoshi-gelis-approval.html'
D1, D2, BIG, SMALL = 'נערה ראשונה', 'נערה שנייה', 'ילדה גדולה', 'ילדה קטנה'
CU, FB, SIDE, BACK = 'תקריב', 'גוף מלא', 'צילום מהצד', 'צילום מהגב'


def new(sid, who, extra=''):
    """Shot made with the closeup-first method: <sid>-closeup / -full / -side-full in catalog-refs."""
    imgs = [(R + sid + '-closeup.jpg', CU), (R + sid + '-full.jpg', FB)]
    if os.path.exists(R + sid + '-side-full.jpg'):
        imgs.append((R + sid + '-side-full.jpg', SIDE))
    return (sid, who, extra, imgs)


def old(sid, who, extra, *parts):
    """Earlier-round shot: parts are (file suffix, label) under catalog-refs/earlier/<sid>-<suffix>.jpg."""
    return (sid, who, extra, [(E + sid + '-' + suf + '.jpg', label) for suf, label in parts])


MODELS = [
    ('דגם 1', 'אפרסק', [new('m01-d1-v3', D1, 'תחרת פרחים'), new('m01-big-flowers', BIG, 'עם פרחים'),
                        new('m01-big-plain', BIG, 'חלק, חגורת אבנים'), new('m01-small', SMALL)]),
    ('דגם 2', 'מוקה פרפרים / טורקיז', [
        old('m02-d1-mocha', D1, 'מוקה', ('closeup', CU), ('full', FB)),
        old('m02-d2-turquoise', D2, 'טורקיז', ('closeup-crop', CU), ('full', FB)),
        old('m02-big-mocha', BIG, 'מוקה', ('closeup-crop', CU), ('full', FB), ('back', BACK)),
        old('m02-small-mocha', SMALL, 'מוקה', ('closeup', CU), ('full', FB))]),
    ('דגם 3', 'שמנת עם רקמת פרחים', [
        old('m03-d1', D1, '', ('closeup-crop', CU), ('full', FB)),
        old('m03-d2', D2, '', ('closeup-crop', CU), ('full', FB), ('back', BACK)),
        old('m03-big', BIG, '', ('closeup-crop', CU), ('full', FB)),
        old('m03-small', SMALL, '', ('closeup-crop', CU), ('full', FB))]),
    ('דגם 4', 'שחור עם תחרה', [
        old('m04-big', BIG, '', ('closeup-crop', CU), ('full', FB)),
        old('m04-small', SMALL, '', ('closeup-crop', CU), ('full', FB))]),
    ('דגם 5', 'ירוק כהה', [new('m05-big', BIG), new('m05-small', SMALL)]),
    ('דגם 6', 'מנטה', [new('m06-d1', D1), new('m06-d2', D2), new('m06-big', BIG), new('m06-small', SMALL)]),
    ('דגם 7', 'תכלת־מנטה', [new('m07-d1', D1), new('m07-d2', D2), new('m07-big', BIG), new('m07-small', SMALL)]),
    ('דגם 8', 'שמנת עם תחרת פרחים', [
        old('m08-d1', D1, '', ('full-lowres', FB)),
        old('m08-d2', D2, '', ('full-lowres', FB)),
        old('m08-big', BIG, '', ('full-lowres', FB)),
        old('m08-small', SMALL, '', ('closeup', CU), ('full', FB))]),
    ('דגם 9', 'כחול־אפרפר', [new('m09-d1', D1), new('m09-d2', D2), new('m09-big', BIG), new('m09-small', SMALL)]),
    ('דגם 10', 'שמנת עם גלים', [new('m10-d1', D1), new('m10-d2', D2)]),
    ('דגם 11', 'שמפניה נצנץ', [
        old('m11-d1', D1, '', ('closeup-crop', CU), ('full', FB)),
        old('m11-d2', D2, '', ('closeup', CU), ('full', FB)),
        old('m11-big', BIG, '', ('closeup-crop', CU), ('full', FB)),
        old('m11-small', SMALL, '', ('closeup-crop', CU), ('full', FB))]),
    ('דגם 12', 'ורוד', [new('m12-d1', D1, 'פסי קטיפה שחורים'), new('m12-d2', D2, 'קומות טול'),
                        new('m12-big', BIG), new('m12-small', SMALL)]),
    ('דגם 13', 'שחור ובז׳', [new('m13-d1', D1), new('m13-d2', D2), new('m13-big', BIG), new('m13-small', SMALL)]),
    ('דגם 14', 'ברוקד כסף־תכלת', [
        old('m14-d1', D1, '', ('closeup-crop', CU), ('full', FB)),
        old('m14-d2', D2, '', ('closeup-crop', CU), ('full', FB))]),
]


def enc(path, label):
    h, q = (1100, 80) if label == CU else (1500, 82)
    im = Image.open(path).convert('RGB')
    im.thumbnail((10000, h), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, optimize=True, progressive=True)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode(), im.size


data, n = [], 0
for title, color, shots in MODELS:
    m = {'title': title, 'color': color, 'shots': []}
    for sid, who, extra, imgs in shots:
        out = []
        for path, label in imgs:
            src, (w, h) = enc(path, label)
            out.append({'id': os.path.basename(path)[:-4], 'label': label, 'src': src, 'w': w, 'h': h})
            n += 1
        m['shots'].append({'who': who, 'extra': extra, 'imgs': out})
    data.append(m)

ids = [i['id'] for m in data for s in m['shots'] for i in s['imgs']]
assert len(ids) == len(set(ids)), 'duplicate image ids'
tpl = open(sys.argv[1], encoding='utf8').read()
html = tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False)).replace('__TOTAL__', str(n))
open(OUT, 'w', encoding='utf8').write(html)
print(n, 'images,', sum(len(m['shots']) for m in data), 'shots,', round(len(html.encode()) / 1e6, 2), 'MB')
