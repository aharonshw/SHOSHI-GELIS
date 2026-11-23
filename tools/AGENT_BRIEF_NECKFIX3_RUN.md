# הרצת תיקון הצוואר לפי הסטנדרט (אחרי ניסוי השיטה) — הנחיות לסוכן

קרא קודם את `/home/user/SHOSHI-GELIS/tools/AGENT_BRIEF_NECKFIX3.md` (הסטנדרט, הפרומפט, הבדיקה). כאן התהליך המדויק. כתוב בעברית, אל תמחק ואל תדרוס קבצים, אל תעשה git commit/push, אל תיגע ב־`catalog-refs/`.

## מה הוכח בניסוי (`review/r3/neck3-test/2-cmp.jpg`, `3-cmp.jpg`, `4-cmp.jpg` — לפתוח ולראות)
`images_retouch`, `mode: "replace"`, `editType: "precise"`, **`model: "retouch-precise-gpt-2-6"`** (270 קרדיטים), פרומפט NECKFIX3 כלשונו, ומסכת **מצולע צר** שעוקב אחרי קצה הצוואר הקיים: מוריד את הפס/התפר ונותן קצה נקי. לא להשתמש ב־Nano או ב־Ideogram.

## כלים
ToolSearch `select:mcp__Magnific-bcaf73fa__images_retouch,mcp__Magnific-bcaf73fa__creations_wait,mcp__Magnific-bcaf73fa__creations_get,mcp__Magnific-bcaf73fa__creations_read,mcp__Magnific-bcaf73fa__creations_request_upload,mcp__Magnific-bcaf73fa__creations_finalize_upload`. רק השרת `Magnific-bcaf73fa`. folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.
תיקיית עבודה: `/tmp/claude-0/-home-user-SHOSHI-GELIS/6db3e497-d6ab-538e-b499-c27a9585efe5/scratchpad/neck3/run/<שם הקבוצה>/`. דוגמת סקריפט מסכה: `.../scratchpad/neck3/test/scripts/mask.py`.

## תהליך לכל שוט
1. **מקור:** התמונה הנוכחית שהלקוחה ראתה = הקובץ המקומי `catalog-refs/<שוט>-closeup.jpg` / `-full.jpg` (לדגמים 2, 3, 4, 8, 11, 14: `catalog-refs/earlier/<שוט>-closeup-hq.jpg` / `-full.jpg`). אם קיבלת מזהה Magnific: `creations_get`, להוריד את ה־PNG המלא עם curl, ולוודא **בעיניים** שהוא זהה לקובץ המקומי (אותו צוואר, בלי עגילים). אם אין מזהה, או שהוא לא תואם: להעלות את הקובץ המקומי כמו שהוא (JPEG, `creations_request_upload` → `curl -X PUT -H 'Content-Type: image/jpeg' --data-binary @file "<proxyUploadUrl>"` → `creations_finalize_upload`) ולעבוד עליו.
2. **מסכה:** PNG באותו גודל פיקסלים בדיוק של המקור ב־Magnific; שחור, ומצולע לבן שעוקב אחרי קצה הצוואר מכתף לכתף: מעט עור מעל הקצה, כל הפס/התפר/הביס הקיים, ועוד כ־1.5% מגובה התמונה מתחתיו (בתקריב; בגוף מלא: כ־0.6%). לא לגעת בסנטר, בפנים, ובמידת האפשר לא בשיער ולא בתחרה/עיטור חשוב. לשמור תצוגה מקדימה עם קו אדום ולהסתכל עליה לפני ההעלאה. העלאה עם `visible: false`.
3. **הרצה** עם הפרומפט מ־NECKFIX3 (להתאים צבע/בד/עיטור; לצוואר עגול את משפט העגול). להערה מיוחדת בטבלת השוטים: להוסיף משפט מתאים.
4. **בדיקה בעיניים**, חיתוך מוגדל של הצוואר מול `review/neck-refs/STANDARD_m05_small_neck.jpg`: אין פס/תפר/מסגרת/קו מקביל; שתי קשתות ושקע קטן אחד (או עגול נקי); לא גלי; אין גבול מסכה; הבד והעיטור רציפים; הפנים והשיער לא השתנו. לבדוק גם חישובית שיש שינוי בתוך המסכה ואין שינוי משמעותי הרחק ממנה.
5. נכשל: ניסיון **אחד** נוסף (מסכה מתוקנת או ניסוח מחוזק). לא יותר.

## תוצרים
- `/home/user/SHOSHI-GELIS/review/r3/neck3/<שוט>-closeup.jpg` או `-full.jpg`: התוצאה הנבחרת ב**רזולוציה מלאה**, JPEG 92 (ליצור את התיקייה אם אין; לא לדרוס).
- `/home/user/SHOSHI-GELIS/review/r3/neck3/<שוט>-closeup-cmp.jpg` / `-full-cmp.jpg`: `python3 -I /home/user/SHOSHI-GELIS/tools/compare.py out.jpg "STANDARD|/home/user/SHOSHI-GELIS/review/neck-refs/STANDARD_m05_small_neck.jpg" "BEFORE|<חיתוך צוואר לפני>" "AFTER|<חיתוך צוואר אחרי>"` (אותו חיתוך בדיוק לפני ואחרי).
- דוח: טבלה עם שוט, מזהה המקור שבו השתמשת, מזהה התוצאה הנבחרת, מספר ניסיונות, קרדיטים, פס/תפר (יש/אין), צורה (כמו הסטנדרט / חלקית / לא), גבול מסכה, וכל פגם שנשאר. בלי לייפות: אם לא יצא טוב, לכתוב שלא יצא טוב.
