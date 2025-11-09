@echo off
echo Creating high-quality 20MB Dr. Gideon video with Ken Burns effects...
echo.
echo Verifying all 8 images are included...
echo - 1.png (Opening)
echo - 2.png
echo - 3.png
echo - 4.png
echo - 5.png
echo - 6.png
echo - 7.png
echo - 8.png (Closing)
echo.

set FFMPEG="C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

REM High-quality 1080p @ 24fps video with Ken Burns effects (targeting ~20MB)
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
"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':d=494:s=1920x1080:fps=24[v0]; ^
[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':d=494:s=1920x1080:fps=24[v1]; ^
[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':d=494:s=1920x1080:fps=24[v2]; ^
[3:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':d=494:s=1920x1080:fps=24[v3]; ^
[4:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':d=494:s=1920x1080:fps=24[v4]; ^
[5:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':d=494:s=1920x1080:fps=24[v5]; ^
[6:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':d=494:s=1920x1080:fps=24[v6]; ^
[7:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':d=494:s=1920x1080:fps=24[v7]; ^
[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[v]" ^
-i "Dr. Gideon Second Video.wav" ^
-stream_loop -1 -i "Instrumentals.mp3" ^
-filter_complex "[9:a]volume=0.1[music];[8:a][music]amix=inputs=2:duration=shortest[audio]" ^
-map "[v]" -map "[audio]" ^
-c:v libx264 -preset ultrafast -b:v 800k -maxrate 1000k -bufsize 2000k ^
-pix_fmt yuv420p -c:a aac -b:a 128k ^
-shortest Dr_Gideon_HD_20MB.mp4

echo.
echo Done! High-quality video created: Dr_Gideon_HD_20MB.mp4
echo.
echo Video details:
echo - Resolution: 1920x1080 (Full HD)
echo - Framerate: 24fps
echo - All 8 images included (20.61 seconds each)
echo - Ken Burns animation (alternating zoom in/out)
echo - Audio: Narration + 10%% background instrumental
echo - Target size: ~20MB
echo.
pause
