# פתח צוואר, סטנדרט סופי (אחרי משוב שושי) — הנחיות לסוכן

שושי (הלקוחה) והמשתמשת קבעו: **הסטנדרט לפתח הצוואר הוא דגם 5 ילדה קטנה**: `/home/user/SHOSHI-GELIS/review/neck-refs/STANDARD_m05_small_neck.jpg` (וגם `STANDARD_m01_big_plain_neck.jpg`). לפתוח ולהסתכל היטב. מה שיש שם:
- **קצה נקי**: הבד עצמו נגמר בקו חלק. **אין** פס שפה, **אין** ביס/פייפינג, **אין** תפר נראה, **אין** רצועת בד נוספת, אין קו מקביל לקצה. זה הדבר הכי חשוב: שושי פסלה כ־30 תמונות על "מסגרת / תפר / תוספת בד".
- גבוה וצמוד לבסיס הצוואר, ברוחב הצוואר בלבד.
- שתי קשתות רכות (קמורות) שנפגשות ב**שקע אחד קטן**, עם חוד קטן ועדין. לא V גדול/עמוק/רחב, לא קו גלי עם כמה קשתות, לא עגול לגמרי (אלא אם השמלה עגולה).
- לשמלה עם **צוואר עגול** (דגם 3, דגם 7 נערה ראשונה): הצורה נשארת עגולה; רק להסיר את התפר/הפס כך שהקצה ייראה "חתיכה אחת של הבד".

הכלי: `mcp__Magnific-bcaf73fa__images_retouch`, `mode: "replace"`, `editType: "precise"`, מסכה לבנה על קצה הצוואר בלבד (בנייה והעלאה כמו ב־`/home/user/SHOSHI-GELIS/tools/AGENT_BRIEF_NECKFIX2.md`). המסכה צריכה לכסות את כל הפס/התפר הקיים (עד כ־1.5% מגובה התמונה מתחתיו) ומעט עור מעל.

פרומפט בסיס (להתאים סוגריים; **לא** לכתוב "sewn edge", "finished edge", "binding", "trim" בחיוב):
"The top of the [girl's/woman's] [צבע ובד] dress at the base of her neck. The fabric simply ends in a clean, smooth, plain cut edge: NO binding, NO piping, NO band, NO facing strip, NO topstitching, NO visible seam line, no second line parallel to the edge, no border of any kind — just the same [בד] continuing unchanged right up to the edge, as one single piece of fabric. Shape of the edge: high and close to the base of the neck, only as wide as the neck, two soft rounded curves that meet in one small, shallow notch in the centre with a tiny gentle point (a small modest sweetheart). Not a big V, not deep, not wide, not wavy or scalloped. [העיטור] continues below exactly as around it. Natural skin above."
לצוואר עגול: להחליף את משפט הצורה ב־"Shape of the edge: a plain smooth round neckline, high at the base of the neck."

בדיקה בעיניים, בהגדלה, מול `STANDARD_m05_small_neck.jpg`: (1) אין שום פס/תפר/מסגרת; (2) הצורה כמו בסטנדרט; (3) אין גבול מסכה, הבד והעיטור רציפים; (4) מחוץ למסכה לא השתנה דבר. כתוב בעברית, אל תמחק ואל תדרוס קבצים, אל תעשה git commit/push. folderReference: `736649c7-48c2-4480-9981-4f3a060a7870`.
