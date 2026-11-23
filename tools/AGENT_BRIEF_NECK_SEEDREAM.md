# גזרת צוואר מדויקת לפי דגם 5 — Seedream 5.5 (24.11) — הנחיות לסוכן

המשתמשת אישרה שיטה: **Seedream 5.5 עם שני רפרנסים**. רפרנס 1 = התקריב (הדמות, השיער, סוג הבד, הצבע והעיטורים). רפרנס 2 = **רק חיתוך הצוואר של דגם 5** (בלי הילדה) שקובע את הגזרה המדויקת של פתח הצוואר. דוגמאות מאושרות: `review/r3/neck4/test4-neck.jpg` (שורה 1 ושורה 4, אפשרות 1) ו־`review/r3/neck4/m12-d1-neck-cmp.jpg` (אפשרות 1). לפתוח ולראות אותן, ואת הסטנדרט `review/neck-refs/STANDARD_m05_small_neck.jpg`.
כתוב בעברית, אל תמחק ואל תדרוס קבצים, אל תעשה git commit/push, אל תיגע ב־`catalog-refs/`.

## כלים והגדרות
ToolSearch `select:mcp__Magnific-bcaf73fa__images_generate,mcp__Magnific-bcaf73fa__creations_wait,mcp__Magnific-bcaf73fa__creations_get,mcp__Magnific-bcaf73fa__creations_request_upload,mcp__Magnific-bcaf73fa__creations_finalize_upload`. רק השרת `Magnific-bcaf73fa`. folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.
`mode: "seedream-5-5"`, `resolution: "2k"`, `aspectRatio: "3:4"`, `count: 2` (60 קרדיטים לתמונה). **בלי הגדלה** (המשתמשת לא צריכה 4K).
references: `[{type:"image", identifier:<מקור>}, {type:"image", identifier:"MBO7u25DCm"}]` (`MBO7u25DCm` = חיתוך הצוואר של דגם 5).

## מקור לכל שוט
המזהה שקיבלת בטבלה. אם כתוב "להעלות": להעלות את הקובץ המקומי כמו שהוא (`creations_request_upload` image/jpeg → `curl -X PUT -H 'Content-Type: image/jpeg' --data-binary @file "<proxyUploadUrl>"` → `creations_finalize_upload` עם `visible: false`).

## פרומפט (להחליף רק סוגריים)
"Edit image 1[, a portrait for a children's formal-wear catalog — לילדות]. Image 1 decides the [woman/girl] and the dress: the same [woman/girl], identical face, hair[ and hair accessory], skin, pose, framing, white background, and the same [צבע ובד ועיטורים בדיוק כפי שהם בתמונה]. Image 2 decides ONLY the neckline: give the dress in image 1 exactly the same neckline cut and shape as the dark green dress in image 2 — same height at the base of the neck, same narrow width (only as wide as the neck, the edge rises to meet the neck at both sides and does not run out towards the shoulders), the same two small soft curves and the same small notch with a tiny point in the centre, a clean plain edge with no seam, no band and no trim[, the (עיטור) continuing naturally below the edge without outlining it]. Copy nothing else from image 2. No earrings, no jewellery. Photorealistic studio photo, razor-sharp."
חסימת NSFW שגויה (ילדות): לנסח מחדש ("the young model", "formal-wear catalog"). כשל קיבולת: לנסות שוב אחרי דקה.

## בדיקה בעיניים (לכל אפשרות)
1. **צוואר** (חיתוך מוגדל מול הסטנדרט): אותה גזרה: גבוה, צר, שתי קשתות ושקע קטן עם חוד; בלי תפר/פס/מסגרת; העיטור לא מקיף את הקצה כמו מסגרת.
2. **פנים** (חיתוך פנים מול המקור, זה לצד זה): אותה דמות, אותה תסרוקת, בלי עגילים. אם הפנים השתנו: לפסול.
3. בד, צבע ועיטורים כמו במקור; רקע לבן; הפריים כמו במקור.
אם שתי האפשרויות נכשלות: ניסיון **אחד** נוסף עם ניסוח מחוזק (לא יותר).

## תוצרים
- `review/r3/neck5/<שוט>-sd1.jpg`, `-sd2.jpg` (JPEG 92, ברזולוציה שהתקבלה).
- `review/r3/neck5/<שוט>-cmp.jpg`: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "STANDARD|<חיתוך צוואר מהסטנדרט>" "NOW|<חיתוך צוואר מהמקור>" "1|<חיתוך מאפשרות 1>" "2|<חיתוך מאפשרות 2>"` — אותו חיתוך יחסי בכולם (למשל x 22%–78%, y 60%–95%).
- `review/r3/neck5/<שוט>-face.jpg`: `"NOW|..." "1|..." "2|..."` חיתוכי פנים.
- דוח: טבלה עם שוט, מזהה המקור, מזהי 1 ו־2, איזו טובה יותר, צוואר (כמו הסטנדרט / חלקית / לא), פנים נשמרו (כן/לא), וכל פגם, בלי לייפות.
