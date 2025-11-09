@echo off
echo Creating Dr. Gideon video with Ken Burns effects...

REM Set paths
set FFMPEG=ffmpeg
set NARRATION=Dr. Gideon Second Video.wav
set MUSIC=Instrumentals.mp3
set OUTPUT=Dr_Gideon_Final_Video.mp4

REM Create video from images with Ken Burns effect and crossfade transitions
%FFMPEG% -loop 1 -t 10 -i 1.png ^
-loop 1 -t 10 -i 2.png ^
-loop 1 -t 10 -i 3.png ^
-loop 1 -t 10 -i 4.png ^
-loop 1 -t 10 -i 5.png ^
-loop 1 -t 10 -i 6.png ^
-loop 1 -t 10 -i 7.png ^
-loop 1 -t 10 -i 8.png ^
-filter_complex ^
"[0:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.5)':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v0]; ^
[1:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v1]; ^
[2:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.5)':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v2]; ^
[3:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v3]; ^
[4:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.5)':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v4]; ^
[5:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v5]; ^
[6:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.5)':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v6]; ^
[7:v]scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d=250:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080,fade=t=in:st=0:d=0.5,fade=t=out:st=9.5:d=0.5[v7]; ^
[v0][v1]xfade=transition=fade:duration=1:offset=9[vf01]; ^
[vf01][v2]xfade=transition=fade:duration=1:offset=18[vf02]; ^
[vf02][v3]xfade=transition=fade:duration=1:offset=27[vf03]; ^
[vf03][v4]xfade=transition=fade:duration=1:offset=36[vf04]; ^
[vf04][v5]xfade=transition=fade:duration=1:offset=45[vf05]; ^
[vf05][v6]xfade=transition=fade:duration=1:offset=54[vf06]; ^
[vf06][v7]xfade=transition=fade:duration=1:offset=63[vf07]" ^
-i "%NARRATION%" ^
-stream_loop -1 -i "%MUSIC%" ^
-filter_complex "[3:a]volume=0.1[music];[2:a][music]amix=inputs=2:duration=first[audio]" ^
-map "[vf07]" -map "[audio]" ^
-c:v libx264 -preset fast -crf 23 -pix_fmt yuv420p ^
-c:a aac -b:a 192k ^
-movflags +faststart ^
-shortest ^
"%OUTPUT%" -y

echo.
echo Done! Video saved as: %OUTPUT%
echo.
pause
