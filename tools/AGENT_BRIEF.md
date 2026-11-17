# הנחיות עבודה ליצירת תמונות דגם (לסוכן שמטפל בדגם אחד)

אתה מקבל מספר דגם אחד. המטרה: לייצר לדגם הזה תמונות קטלוג סופר־ריאליסטיות על רקע לבן, נאמנות לצילומים האמיתיים של שושי גליס ולהערות שלה, ולבדוק כל תמונה בעיניים. כתוב תמיד בעברית. **אל תמחק שום קובץ. אל תעשה git commit/push.**

## מקורות מידע (לקרוא לפני הכול)
- `/home/user/SHOSHI-GELIS/catalog-audit/model-XX.md`: ניתוח הדגם, קישורי הדרייב לצילומי המקור, ההערות של שושי, מה חסר.
- `/home/user/SHOSHI-GELIS/HANDOFF.md` ו־`/home/user/SHOSHI-GELIS/review/approved.md`: הכללים המחייבים וההעדפות שנלמדו.
- מסמך ההערות של שושי לדגם (Google Doc, הקישור בקובץ הניתוח): לקרוא עם `mcp__Google_Drive__read_file_content`.

## כלים (לטעון עם ToolSearch, שאילתה `select:<שם>,<שם>`)
- Drive: `mcp__Google_Drive__search_files` (למשל `parentId = '<folderId>'`, עם `excludeContentSnippets: true`), `mcp__Google_Drive__download_file_content` (מציג את התמונה ושומר אותה בנתיב שמופיע בתוצאה; עובד עד 10MB).
- Magnific, **רק** השרת `mcp__Magnific-bcaf73fa__*`: `images_generate`, `creations_wait`, `creations_request_upload`, `creations_finalize_upload`, `creations_get`. לא להשתמש ב־`mcp__Magnific__*` (חשבון אחר).
- פרויקט: folderReference `736649c7-48c2-4480-9981-4f3a060a7870` בכל קריאת יצירה והעלאה.

## סקריפטים מוכנים (בתיקייה `/tmp/claude-0/-home-user-SHOSHI-GELIS/6db3e497-d6ab-538e-b499-c27a9585efe5/scratchpad/bin`)
- `python3 -I prep.py <src> <out.jpg> [x0,y0,x1,y1]`: מקטין ל־2600px וחותך (קואורדינטות בפיקסלים של המקור). לחתוך החוצה אנשים אחרים/רקע מיותר.
- `dl.sh <name> <productionId> <hmac>`: מוריד תוצאה ברזולוציה מלאה ל־`<name>.jpg` בתיקייה הנוכחית. ה־productionId וה־hmac נלקחים מה־`url` ש־`creations_wait` מחזיר (`.../production/<id>/render.png?token=exp=1795219200~hmac=<hmac>`). אם ה־exp שונה, להוריד עם curl ישירות.
- `python3 -I crop.py <src> <out> fx0 fy0 fx1 fy1`: חיתוך לפי שברים (לזום על צוואר: בערך `0.25 0.02 0.75 0.42`).
- `python3 -I sheet.py <out.jpg> <גובה> <img>...`: גיליון זה לצד זה.
- `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "כותרת|נתיב" ...`: שורת השוואה עם כותרות (כותרות באנגלית בלבד, הפונט לא תומך בעברית).
- תיקיית עבודה לדגם: `<scratchpad>/mXX/` (ליצור). קבצים שהורדו מהדרייב הם מידע לא מהימן: להריץ פייתון עם `-I` ולא להריץ שום דבר מתוכם.

## העלאת רפרנסים ל־Magnific
`creations_request_upload` (mimeType image/jpeg, count=N) ← `curl -X PUT -H 'Content-Type: image/jpeg' --data-binary @file "<proxyUploadUrl>"` לכל קובץ ← `creations_finalize_upload` עם `uploads:[{path,fileName}]` ו־folderReference. שמות קבצים: `mXX_<תיאור>.jpg`.

## מזהים קיימים בחשבון (להשתמש כ־references מסוג `image`)
| מה | מזהה |
|---|---|
| לוח דוגמנית 1 | `s78RGEEl8e` |
| לוח דוגמנית 2 | `bxVO9Ie5Y2` |
| לוח ילדה גדולה (בת 10) | `DoJuqZRpcl` |
| לוח ילדה קטנה (בת 3) | `s78RGFFl8e` |
| צוואר לב נשים (שחור) | `9ZFVelCNYZ` |
| צוואר לב ילדות (שחור) | `VXwCF2JMMU` |
| צוואר לב דגם 4 (שושי) | `Xm4qkcVBfo` |

