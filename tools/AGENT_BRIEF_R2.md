# סבב 2 (17.11) — יצירה מחדש של כל התמונות ב־GPT 2.6

המשתמשת פסלה את כל תמונות סבב 1. קרא קודם את `tools/AGENT_BRIEF.md` (כלים, סקריפטים, תהליך, תוצרים), ואז את המסמך הזה. **במקום שיש סתירה, המסמך הזה גובר.** כתוב בעברית, אל תמחק קבצים, אל תעשה git commit/push.

## למה סבב 1 נפסל (דברי המשתמשת)
1. המותן לא מספיק צרה, אצל כולן.
2. שמלות הילדות לא נפוחות מספיק. הן צריכות להיות **נפוחות מאוד, לפחות כמו בצילומי הרפרנס**.
3. הרבה דגמים לא מדויקים מול הצילום, והדוגמניות לא זהות למקור (ללוח הדמות).
4. ההערות של שושי יושמו בלי שיקול דעת: חלקן לא יושמו וחלקן הוגזמו (למשל "פחות טול" הפך לחצאית לא נפוחה).
5. הילדה הקטנה נוצרה עם פנים לא נכונות, ולילדות תמיד אותה תסרוקת.

## הכללים החדשים
- **מודל:** `mode: "gpt-2-6"`, `resolution: "4k"`, `aspectRatio: "2:3"`, `count: 2`, `extraSettings: {"quality": "high", "thinkingLevel": "high"}`. לא Nano Banana.
- **סדר העדיפויות:** קודם כול הצילום האמיתי של השמלה (גזרה, נפח, מותן, בד, גוון, עיטור, אורך שרוול). ההערות של שושי מתקנות רק את מה שהן אומרות במפורש, ובמידה: "פחות טול" = מעט פחות, לא חצאית שטוחה. לא להמציא שינוי שלא נכתב.
- **מותן:** צרה, צמודה ומודגשת אצל כולן ("a very NARROW, snug, clearly defined waist"). נשים עדיין במידה 36–38, לא רזות מדי, אבל עם מותן מוגדרת.
- **נפח:** לילדות חצאית נפוחה מאוד על חישוק, ברוחב ובנפח **לפחות** כמו בצילום הרפרנס ("a VERY full, very wide, voluminous skirt standing out over a hoop petticoat, at least as wide and as puffy as in image N"). לנשים: רוחב החצאית כמו בצילום, לא להצר.
- **זהות:** "keep her face exactly identical to image 1". לבדוק בזום מול הלוח שהפנים, צבע השיער והגיל הנראה זהים. אם לא, לפסול.
- **ילדה קטנה — פנים חדשות (חובה):** במקום הלוח הישן `s78RGFFl8e` להשתמש בשתי תמונות המקור: `s782at2l8e` (שיער ארוך גלי עם צמות דקות בצדדים) ו־`rgditoCxtc` (אסוף לגולגול עם צמה). עותקים: `review/boards/small_original_loose_braids.jpg`, `review/boards/small_original_updo.jpg`. הפנים: אותה ילדה בדיוק (עיניים ירקרקות־אפורות, פוני, שיער חום־דבש). גיל וגוף: בת 3–4, נמוכה, פרופורציות של פעוטה.
- **תסרוקות לילדות:** מגוונות בין הדגמים, כולל אסוף, וכולל אקססוריז שמתאים לשמלה (סרט, קשת, פפיון, סיכות). התסרוקת לכל דגם נקבעה מראש בטבלה למטה, לא לשנות. **נשים:** שיער פתוח ופזור כמו בלוח, בלי אקססוריז.
- **רקע:** לבן נקי ("pure clean WHITE seamless studio background, pure white, not grey"). לבדוק במדידה שפינות התמונה מעל 248. ב־GPT 2.6 זה יוצא לבן גם עם לוח הילדה הגדולה.
- **פתח צוואר:** כמו קודם: לפי השמלה והערות שושי; לב = גבוה, צר, שקע קטן **מעוגל ורדוד**, לא מחודד ולא V.
- **תכשיטים:** בלי עגילים ושרשראות.
- **עד שני סבבי תיקון לכל שוט** (יצירה מחדש עם פרומפט מתוקן). לבחור רק תמונה שעוברת את כל הקריטריונים; אם אחרי שני סבבים אין כזו, לבחור את הטובה ביותר ולכתוב במפורש מה לא עבר.

