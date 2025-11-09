@echo off
echo Creating FAST Dr. Gideon video - Simple crossfades, ALL 8 images...
echo.

set FFMPEG="C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

REM FAST VERSION - No zoompan (too slow!), just crossfade transitions
REM Each image shows for 20.61 seconds with 0.5 second crossfade
REM Total: 164.88 seconds to match narration

%FFMPEG% -y ^
-loop 1 -t 20.61 -i 1.png ^
-loop 1 -t 20.61 -i 2.png ^
-loop 1 -t 20.61 -i 3.png ^
-loop 1 -t 20.61 -i 4.png ^
-loop 1 -t 20.61 -i 5.png ^
-loop 1 -t 20.61 -i 6.png ^
-loop 1 -t 20.61 -i 7.png ^
-loop 1 -t 20.61 -i 8.png ^
-filter_complex ^
"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v0]; ^
[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v1]; ^
[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v2]; ^
[3:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v3]; ^
[4:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v4]; ^
[5:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v5]; ^
[6:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v6]; ^
[7:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24[v7]; ^
[v0][v1]xfade=transition=fade:duration=0.5:offset=20.11[vf01]; ^
[vf01][v2]xfade=transition=fade:duration=0.5:offset=40.22[vf02]; ^
[vf02][v3]xfade=transition=fade:duration=0.5:offset=60.33[vf03]; ^
[vf03][v4]xfade=transition=fade:duration=0.5:offset=80.44[vf04]; ^
[vf04][v5]xfade=transition=fade:duration=0.5:offset=100.55[vf05]; ^
[vf05][v6]xfade=transition=fade:duration=0.5:offset=120.66[vf06]; ^
[vf06][v7]xfade=transition=fade:duration=0.5:offset=140.77[vf07]" ^
-i "Dr. Gideon Second Video.wav" ^
-stream_loop -1 -i "Instrumentals.mp3" ^
-filter_complex "[9:a]volume=0.1[music];[8:a][music]amix=inputs=2:duration=shortest[audio]" ^
-map "[vf07]" -map "[audio]" ^
-c:v libx264 -preset ultrafast -b:v 600k -maxrate 800k -bufsize 1600k ^
-pix_fmt yuv420p -c:a aac -b:a 128k ^
-shortest Dr_Gideon_FAST_SIMPLE.mp4

echo.
echo ========================================
echo DONE! Video created: Dr_Gideon_FAST_SIMPLE.mp4
echo.
echo All 8 images included with smooth crossfades:
echo   1.png (20.61s - opening)
echo   2.png (20.61s)
echo   3.png (20.61s)
echo   4.png (20.61s)
echo   5.png (20.61s)
echo   6.png (20.61s)
echo   7.png (20.61s)
echo   8.png (20.61s - closing)
echo.
echo Total duration: 2:44 (164.88 seconds)
echo ========================================
echo.
pause
