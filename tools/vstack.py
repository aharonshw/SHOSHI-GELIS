import sys
from PIL import Image, ImageDraw, ImageFont
out=sys.argv[1]; items=[a.split('|',1) for a in sys.argv[2:]]
W=2000; f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',48)
rows=[]
for lab,p in items:
    im=Image.open(p).convert('RGB'); im=im.resize((W,int(im.height*W/im.width))); rows.append((lab,im))
H=sum(i.height+80 for _,i in rows)
c=Image.new('RGB',(W,H),'white'); d=ImageDraw.Draw(c); y=0
for lab,im in rows:
    tw=d.textlength(lab,font=f); d.text(((W-tw)/2,y+12),lab,fill=(30,30,30),font=f); c.paste(im,(0,y+80)); y+=im.height+80
c.save(out,quality=86); print(out,c.size)
