import base64, io, json, sys
from PIL import Image
R='/home/user/SHOSHI-GELIS/catalog-refs/'
OUT='/home/user/SHOSHI-GELIS/deliverables/shoshi-gelis-approval.html'
MODELS=[
 ('דגם 1','אפרסק',[('m01-d1-v3','נערה ראשונה','תחרת פרחים'),('m01-big-flowers','ילדה גדולה','עם פרחים'),('m01-big-plain','ילדה גדולה','חלק, חגורת אבנים'),('m01-small','ילדה קטנה','')]),
 ('דגם 5','ירוק כהה',[('m05-big','ילדה גדולה',''),('m05-small','ילדה קטנה','')]),
 ('דגם 6','מנטה',[('m06-d1','נערה ראשונה',''),('m06-d2','נערה שנייה',''),('m06-big','ילדה גדולה',''),('m06-small','ילדה קטנה','')]),
 ('דגם 7','תכלת־מנטה',[('m07-d1','נערה ראשונה',''),('m07-d2','נערה שנייה',''),('m07-big','ילדה גדולה',''),('m07-small','ילדה קטנה','')]),
 ('דגם 9','כחול־אפרפר',[('m09-d1','נערה ראשונה',''),('m09-d2','נערה שנייה',''),('m09-big','ילדה גדולה',''),('m09-small','ילדה קטנה','')]),
 ('דגם 10','שמנת עם גלים',[('m10-d1','נערה ראשונה',''),('m10-d2','נערה שנייה','')]),
 ('דגם 12','ורוד',[('m12-d1','נערה ראשונה','פסי קטיפה שחורים'),('m12-d2','נערה שנייה','קומות טול'),('m12-big','ילדה גדולה',''),('m12-small','ילדה קטנה','')]),
 ('דגם 13','שחור ובז׳',[('m13-d1','נערה ראשונה',''),('m13-d2','נערה שנייה',''),('m13-big','ילדה גדולה',''),('m13-small','ילדה קטנה','')]),
]
import os
def enc(path,h,q):
    im=Image.open(path).convert('RGB'); im.thumbnail((10000,h),Image.LANCZOS)
    b=io.BytesIO(); im.save(b,'JPEG',quality=q,optimize=True,progressive=True)
    return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode(), im.size
data=[]; n=0
for mt,mc,shots in MODELS:
    m={'title':mt,'color':mc,'shots':[]}
    for sid,who,extra in shots:
        imgs=[]
        for kind,label,h,q in [('closeup','תקריב',1100,80),('full','גוף מלא',1500,82),('side-full','צילום מהצד',1500,82)]:
            p=R+sid+'-'+kind+'.jpg'
            if os.path.exists(p):
                src,(w,hh)=enc(p,h,q); imgs.append({'id':sid+':'+kind,'label':label,'src':src,'w':w,'h':hh}); n+=1
        assert len(imgs)>=2,sid
        m['shots'].append({'who':who,'extra':extra,'imgs':imgs})
    data.append(m)
tpl=open(sys.argv[1],encoding='utf8').read()
html=tpl.replace('/*__DATA__*/null',json.dumps(data,ensure_ascii=False)).replace('__TOTAL__',str(n))
open(OUT,'w',encoding='utf8').write(html)
print(n,'images',round(len(html.encode())/1e6,2),'MB')
