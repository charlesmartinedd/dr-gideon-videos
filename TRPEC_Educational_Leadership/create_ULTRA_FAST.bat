@echo off
echo Creating ULTRA FAST Dr. Gideon video - ALL 8 images included!
echo.

set FFMPEG="C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

REM ULTRA FAST VERSION - Simple crossfades, no zoompan
REM Combined filter_complex for both video and audio

%FFMPEG% -y ^
-loop 1 -t 20.61 -i 1.png ^
-loop 1 -t 20.61 -i 2.png ^
-loop 1 -t 20.61 -i 3.png ^
-loop 1 -t 20.61 -i 4.png ^
-loop 1 -t 20.61 -i 5.png ^
-loop 1 -t 20.61 -i 6.png ^
-loop 1 -t 20.61 -i 7.png ^
-loop 1 -t 20.61 -i 8.png ^
-i "Dr. Gideon Second Video.wav" ^
-stream_loop -1 -i "Instrumentals.mp3" ^
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
[vf06][v7]xfade=transition=fade:duration=0.5:offset=140.77[vf07]; ^
[9:a]volume=0.1[music]; ^
[8:a][music]amix=inputs=2:duration=shortest[audio]" ^
-map "[vf07]" -map "[audio]" ^
-c:v libx264 -preset ultrafast -b:v 600k -maxrate 800k -bufsize 1600k ^
-pix_fmt yuv420p -c:a aac -b:a 128k ^
-shortest Dr_Gideon_ULTRA_FAST.mp4

echo.
echo ========================================
echo DONE! Video created: Dr_Gideon_ULTRA_FAST.mp4
echo.
echo All 8 images included (20.61s each):
echo   1.png, 2.png, 3.png, 4.png
echo   5.png, 6.png, 7.png, 8.png
echo.
echo Features:
echo   - Smooth crossfade transitions
echo   - Narration + 10%% background music
echo   - Full HD 1920x1080 @ 24fps
echo   - Duration: 2:44 (164.88 seconds)
echo ========================================
echo.
pause
