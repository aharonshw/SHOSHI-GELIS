# שלב הגוף המלא (18.11) — הנחיות לסוכן

המשתמשת אישרה תקריב (קלוזאפ) לכל שוט. המשימה שלך: לבנות מכל תקריב מאושר **תמונת גוף מלא**, שתי אפשרויות לכל שוט, ולהכין תמונת השוואה. כתוב בעברית, אל תמחק קבצים, אל תעשה git commit/push.

## כלים
- לטעון עם ToolSearch (`select:<שם>,<שם>`): `mcp__Magnific-bcaf73fa__images_generate`, `mcp__Magnific-bcaf73fa__creations_wait`. רק השרת `Magnific-bcaf73fa`. folderReference בכל קריאה: `736649c7-48c2-4480-9981-4f3a060a7870`.
- סקריפטים ב־`/tmp/claude-0/-home-user-SHOSHI-GELIS/6db3e497-d6ab-538e-b499-c27a9585efe5/scratchpad/bin`: `dl.sh <name> <productionId> <hmac>` (מוריד תוצאה ל־`<name>.jpg` בתיקייה הנוכחית; המזהים מה־`url` ש־`creations_wait` מחזיר), `python3 -I face.py <src> <out> 0.115` (חותך את הפנים ב־100% מתמונת גוף מלא), `python3 -I crop.py <src> <out> fx0 fy0 fx1 fy1`, `python3 -I sheet.py <out> <גובה> <img>...`. השוואה עם כותרות: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "LABEL|path" ...` (כותרות באנגלית בלבד).
- תיקיית עבודה: `<scratchpad>/fb/<שם הקבוצה>/`.

## הגדרות יצירה (קבועות)
`mode: "imagen-nano-banana-2-1"`, `resolution: "4k"`, `aspectRatio: "2:3"`, `count: 2`. עלות 145 קרדיטים לתמונה. סבב תיקון אחד לכל היותר, ורק אם שתי האפשרויות נכשלות בקריטריון חובה.

## רפרנסים (בסדר הזה, שלושה בלבד)
1. התקריב המאושר של השוט (image 1): המקור לפנים, לעור, לתסרוקת ולאקססורי בשיער.
2. תמונת השמלה המאושרת של השוט (image 2): המקור לשמלה, לנפח, לפרופורציות ולתנוחה. **לא** להעתיק ממנה פנים, עור או תסרוקת.
3. חיתוך הפנים המקורי של הדמות (image 3): דוגמנית 1 `Lw8ggojswO`, דוגמנית 2 `jUollBlLD0`, ילדה גדולה `gOmwwIGSXO`, ילדה קטנה `s782at2l8e`.
המזהים של התקריב ושל השמלה לכל שוט: `/home/user/SHOSHI-GELIS/catalog-refs/approved-closeups.md`. העותק המקומי של התקריב המאושר: `/home/user/SHOSHI-GELIS/catalog-refs/<שוט>-closeup.jpg`. לפתוח ולראות את התקריב ואת תמונת השמלה לפני כתיבת הפרומפט (את תמונת השמלה אפשר לראות עם `mcp__Magnific-bcaf73fa__creations_read`, `hq: "medium"`).

## תבנית הפרומפט (עבדה ואושרה; להחליף רק את החלקים בסוגריים)
"Full-body professional studio [fashion catalog photograph / photograph for a children's formal-wear catalog], pure white seamless background, razor-sharp, true-to-life, shot on a high-end full-frame camera, the face perfectly in focus. The [woman/girl] is exactly the [woman/girl] in the close-up portrait image 1 (and image 3): the same face with no changes, the same natural skin[ with soft natural freckles — ילדה גדולה בלבד], the same [eye colour] eyes, the same hairstyle as image 1 — [תיאור התסרוקת והאקססורי כפי שהם בתקריב]. [Natural size 36-38 figure. / She is 10 years old with a child's proportions. / She is a small 3-year-old girl: very short, toddler proportions, large head relative to her body.] No earrings, bare earlobes, no jewellery. She stands straight facing the camera, arms relaxed down at her sides, gentle closed-mouth smile. She wears exactly the dress of image 2, same shape, same proportions and same volume: [תיאור מדויק של השמלה כפי שהיא בתמונת השמלה: בד, צבע, עליון, פתח צוואר, שרוולים, מותן צרה, חצאית ונפח, עיטורים, אורך]. [Hem at the floor, shoes hidden. / לשמלה קצרה: hem at the knee, ותיאור הגרביים והנעליים כמו בתמונת השמלה.] Do not copy the face, the skin or the hairstyle from image 2. Whole figure from head to hem in frame with white margin around, natural accurate colours."
- צבע עיניים: דוגמניות כחול; ילדה גדולה blue-grey; ילדה קטנה grey-green (ויש לה פוני, שיער honey-brown).
- פתח הצוואר, השרוולים והעיטורים: לפי **תמונת השמלה המאושרת** (image 2), לא לפי התקריב. בתקריבים פתח הצוואר לפעמים יצא עם שקע לב חד מדי.
- חסימת NSFW שגויה (קורה עם ילדות): לנסח מחדש ("formal-wear catalog photograph for a dress rental catalog", "the young model") ולנסות שוב.

## קריטריונים (לבדוק בעיניים כל תוצאה ברזולוציה מלאה)
1. **פנים:** חיתוך הפנים ב־100% (`face.py`) מול התקריב המאושר: אותה דמות, עור טבעי, בלי כתמים. אם הפנים שונות: לפסול.
2. **תסרוקת ואקססורי:** כמו בתקריב.
3. **שמלה:** זהה לתמונת השמלה המאושרת: צבע, בד, פתח צוואר, שרוולים, מותן צרה, נפח החצאית, עיטורים, אורך.
4. **פרופורציות:** דוגמנית 36–38; ילדה גדולה בת 10, לא גבוהה; ילדה קטנה בת 3–4, נמוכה.
5. **בלי עגילים ותכשיטים**, ידיים תקינות, רקע לבן, כל הדמות בפריים.

## תוצרים
- לכל שוט: `/home/user/SHOSHI-GELIS/review/r3/full/<שוט>-full.jpg` שנבנה עם `compare.py`: `"CLOSEUP|<התקריב המאושר>" "DRESS|<תמונת השמלה המאושרת, אם יש עותק מקומי; אחרת להוריד אותה>" "1|<אפשרות 1>" "2|<אפשרות 2>"`. הכותרות חייבות להיות `CLOSEUP`, `DRESS`, `1`, `2`. ליצור את התיקייה אם אין.
- שני הקבצים המלאים ברזולוציה מלאה (JPEG איכות 92, בלי הקטנה): `/home/user/SHOSHI-GELIS/review/r3/full/<שוט>-fb1.jpg` ו־`-fb2.jpg`.
- דוח סופי קצר: טבלה עם שוט, מזהה Magnific של אפשרות 1 ושל אפשרות 2, איזו לדעתך טובה יותר, וכל פגם שנשאר (בלי לייפות).