## פרומפט שעבד בפיילוט (ילדה גדולה, דגם 7)
"Super-realistic full-body children's formal-wear catalog photograph on a pure clean WHITE seamless studio background (pure white, not grey). The 10-year-old girl from image 1: keep her face exactly identical, child proportions, not tall; [תסרוקת]. She stands straight facing the camera, arms relaxed down at her sides, gentle smile, no jewellery. She wears exactly the long festive dress photographed in image 2, reproduced faithfully in every detail: [עליון, תחרה לפי תקריב image 3, שרוול]; a very NARROW, snug, clearly defined waist; from the waist a VERY full, very wide, voluminous bell skirt standing out over a hoop petticoat, at least as wide and as puffy as in image 2, [בד, קומות, תחרה לפי image 4]; floor length, hem at the floor, shoes hidden. Neckline shaped exactly like the black dress in image 5: ... Colour, fabric and lace exactly as in the real photos; matte, not shiny. Even soft studio light, whole figure from head to hem in frame with white margin around."
לנשים אותו מבנה: "The woman from image 1: keep her face exactly identical, same hair worn loose and down ... a NARROW, snug, clearly defined waist ... a full, flowing skirt with the same generous width as in image N".

## תסרוקות לפי דגם (ילדות בלבד)
| דגם | ילדה גדולה | ילדה קטנה |
|---|---|---|
| 1 | פזור גלי ארוך עם סיכת קריסטל קטנה בצד | חצי אסוף עם שתי צמות דקות בצדדים ופפיון אפרסק קטן מאחור |
| 5 | חצי אסוף עם פפיון קטיפה שחור מאחור, גלים רכים | פזור ארוך גלי עם קשת תחרה שחורה דקה (כמו בצילום המקור) |
| 6 | תלתלים ארוכים פזורים עם קשת כסופה דקה | אסוף לגולגול גבוה עם צמה, סיכות קריסטל זעירות |
| 7 | צמה צדדית רכה אחת עם סרט לבן שזור | שתי קוקיות קטנות עם סרטים לבנים |
| 9 | חצי אסוף עם זר צמות דק סביב הראש | פזור גלי עם שתי צמות דקות בצדדים (כמו בתמונת המקור שלה) |
| 12 | קוקו גבוה מתולתל עם פפיון ורוד | אסוף לגולגול עם פפיון ורוד קטן |
| 13 | שיער אסוף נמוך אלגנטי (שיניון) עם צמה עדינה | חצי אסוף עם פפיון קטיפה שחור |

## מזהי Magnific קיימים (אין צורך להעלות שוב)
לוחות: דוגמנית 1 `s78RGEEl8e`, דוגמנית 2 `bxVO9Ie5Y2`, ילדה גדולה `DoJuqZRpcl`, ילדה קטנה `s782at2l8e` + `rgditoCxtc`. צוואר לב: נשים `9ZFVelCNYZ`, ילדות `VXwCF2JMMU`.
העותקים המקומיים של הרפרנסים מסבב 1 נמצאים ב־`<scratchpad>/mXX/` (לפתוח ולראות אותם בעיניים לפני השימוש). תיקיית העבודה לסבב 2: `<scratchpad>/r2/mXX/`.

