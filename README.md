# subtitle-flip-punctuation-rtl
Flips punctuation for RTL languages (tested only with Hebrew). To be used on programs/TVs that do not render regular subtitles correctly.

Use: python flip_subs.py \<input file path\> \<output file path\>

This script should deal with double brackets, blocks such as "\<i\>" and "\<b\>", and ignore non subtitle lines in the srt file.

Note: I use 'latin-1' instead of 'utf-8' because python seems to have some problems with certain characters, and since the actual script doesn't care which encoding is used.

<b>Utilty (for windows 7 and above):</b>

Create a script file with the following content:

```batch
@echo off
cls
<python exe path> <script path> %1 %1
```

Name the file "Flip Punctuation.cmd"

Place the file in `C:\Users\<user name>\AppData\Roaming\Microsoft\Windows\SendTo`

Now when right clicking a subtitle file, in the "Send To" menu, the new script should appear. Using it will run the script in place on the selected file.
  

<b>Example:</b>

Input:
```
1
00:00:07,100 --> 00:00:09,510
<i>בעונה הקודמת של
מסע בין כוכבים: "דיסקברי</i>"

2
00:00:09,770 --> 00:00:13,030
<i>,שבע-מאות שנים אחרי עזיבתנו
אזל מלאי הדיליתיום</i>.

3
00:00:13,210 --> 00:00:15,600
<i>הפדרציה ניסתה תכנונים חלופיים
להינע על-חלל</i>,

10
00:00:29,700 --> 00:00:31,860
כאן החלה "השריפה."

11
00:00:32,050 --> 00:00:35,300
אני מקבלת קריאה של פיזור דיליתיום
על פני הכוכב כולו.

12
00:00:35,780 --> 00:00:38,270
הפדרציה תשמח לקבל
חדשות כאלה עכשיו.

62
00:03:41,890 --> 00:03:43,490
"בלי תנאים מוקדמים."

651
00:39:09,785 --> 00:39:11,668
%מחזיקים מעמד ב-25.

653
00:39:12,951 --> 00:39:15,170
טוב, נו, אל תחגגי:
```

Output:
```
1
00:00:07,100 --> 00:00:09,510
<i>בעונה הקודמת של
"מסע בין כוכבים: "דיסקברי</i>

2
00:00:09,770 --> 00:00:13,030
<i>,שבע-מאות שנים אחרי עזיבתנו
.אזל מלאי הדיליתיום</i>

3
00:00:13,210 --> 00:00:15,600
<i>הפדרציה ניסתה תכנונים חלופיים
,להינע על-חלל</i>

10
00:00:29,700 --> 00:00:31,860
".כאן החלה "השריפה

11
00:00:32,050 --> 00:00:35,300
אני מקבלת קריאה של פיזור דיליתיום
.על פני הכוכב כולו

12
00:00:35,780 --> 00:00:38,270
הפדרציה תשמח לקבל
.חדשות כאלה עכשיו

62
00:03:41,890 --> 00:03:43,490
".בלי תנאים מוקדמים"

651
00:39:09,785 --> 00:39:11,668
.%מחזיקים מעמד ב-25

653
00:39:12,951 --> 00:39:15,170
:טוב, נו, אל תחגגי  
```
  
