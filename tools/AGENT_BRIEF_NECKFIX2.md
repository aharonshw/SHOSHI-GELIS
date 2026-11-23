# תיקון פתח צוואר ממוסך (23.11, שיטה ב') — הנחיות לסוכן

עריכה רגילה לא הצליחה להפוך V ללב עדין. מה שעובד: **retouch ממוסך ומדויק ב־GPT 2.6**, שמשנה רק את האזור הלבן במסכה ומשאיר את כל השאר (פנים, שיער, רקע) פיקסל לפיקסל. דוגמה לתוצאה טובה: `/home/user/SHOSHI-GELIS/review/r3/neckfix2/method-test.jpg` (BEFORE מול 2). הרפרנס לצורה: `/home/user/SHOSHI-GELIS/review/neck-refs/women_black_sweetheart.jpg`, `girls_black_sweetheart_model4.jpg`. לפתוח ולראות את שלושתם. כתוב בעברית, אל תמחק ואל תדרוס קבצים, אל תעשה git commit/push.

## כלים
ToolSearch `select:mcp__Magnific-bcaf73fa__images_retouch,mcp__Magnific-bcaf73fa__creations_wait,mcp__Magnific-bcaf73fa__creations_get,mcp__Magnific-bcaf73fa__creations_request_upload,mcp__Magnific-bcaf73fa__creations_finalize_upload`. folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.

## תהליך לכל שוט
1. `creations_get` למזהה התקריב → להוריד את ה־`url` המלא (PNG) עם curl; לבדוק את הגודל בפיקסלים (בדרך כלל 3584×4800).
2. לפתוח גרסה מוקטנת ולמצוא את קו הצוואר. לבנות **מסכה באותו גודל פיקסלים בדיוק**: שחור מלא, ומלבן לבן שמכסה את קצה הצוואר של השמלה מכתף לכתף: מעט עור מעל הקצה (כ־3% מגובה התמונה מעל הנקודה הגבוהה של הקצה) ועד כ־5–6% מתחת לתחתית השקע. המלבן **לא** נוגע בסנטר, בפנים או בקישוט חשוב; שיער שנופל על הכתפיים מותר שייכנס מעט בצדדים אבל עדיף לצמצם את הרוחב כך שיישאר בחוץ. לשמור תצוגה מקדימה עם מסגרת אדומה ולהסתכל עליה לפני ההעלאה.
3. להעלות את המסכה (PNG, `creations_request_upload` mimeType image/png → `curl -X PUT -H 'Content-Type: image/png' --data-binary @mask.png "<proxyUploadUrl>"` → `creations_finalize_upload` עם `visible: false`).
4. `images_retouch`: `creationIdentifier` = התקריב, `maskCreationIdentifier` = המסכה, `mode: "replace"`, `editType: "precise"`, `model: "retouch-precise-gpt-2-6"` (270 קרדיטים), פרומפט:
"The top edge of the [woman's/girl's] [צבע ובד] dress bodice at the base of her neck: a gentle modest sweetheart neckline — a high edge, only as wide as the neck, with two soft, rounded, convex curves that meet in one small, shallow, softly rounded dip in the centre, like the top of a heart. Not a V, no straight diagonal lines, not pointed, not deep, not wide. A neatly sewn finished edge in the same [בד]; [העיטור/הרקמה/הפייטים] continues below the edge exactly as around it; natural skin of the neck above; the same hair where it crosses the area."
5. `creations_wait`, להוריד, ולבדוק **בעיניים**: (א) חיתוך מוגדל של הצוואר לפני/אחרי מול הרפרנס: לב עדין? (ב) שאין תפר/גבול נראה בקצה המסכה, ושהבד והעיטור ממשיכים טבעי; (ג) שמחוץ למסכה לא השתנה דבר (אפשר לוודא חישובית: הפרש פיקסלים מחוץ למלבן קרוב לאפס).
6. אם התוצאה לא לב עדין או שיש גבול נראה: ניסיון **אחד** נוסף (מסכה מעט שונה או ניסוח מחוזק). לא יותר.

## תוצרים
- `/home/user/SHOSHI-GELIS/review/r3/neckfix2/<שוט>-nk.jpg`: התוצאה הנבחרת, מוקטנת לגובה 3000px, JPEG 92.
- `/home/user/SHOSHI-GELIS/review/r3/neckfix2/<שוט>-cmp.jpg`: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "BEFORE|<חיתוך צוואר לפני>" "AFTER|<חיתוך צוואר אחרי>" "FULL|<התקריב המתוקן המלא>"`.
- דוח: טבלה עם שוט, מזהה Magnific של התוצאה הנבחרת, מספר ניסיונות, האם לב עדין (כן / חלקית / לא), האם יש גבול נראה, וכל פגם שנשאר. בלי לייפות.
