# תיקון פתח צוואר בתקריבים (23.11) — הנחיות לסוכן

המשתמשת: "יש הרבה פתחי צוואר עם פתח וי מכוער. הכול צריך להיות עם לב עדין כמו ברפרנס הקובע". המשימה: לתקן בתקריבים שקיבלת **רק את פתח הצוואר**, בעריכה של התמונה הקיימת, בלי לשנות פנים, שיער, תסרוקת, בד או רקע. כתוב בעברית, אל תמחק קבצים, אל תדרוס קבצים קיימים, אל תעשה git commit/push.

## הרפרנס הקובע
- נשים: `9ZFVelCNYZ` (עותק מקומי `/home/user/SHOSHI-GELIS/review/neck-refs/women_black_sweetheart.jpg`).
- ילדות: `VXwCF2JMMU` (עותק מקומי `/home/user/SHOSHI-GELIS/review/neck-refs/girls_black_sweetheart_model4.jpg`).
לפתוח ולראות את שניהם לפני העבודה. הצורה: פתח גבוה וצנוע, צמוד לבסיס הצוואר, ברוחב הצוואר בלבד, מכסה את עצמות הבריח; **שתי קשתות רכות ומעוגלות** שנפגשות ב**שקע אחד קטן ורדוד** במרכז. לא V, לא חריץ, לא שסע, לא זווית חדה, לא עמוק, לא רחב, לא גלי עם כמה קשתות.
לוודא בתחילת העבודה (עם `mcp__Magnific-bcaf73fa__creations_get`) ששני המזהים קיימים בחשבון; אם לא, להעלות את העותקים המקומיים ולהשתמש במזהים החדשים.

## כלים והגדרות
רק `mcp__Magnific-bcaf73fa__*` (ToolSearch `select:mcp__Magnific-bcaf73fa__images_generate,mcp__Magnific-bcaf73fa__creations_wait,mcp__Magnific-bcaf73fa__creations_get`). folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.
`mode: "imagen-nano-banana-2-1"`, `resolution: "4k"`, `aspectRatio: "3:4"`, `count: 2`. רפרנסים: image 1 = התקריב הקיים (המזהה שקיבלת), image 2 = רפרנס הצוואר.
הורדה: `curl -sS -o x.png "<url מ־creations_wait>"` ואז המרה ל־JPEG 92 בגובה 3000px עם PIL (`python3 -I`).

## פרומפט (להתאים רק את הסוגריים)
"Edit image 1. Keep EVERYTHING exactly as it is: the same [woman/girl], the identical face, skin, eyes, expression, the identical hair and hairstyle[ and hair accessory], the same dress fabric, colour, texture and decoration, the same shoulders and sleeves, the same pure white background, framing and lighting. Change ONLY the shape of the neckline edge of the dress: make it the gentle modest sweetheart neckline of the black dress in image 2 — high and close to the base of the neck, only as wide as the neck, covering the collarbones, formed by two soft rounded curves that meet in ONE small, shallow, softly rounded dip in the centre. Not a V, not a pointed notch, not a slit, not a keyhole, not deep, not wide. A real, neatly sewn finished edge in the dress's own fabric[, the decoration continuing naturally up to the new edge]. No earrings, no jewellery. Photorealistic, razor-sharp."
חסימת NSFW שגויה (ילדות): לנסח מחדש ("portrait for a formal-wear dress rental catalog", "the young model"). כשל קיבולת / "24/24 slots": לנסות שוב אחרי דקה.

## בדיקה (בעיניים, לכל תוצאה)
1. פתח הצוואר: לב עדין כמו ברפרנס. לחתוך ולהגדיל את אזור הצוואר ולהשוות לרפרנס.
2. הפנים, העור, התסרוקת והאקססורי **לא השתנו** מול התקריב המקורי (להשוות זה לצד זה בהגדלה). אם הפנים השתנו: לפסול.
3. בד, צבע ועיטורים לא השתנו; אין עגילים; הרקע לבן.
סבב תיקון אחד לכל היותר, רק אם שתי האפשרויות נכשלות.

## תוצרים
- לכל שוט: `/home/user/SHOSHI-GELIS/review/r3/neckfix/<שוט>-neck.jpg` עם `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "BEFORE|<התקריב המקורי>" "1|<אפשרות 1>" "2|<אפשרות 2>"` (ליצור את התיקייה).
- שתי האפשרויות: `/home/user/SHOSHI-GELIS/review/r3/neckfix/<שוט>-nf1.jpg`, `-nf2.jpg`.
- דוח: טבלה עם שוט, מזהה אפשרות 1 ו־2, איזו טובה יותר, האם הפנים נשמרו, האם הצוואר עכשיו לב עדין (כן / חלקית / לא), וכל פגם שנשאר, בלי לייפות.
