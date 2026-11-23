# תיקוני גוון לפי משוב שושי (24.11) — תמונות גוף מלא — הנחיות לסוכן

שושי (הלקוחה) ביקשה לשנות **רק את גוון השמלה** בכמה תמונות גוף מלא. כל השאר נשאר בדיוק כמו שהוא: הדמות, הפנים, השיער, התנוחה, גזרת השמלה, הבד, העיטורים, הרקע הלבן והפריים. כתוב בעברית, אל תמחק ואל תדרוס קבצים, אל תעשה git commit/push, אל תיגע ב־`catalog-refs/`.

## כלים והגדרות
ToolSearch `select:mcp__Magnific-bcaf73fa__images_generate,mcp__Magnific-bcaf73fa__creations_wait,mcp__Magnific-bcaf73fa__creations_get,mcp__Magnific-bcaf73fa__creations_read,mcp__Magnific-bcaf73fa__creations_request_upload,mcp__Magnific-bcaf73fa__creations_finalize_upload`. רק השרת `Magnific-bcaf73fa`. folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.
עריכה ישירה של התמונה: `mode: "imagen-nano-banana-2-1"`, `resolution: "4k"`, `aspectRatio: "2:3"`, `count: 2` (145 קרדיטים לתמונה). references: image 1 = תמונת הגוף המלא, image 2 = רפרנס הגוון (אם יש).
הורדה: `curl -sS -o x.png "<url מ־creations_wait>"`, המרה ל־JPEG 92 עם PIL (`python3 -I`).
אם Nano כמעט לא שינה את הגוון בשתי האפשרויות (בדיקה חישובית: ממוצע צבע השמלה כמעט זהה למקור): ניסיון אחד עם `mcp__Magnific-bcaf73fa__images_retouch` במצב `mode: "edit"`, `referenceIdentifiers: [<רפרנס הגוון>]`, אותו פרומפט (270 קרדיטים).

## פרומפט (להתאים)
"Edit image 1. Change ONLY the colour of the dress: make it exactly [the same colour as the dress in image 2 / התיאור]. Keep EVERYTHING else exactly as it is: the same [woman/girl], identical face, skin, hair and hairstyle, the same pose, the same dress cut, fabric, sheen, texture, folds, volume, sleeves, neckline and decorations[ — העיטורים לפי מה שרואים, שנשארים בצבעם], the same shoes, the same pure white background, framing and lighting. Do not copy anything from image 2 except the dress colour. No earrings, no jewellery. Photorealistic."
חסימת NSFW שגויה (ילדות): לנסח מחדש ("the young model", "children's formal-wear catalog"). כשל קיבולת: לנסות שוב אחרי דקה.

## בדיקה בעיניים
1. הגוון החדש מול הרפרנס, זה לצד זה (גיליון). 2. הפנים, השיער והתנוחה לא השתנו (חיתוך פנים מוגדל מול המקור). 3. הגזרה, הבד, העיטורים והצוואר לא השתנו. 4. רקע לבן, כל הדמות בפריים.

## תוצרים
- `review/r3/color/<שוט>-c1.jpg`, `-c2.jpg` (רזולוציה מלאה, JPEG 92).
- `review/r3/color/<שוט>-cmp.jpg`: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "NOW|<המקור>" "TARGET|<רפרנס הגוון, אם יש>" "1|..." "2|..."`.
- דוח: טבלה עם שוט, מזהי 1 ו־2, איזו טובה יותר, האם הגוון הגיע ליעד (כן/חלקית/לא), האם הפנים נשמרו, וכל פגם, בלי לייפות.
