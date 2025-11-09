@echo off
echo Creating video quickly...

REM Simple Ken Burns video with smooth transitions
ffmpeg -framerate 1/10 -pattern_type glob -i "*.png" ^
-i "Dr. Gideon Second Video.wav" ^
-stream_loop -1 -i "Instrumentals.mp3" ^
-filter_complex ^
"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.5)':d=250:s=1920x1080:fps=30[v]; ^
[2:a]volume=0.1[music]; ^
[1:a][music]amix=inputs=2:duration=shortest[audio]" ^
-map "[v]" -map "[audio]" ^
-c:v libx264 -preset ultrafast -crf 23 -pix_fmt yuv420p ^
-c:a aac -b:a 192k ^
-shortest ^
"Dr_Gideon_Video.mp4" -y

echo Done!
pause