- **דגם 1:** women_real `LwoRnmaswO`, lace1_center `8a6ksAmIrU`, lace2_side `0eSfHP1TfW`, lace3_scattered `p8OFkRaehw`, big_long_flowers `VXwEbilMMU`, big_long_plain `Ifi1lcetvE`, kid_top `79aYM1iJAL`, kid_short `TdUCqR0VNR`, belt `LwoRnqOswO`, toddler `gOtAckNSXO`.
- **דגם 5:** front `UPhzvJ0wny`, side `gOtAm7MSXO`, sleeve `6Aqpb25iJO`, skirtlace `xSXiBSFjfW`, lace_pattern_m12 `ovNK6ff829`.
- **דגם 6:** w_chiffon_full `p8OFPrJehw`, w_chiffon_bodice `lJI2mTkgv9`, w_chiffon_b `SymGvDgUb8`, w_sparkle_full `s78ZtM9l8e`, w_sparkle_top `MB7uOLkDCm`, w_sparkle_b `UPhzaBKwny`, g_front `9ZFMqfPNYZ`, g_full `3z5dkFUREY`, g_neck `KLD4eVMkqp`, g_big `TdUC7SxVNR`, g_tiers `P3uTFua42C`, g_sleeve `ovNKi6N829`, g_applique `8a6k33GIrU`.
- **דגם 7:** women_full `O6CcuhWynm`, women_skirt `dtPq9JxXSL`, women_bodice_closeup `JNfWEvvOq4`, women_lace_closeup `JNfWEaaOq4`, v1_mirror `LwoRIoYswO`, v1_lace_skirt `jUB38oXLD0`, v1_shoulder `79aYCCFJAL`, girl_big_full `jUB38IoLD0`, girl_bodice_lace_closeup `JNfWEQQOq4`, girl_skirt_lace_closeup `LwoRIhaswO`, girls_small_three `LwoRIvfswO`, girl_small_side `jUB38vmLD0`.
- **דגם 9:** w_skirt_fall `SymGhlIUb8`, w_neck_shoulder `Bh95NXUoQR`, w_princess_bodice `5jMPD5aKxe`, w_flowers_closeup `ksp9dra16B`, w_skirt_lower `ksp9aQW16B`, w_bodice_upper `79aYkskJAL`, g_full_dress `cpgaUVg0eP`, g_top `yiE0QNDPW9`, g_neck `UPhzayTwny`, g_hem_flowers `9ZFMqZfNYZ`.
- **דגם 10:** dress_full `nVLmL2lYQD`, neck_closeup `Bh959eSoQR`, wave_fabric `0eSfScxTfW`.
- **דגם 12:** w_stripes_full `KLD4eGzkqp`, w_stripes_skirt `tC3rZJTmZJ`, w_sleeve_stripe `fHGlnNhCDY`, w_neck `Ifi1RystvE`, w_princess_waistband `s78Zteml8e`, w_tiers_skirt `yiE0QvLPW9`, g_long_dress `Ifi1RNUtvE`, g_older_long `MB7uOwsDCm`, g_bodice_roundneck `xSXioX2jfW`, g_sleeve_cuff `w4vnfam7EI`, g_lace_closeup `aFAszzXfSh`, g_short_dress `79aYCEHJAL`.
- **דגם 13:** src_puff_girl `DoJQOmnpcl`, src_tight_girl `huZj2bDvqL`, src_puff_side `eIyHPCXdqL`, sleeve_puff `p8OFyCrehw`, skirt_1tier `0eSfUh9TfW`, sleeve_tight `Ifi13kutvE`, src_big_9494 `JNfWCWcOq4`, src_big_9530 `vQ2LAs4a47`, src_small_9550 `jUB3oZWLD0`, sleeve_big `p8OFybSehw`, sleeve_small `aFAsG7AfSh`, skirt_2tier `yiE0udbPW9`.

אם רפרנס חסר או לא מספיק ברור, מותר להוריד שוב מהדרייב ולהעלות חיתוך חדש.

## תוצרים (שמות קבצים חדשים, לא לדרוס את סבב 1)
- השוואה לכל שוט: `/home/user/SHOSHI-GELIS/review/r2/mXX-<shot>.jpg` (SOURCE + PICK, ואם יש ALT קרובה גם היא), עם `compare.py`.
- הנבחרת בגובה 2400px: `/home/user/SHOSHI-GELIS/review/r2/final/mXX-<shot>.jpg`.
- שמות השוטים: `d1`, `d2`, `big`, `small` (בדגם 1 גם `d1-v3`, `big-flowers`, `big-plain`).
- דוח סופי קצר: לכל שוט קישור `https://www.magnific.com/app/creation/<identifier>`, מספר סבבים, ושורה אחת לכל קריטריון שלא עבר במלואו. בסוף: האם לדעתך התמונה עומדת **בכל** הכללים (כן/לא) לכל שוט. בלי לייפות: המשתמשת ביקשה לקבל לאישור רק תמונות מדויקות לגמרי.

## תוספת (17.11): עור הפנים — בלי הכתמים של GPT
המשתמשת מוטרדת מ"הכתמים הידועים של GPT" על הפנים. בפיילוט הם הופיעו אצל הילדה הגדולה: סומק אדמדם־כתום לא אחיד על הלחיים והמצח ונמשים מודגשים.
- להוסיף לכל פרומפט: "Skin: clear, even, natural fair skin tone exactly like image 1; no red or orange blotches, no uneven flush, no mottled patches, no added freckles, no orange or yellow colour cast on the face; soft natural studio skin."
- קריטריון חובה נוסף: חיתוך הפנים ברזולוציה מלאה (בערך `0.36 0.01 0.64 0.20` ב־crop.py) והשוואה ללוח הדמות. תמונה עם כתמים, סומק לא אחיד או גוון כתום על הפנים נפסלת, גם אם השמלה מושלמת.
- בדוח: לכתוב לכל שוט אם הפנים נקיות מכתמים (כן/לא).
