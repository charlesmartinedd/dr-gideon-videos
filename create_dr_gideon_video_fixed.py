"""
Fixed version - Creates individual video segments then concatenates them
This avoids the complex filter issues that caused image looping
"""

import subprocess
from pathlib import Path
import os

PROJECT_DIR = Path(__file__).parent
AUDIO_FILE = PROJECT_DIR.parent / "Dr_Gideon_Audio_Cleaned.mp3"
OUTPUT_FILE = PROJECT_DIR / "Dr_Gideon_Video_FIXED.mp4"
FFMPEG_PATH = Path(r"C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe")
TEMP_DIR = PROJECT_DIR / "temp_segments"

# Timeline - exact same as before
timeline = [
    ("1_Opening.png", 0.0, 11.0, None),
    ("2_Leadership.png", 11.0, 13.0, "zoom_in"),
    ("4_Challenges.png", 24.0, 15.0, "pan_right"),
    ("6_Impact.png", 39.0, 21.0, "zoom_out"),
    ("7_Four_Sessions.png", 60.0, 2.0, None),
    ("12_Session1_Demystifying_AI.png", 62.0, 16.0, "zoom_in"),
    ("7_Four_Sessions.png", 78.0, 2.0, None),
    ("13_Session2_Executive_Assistant.png", 80.0, 8.0, "pan_left"),
    ("7_Four_Sessions.png", 88.0, 2.0, None),
    ("14_Session3_Data_Driven.png", 90.0, 11.0, "zoom_out"),
    ("7_Four_Sessions.png", 101.0, 2.0, None),
    ("15_Session4_Career_Advancement.png", 103.0, 10.0, "zoom_in"),
    ("11_Closing.png", 113.0, 5.0, None),
]

def create_ken_burns(effect_type, duration):
    """Create FFmpeg filter for Ken Burns effect"""
    if effect_type is None:
        return "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,setsar=1"

    fps = 30
    frames = int(duration * fps)

    effects = {
        "zoom_in": f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,zoompan=z='min(zoom+0.0015,1.5)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "zoom_out": f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "pan_right": f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,zoompan=z='1.3':d={frames}:x='min(iw/zoom*(on/{frames}),iw/zoom)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "pan_left": f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black,zoompan=z='1.3':d={frames}:x='iw/zoom-iw/zoom*(on/{frames})':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
    }
    return effects.get(effect_type, effects["zoom_in"])

def create_video_segment(image_file, duration, effect, segment_num):
    """Create individual video segment"""
    image_path = PROJECT_DIR / image_file
    segment_path = TEMP_DIR / f"segment_{segment_num:03d}.mp4"

    filter_str = create_ken_burns(effect, duration)

    cmd = [
        str(FFMPEG_PATH), "-y",
        "-loop", "1",
        "-i", str(image_path),
        "-vf", filter_str,
        "-t", str(duration),
        "-c:v", "libx264",
        "-preset", "ultrafast",
        "-pix_fmt", "yuv420p",
        "-r", "30",
        str(segment_path)
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return segment_path

def create_video():
    """Create video by building segments then concatenating"""

    print("=" * 80)
    print("FIXED RENDER - Dr. Gideon Video")
    print("=" * 80)

    # Create temp directory
    TEMP_DIR.mkdir(exist_ok=True)

    # Step 1: Create all video segments
    print("\nStep 1: Creating individual segments...")
    segment_files = []

    for i, (image_file, _, duration, effect) in enumerate(timeline):
        image_path = PROJECT_DIR / image_file
        if not image_path.exists():
            print(f"ERROR: Missing {image_path}")
            return False

        print(f"  [{i+1}/{len(timeline)}] {image_file} ({duration}s, {effect or 'static'})")
        segment_path = create_video_segment(image_file, duration, effect, i)
        segment_files.append(segment_path)

    # Step 2: Create concat file
    print("\nStep 2: Creating concat list...")
    concat_file = TEMP_DIR / "concat_list.txt"
    with open(concat_file, 'w') as f:
        for segment in segment_files:
            f.write(f"file '{segment}'\n")

    # Step 3: Concatenate all segments
    print("\nStep 3: Concatenating segments...")
    temp_video = TEMP_DIR / "video_no_audio.mp4"

    cmd = [
        str(FFMPEG_PATH), "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(temp_video)
    ]

    subprocess.run(cmd, check=True, capture_output=True)

    # Step 4: Add audio
    print("\nStep 4: Adding audio...")

    cmd = [
        str(FFMPEG_PATH), "-y",
        "-i", str(temp_video),
        "-i", str(AUDIO_FILE),
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "128k",
        "-shortest",
        str(OUTPUT_FILE)
    ]

    subprocess.run(cmd, check=True, capture_output=True)

    # Cleanup
    print("\nStep 5: Cleaning up temp files...")
    for segment in segment_files:
        segment.unlink()
    concat_file.unlink()
    temp_video.unlink()
    TEMP_DIR.rmdir()

    print("\n" + "=" * 80)
    print(f"SUCCESS: {OUTPUT_FILE}")
    print("=" * 80)
    return True

if __name__ == "__main__":
    if not AUDIO_FILE.exists():
        print(f"ERROR: Audio not found: {AUDIO_FILE}")
    else:
        create_video()