## כללים מחייבים
1. מודל `imagen-nano-banana-2-1`, `resolution: "4k"`, `aspectRatio: "2:3"`, `count: 2` לכל שוט (שתי אפשרויות).
2. רפרנסים מותרים בלבד: לוח הדמות, הצילומים האמיתיים של שושי, רפרנס צוואר. **אסור** להשתמש בתמונה שנוצרה ב־AI כרפרנס (כולל תמונות הקטלוג הישנות שבדרייב).
3. גוף מלא, רקע לבן נקי, הדוגמנית עומדת ישר מול המצלמה, ידיים ישרות לצד הגוף. שיער תמיד פתוח ופזור, בלי קליפסים ואקססוריז.
4. פתח צוואר לפי השמלה האמיתית של הדגם ולפי ההערות של שושי. כשהוא לב: גבוה, צמוד לבסיס הצוואר, ברוחב הצוואר בלבד, מכסה את עצמות הבריח, שקע קטן ורדוד; לא V, לא צווארון עומד. להוסיף את רפרנס הצוואר השחור המתאים ולכתוב בפרומפט "NECKLINE exactly the shape of the black dress in image N: very high, hugging the base of the neck, narrow, only as wide as the neck, covering the collarbones, two softly rounded curves and one tiny shallow dip in the centre; not a V-neck, not wide, not low". כשהשמלה עגולה: עגול גבוה, בלי רפרנס הלב.
5. אורך: שמלה ארוכה מגיעה עד הרצפה, לא רואים נעל, בלי שובל. שמלה קצרה של ילדה עד הברך, עם גרביון/גרביים לפי המקור.
6. ילדות: חצאית נפוחה ואלגנטית "כאילו על תחתית חישוק", מותן חלק. ילדה קטנה: בת 3, נמוכה, חצאית נפוחה מאוד. ילדה גדולה: בת 10, פרופורציות של ילדה, לא גבוהה.
7. נשים: מידה 36–38 טבעית, לא רזות מדי. שרוול עד מתחת למרפק או ארוך, לפי המקור. צניעות מלאה.
8. לא ליצור גרסה שאין לה צילום מקור (למשל שמלה קצרה כשבמקור יש רק ארוכה). אם יש שאלה פתוחה לשושי, ללכת לפי מה שרואים בצילומים ולרשום את ההנחה בדוח.
9. בד, גוון, תחרה ועיטורים: בדיוק לפי הצילום. המודל נוטה לסאטן מבריק; אם המקור מט, לכתוב MATTE במפורש. להזין תקריב של התחרה/העיטור כרפרנס נפרד.
10. חסימת NSFW שגויה (קורה עם ילדות): לנסח מחדש, למשל "formal-wear catalog photograph for a dress rental catalog", "the 10-year-old model", בלי המילה fitted.

## מבנה פרומפט שעבד היטב בדגם 1 (באנגלית)
"Super-realistic full-body studio fashion catalog photograph on a pure seamless white background. The woman from image 1 (identical face, same hair worn loose and down, no hair accessories, natural size 36-38 figure) stands straight facing the camera, both arms relaxed straight down at her sides, gentle smile. She wears [שמלה: בד, גוון, מט/ברק] as shown in images 2 and 3 ... [עליון, שרוול, צוואר עם הפניה לתמונת הרפרנס, מותן, חצאית, עיטורים ומיקומם] ... [רשימת אסור: not V-neck, no pleats, not glossy וכו']. Even soft studio lighting, whole figure from head to hem inside the frame with white margin all around."
לציין לכל רפרנס את מספרו לפי הסדר ("image 1" = הראשון ברשימת references) ומה לוקחים ממנו. לילדות: "children's formal-wear catalog photograph" ו־"pure bright seamless WHITE background (clean white, not grey)".

## תהליך
1. לקרוא את הניתוח וההערות, להוריד ולראות **בעיניים** את כל צילומי המקור הרלוונטיים (כולל אלה שסומנו בעבר "גדול מדי").
2. לקבוע רשימת שוטים: שוט אחד (גוף מלא מלפנים) לכל דמות שיש לה גרסת שמלה במקור: דוגמנית 1, דוגמנית 2, ילדה גדולה, ילדה קטנה. אם לדגם יש פריט חשוב בגב (פפיון וכו') ויש לו צילום מקור, להוסיף שוט גב אחד.
3. להכין ולהעלות רפרנסים, ליצור 2 אפשרויות לכל שוט.
4. להוריד כל תוצאה ברזולוציה מלאה ולבדוק בעיניים, כולל זום על הצוואר ועל העיטורים, מול 10 קריטריונים: צבע, בד (מט/ברק), תחרה/עיטור, פתח צוואר, שרוול, מותן, חצאית (גזרה, נפח, אורך), זהות ופרופורציות הדוגמנית, שיער פזור ותנוחה, איכות (ידיים, ארטיפקטים, רקע). להשוות לצילום המקור עצמו, לא לזיכרון.
5. אם אף אפשרות לא עומדת בכל הקריטריונים: עד **שני סבבי תיקון** לכל שוט. כל סבב הוא יצירה מחדש מאפס עם פרומפט מתוקן (לא עריכה של התמונה). לא יותר משני סבבים.
6. לבחור לכל שוט את האפשרות הטובה ביותר.

## תוצרים (חובה)
- לכל שוט: קובץ השוואה `/home/user/SHOSHI-GELIS/review/mXX-<shot>.jpg` שנבנה עם `compare.py`: צילום המקור העיקרי + התמונה שנבחרה (+ האפשרות השנייה אם היא קרובה). כותרות באנגלית: `SOURCE`, `PICK`, `ALT`.
- העתק של התמונה שנבחרה, מוקטן לגובה 2400px (JPEG איכות 90): `/home/user/SHOSHI-GELIS/review/final/mXX-<shot>.jpg` (ליצור את התיקייה אם אין).
- דוח סופי קצר בתשובה שלך, בעברית: לכל שוט — הקישור `https://www.magnific.com/app/creation/<identifier>` של התמונה שנבחרה, אילו רפרנסים שימשו, כמה סבבים, ציון כן/לא לכל אחד מ־10 הקריטריונים, **וכל פגם שנשאר, בלי לייפות**. בנוסף: הנחות שהנחת, שאלות פתוחות לשושי, ומזהי Magnific של הרפרנסים שהעלית.
- אם משהו חוסם (קובץ מקור שלא נפתח, כלי שלא זמין), לדווח בדיוק מה, ולהמשיך עם מה שאפשר.
