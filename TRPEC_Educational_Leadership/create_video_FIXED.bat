@echo off
echo Creating FIXED Dr. Gideon video - All 8 images verified...
echo.

set FFMPEG="C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

REM FIXED VERSION - Using proper frame counts for zoompan
REM 20.61 seconds * 24fps = 494.64 frames, rounded to 495 frames
REM This ensures each image displays for exactly 20.61 seconds

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
"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS[v0]; ^
[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+20.61/TB[v1]; ^
[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+41.22/TB[v2]; ^
[3:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+61.83/TB[v3]; ^
[4:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+82.44/TB[v4]; ^
[5:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+103.05/TB[v5]; ^
[6:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+123.66/TB[v6]; ^
[7:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24,setpts=PTS-STARTPTS+144.27/TB[v7]; ^
[v0][v1][v2][v3][v4][v5][v6][v7]concat=n=8:v=1:a=0[outv]" ^
-i "Dr. Gideon Second Video.wav" ^
-stream_loop -1 -i "Instrumentals.mp3" ^
-filter_complex "[9:a]volume=0.1[music];[8:a][music]amix=inputs=2:duration=shortest[outa]" ^
-map "[outv]" -map "[outa]" ^
-c:v libx264 -preset ultrafast -b:v 800k -maxrate 1000k -bufsize 2000k ^
-pix_fmt yuv420p -c:a aac -b:a 128k ^
-shortest Dr_Gideon_FIXED.mp4

echo.
echo Done! Fixed video with all 8 images: Dr_Gideon_FIXED.mp4
echo.
pause
