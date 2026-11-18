# שלב התקריבים (18.11) — הנחיות לסוכן

המשתמשת קבעה שיטה: לכל תמונה בקטלוג יוצרים קודם **תקריב** (קלוזאפ הדוק על הפנים, עם התסרוקת ועליון השמלה), היא מאשרת אותו, ורק אחר כך נבנה ממנו הגוף המלא. המשימה שלך: ליצור **רק תקריבים** לשוטים שקיבלת, שתי אפשרויות לכל שוט, ולהכין תמונת השוואה לכל שוט. לא ליצור גוף מלא. כתוב בעברית, אל תמחק קבצים, אל תעשה git commit/push.

## כלים
- לטעון עם ToolSearch (`select:<שם>,<שם>`): `mcp__Magnific-bcaf73fa__images_generate`, `mcp__Magnific-bcaf73fa__creations_wait`, ואם צריך להעלות קובץ: `mcp__Magnific-bcaf73fa__creations_request_upload`, `mcp__Magnific-bcaf73fa__creations_finalize_upload` (PUT עם `curl -X PUT -H 'Content-Type: image/jpeg' --data-binary @file "<proxyUploadUrl>"`). רק השרת `Magnific-bcaf73fa`.
- folderReference בכל קריאה: `736649c7-48c2-4480-9981-4f3a060a7870`.
- סקריפטים ב־`/tmp/claude-0/-home-user-SHOSHI-GELIS/6db3e497-d6ab-538e-b499-c27a9585efe5/scratchpad/bin`: `dl.sh <name> <productionId> <hmac>` (מוריד תוצאה ל־`<name>.jpg` בתיקייה הנוכחית; המזהים מה־`url` ש־`creations_wait` מחזיר), `python3 -I crop.py <src> <out> fx0 fy0 fx1 fy1`, `python3 -I sheet.py <out> <גובה> <img>...`. השוואה עם כותרות: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "LABEL|path" ...` (כותרות באנגלית בלבד).
- תיקיית עבודה: `<scratchpad>/cu/<שם הקבוצה>/`.

## הגדרות יצירה (קבועות)
`mode: "imagen-nano-banana-2-1"`, `resolution: "4k"`, `aspectRatio: "3:4"`, `count: 2`. עלות 145 קרדיטים לתמונה. סבב תיקון אחד לכל היותר, ורק אם שתי האפשרויות נכשלות בקריטריון חובה.

## רפרנסים (בסדר הזה)
1. חיתוך הפנים של הדמות (image 1).
2. לוח הדמות המלא (image 2).
3. תמונת השמלה המאושרת של אותו שוט (image 3), רק לעליון השמלה ולצוואר.

| דמות | חיתוך פנים | לוח |
|---|---|---|
| דוגמנית 1 | `Lw8ggojswO` | `s78RGEEl8e` |
| דוגמנית 2 | `jUollBlLD0` | `bxVO9Ie5Y2` |
| ילדה גדולה (בת 10) | `gOmwwIGSXO` | `rgd1Edrxtc` |
| ילדה קטנה (בת 3–4) | `s782at2l8e` (פזור עם צמות) | `rgditoCxtc` (אסוף) |

לילדה הקטנה אין לוח: שתי תמונות המקור שלה הן image 1 ו־image 2. לא להוסיף לה רפרנסים מעבר לשלושה (יותר מדי רפרנסים משנים אותה).
עותקים מקומיים לבדיקת דמיון: `<scratchpad>/faces/face_big_v2.jpg`, `face_d1.jpg`, `face_d2.jpg`; לילדה הקטנה `/home/user/SHOSHI-GELIS/review/boards/small_original_loose_braids.jpg` ו־`small_original_updo.jpg`.

## תבנית הפרומפט (עבדה ואושרה; להחליף רק את החלקים בסוגריים)
"Tight close-up studio portrait photograph, head and shoulders only, the face fills most of the frame, pure white seamless background. This is the SAME real [girl/woman] as in images 1 and 2, photographed again on the same day: copy her face exactly, with no changes at all — identical face shape, identical [eye colour] eyes and eye shape, identical nose, identical lips, identical eyebrows, identical skin tone, identical hair colour. [She is 10 years old. / She is a small 3-year-old girl.] Real, natural skin as in a true unretouched professional photograph: naturally smooth and healthy with fine real skin texture[, soft natural freckles across the nose and cheeks — לילדה הגדולה בלבד], not airbrushed, not plastic, not AI-smoothed, no blotches, no red patches. Razor-sharp focus on the eyes, 85mm lens, soft even studio light, natural accurate colours. Hair: [התסרוקת מהטבלה]. No earrings, bare earlobes, no jewellery. She looks straight at the camera with a gentle closed-mouth smile. At the bottom of the frame the top of her dress is visible, as in image 3: [בד, צבע, צורת פתח הצוואר, כתפיים/ראש שרוול]."
- צבע עיניים: דוגמנית 1 ודוגמנית 2 כחול; ילדה גדולה blue-grey; ילדה קטנה grey-green (ויש לה פוני, שיער honey-brown).
- לדוגמניות יש עגילים בלוח: בתקריב אין עגילים.
- פתח הצוואר והעליון: בדיוק כמו בתמונת השמלה המאושרת (image 3). לפתוח את התמונה ולראות אותה לפני הכתיבה.

## קריטריונים (לבדוק בעיניים כל תוצאה, ברזולוציה מלאה, מול חיתוך הפנים המקורי)
1. **זהות:** אותה דמות בדיוק. אם הפנים רחבות/צרות יותר, גיל שונה או תווים שונים: לפסול.
2. **עור:** טבעי וחלק, לא מוחלק כמו AI, בלי כתמים, בלי מרקם רינדור. לילדה הגדולה נמשים עדינים וטבעיים מותרים.
3. **חדות:** עיניים וריסים חדים.
4. **תסרוקת:** כמו בטבלה.
5. **בלי עגילים ותכשיטים.**
6. **עליון השמלה:** צבע, בד ופתח צוואר כמו בתמונת השמלה המאושרת.
7. **מסגור:** הדוק, ראש וכתפיים, רקע לבן.

## תוצרים
- לכל שוט: `/home/user/SHOSHI-GELIS/review/r3/closeups/mXX-<shot>-closeup.jpg` שנבנה עם `compare.py`: `"ORIGINAL|<חיתוך הפנים המקורי>" "1|<אפשרות 1>" "2|<אפשרות 2>"`. הכותרות חייבות להיות `ORIGINAL`, `1`, `2`.
- שני הקבצים המלאים (מוקטנים לגובה 3000px, JPEG איכות 92): `/home/user/SHOSHI-GELIS/review/r3/closeups/mXX-<shot>-cu1.jpg` ו־`-cu2.jpg`.
- דוח סופי קצר: טבלה עם שוט, מזהה Magnific של אפשרות 1 ושל אפשרות 2, איזו לדעתך דומה יותר למקור, וכל פגם שנשאר (בלי לייפות). לציין גם את מזהי הרפרנסים שהעלית, אם העלית.
