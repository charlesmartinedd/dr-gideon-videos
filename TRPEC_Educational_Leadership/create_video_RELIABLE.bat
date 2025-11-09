@echo off
echo Creating Dr. Gideon video with RELIABLE method...
echo This creates each segment separately then joins them.
echo.

set FFMPEG="C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe"

echo Step 1: Creating 8 individual video segments with Ken Burns...

REM Image 1 - STATIC (no animation)
%FFMPEG% -y -loop 1 -t 20.61 -i 1.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment1.mp4
echo   Segment 1/8 done (1.png - STATIC opening)

REM Image 2 - Zoom OUT
%FFMPEG% -y -loop 1 -t 20.61 -i 2.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment2.mp4
echo   Segment 2/8 done (2.png - zoom out)

REM Image 3 - Zoom IN
%FFMPEG% -y -loop 1 -t 20.61 -i 3.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment3.mp4
echo   Segment 3/8 done (3.png - zoom in)

REM Image 4 - Zoom OUT
%FFMPEG% -y -loop 1 -t 20.61 -i 4.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment4.mp4
echo   Segment 4/8 done (4.png - zoom out)

REM Image 5 - Zoom IN
%FFMPEG% -y -loop 1 -t 20.61 -i 5.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment5.mp4
echo   Segment 5/8 done (5.png - zoom in)

REM Image 6 - Zoom OUT
%FFMPEG% -y -loop 1 -t 20.61 -i 6.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='if(lte(zoom,1.0),1.2,max(1.0,zoom-0.0015))':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment6.mp4
echo   Segment 6/8 done (6.png - zoom out)

REM Image 7 - Zoom IN
%FFMPEG% -y -loop 1 -t 20.61 -i 7.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,zoompan=z='min(zoom+0.0015,1.2)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=495:s=1920x1080:fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment7.mp4
echo   Segment 7/8 done (7.png - zoom in)

REM Image 8 - STATIC (no animation)
%FFMPEG% -y -loop 1 -t 20.61 -i 8.png -vf "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=24" -c:v libx264 -preset ultrafast -crf 18 -pix_fmt yuv420p segment8.mp4
echo   Segment 8/8 done (8.png - STATIC closing)

echo.
echo Step 2: Creating concat list file...
(
echo file 'segment1.mp4'
echo file 'segment2.mp4'
echo file 'segment3.mp4'
echo file 'segment4.mp4'
echo file 'segment5.mp4'
echo file 'segment6.mp4'
echo file 'segment7.mp4'
echo file 'segment8.mp4'
) > segments_list.txt

echo.
echo Step 3: Joining all 8 segments...
%FFMPEG% -y -f concat -safe 0 -i segments_list.txt -c copy video_only.mp4

echo.
echo Step 4: Adding audio (narration + background music)...
%FFMPEG% -y -i video_only.mp4 -i "Dr. Gideon Second Video.wav" -stream_loop -1 -i "Instrumentals.mp3" -filter_complex "[2:a]volume=0.1[music];[1:a][music]amix=inputs=2:duration=shortest[audio]" -map 0:v -map "[audio]" -c:v copy -c:a aac -b:a 128k -shortest Dr_Gideon_ALL_IMAGES.mp4

echo.
echo Step 5: Cleaning up temporary files...
del segment1.mp4 segment2.mp4 segment3.mp4 segment4.mp4 segment5.mp4 segment6.mp4 segment7.mp4 segment8.mp4 video_only.mp4 segments_list.txt

echo.
echo ========================================
echo DONE! Video created: Dr_Gideon_ALL_IMAGES.mp4
echo.
echo All 8 images included:
echo   1.png (20.61s - STATIC opening)
echo   2.png (20.61s - zoom out)
echo   3.png (20.61s - zoom in)
echo   4.png (20.61s - zoom out)
echo   5.png (20.61s - zoom in)
echo   6.png (20.61s - zoom out)
echo   7.png (20.61s - zoom in)
echo   8.png (20.61s - STATIC closing)
echo ========================================
echo.
pause
