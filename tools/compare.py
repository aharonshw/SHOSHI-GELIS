import sys
from PIL import Image, ImageDraw, ImageFont
# usage: compare.py out.jpg "label|path" ...
out=sys.argv[1]; items=[a.split('|',1) for a in sys.argv[2:]]
H=1100; pad=20; top=90
ims=[]
for lab,p in items:
    im=Image.open(p).convert('RGB'); im=im.resize((int(im.width*H/im.height),H)); ims.append((lab,im))
W=sum(i.width for _,i in ims)+pad*(len(ims)+1)
c=Image.new('RGB',(W,H+top+pad),'white'); d=ImageDraw.Draw(c)
try: f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',52)
except: f=ImageFont.load_default()
x=pad
for lab,im in ims:
    c.paste(im,(x,top)); t=lab
    tw=d.textlength(t,font=f); d.text((x+(im.width-tw)/2,18),t,fill=(30,30,30),font=f); x+=im.width+pad
c.save(out,quality=88); print(out,c.size)
