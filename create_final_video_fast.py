"""
Final video - FAST LIGHTWEIGHT version
- 4 seconds for each Four Sessions appearance
- Shortened session images
- 3 seconds closing with silence
- Ultra-fast encoding
"""

import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
AUDIO_FILE = Path(r"C:\Users\MarieLexisDad\Downloads\Dr. Gideon First Video Updated.wav")
OUTPUT_FILE = PROJECT_DIR / "Dr_Gideon_Final_Video.mp4"
FFMPEG_PATH = Path(r"C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe")
TEMP_DIR = PROJECT_DIR / "temp_segments"

# Updated timeline with corrections
timeline = [
    ("1_Opening.png", 0.0, 11.0, None),
    ("2_Leadership.png", 11.0, 13.0, "zoom_in"),
    ("4_Challenges.png", 24.0, 15.0, "pan_right"),
    ("6_Impact.png", 39.0, 21.0, "zoom_out"),
    ("7_Four_Sessions.png", 60.0, 4.0, None),  # 4 seconds (was 2)
    ("12_Session1_Demystifying_AI.png", 64.0, 14.0, "zoom_in"),  # 14s (was 16)
    ("7_Four_Sessions.png", 78.0, 4.0, None),  # 4 seconds (was 2)
    ("13_Session2_Executive_Assistant.png", 82.0, 6.0, "pan_left"),  # 6s (was 8)
    ("7_Four_Sessions.png", 88.0, 4.0, None),  # 4 seconds (was 2)
    ("14_Session3_Data_Driven.png", 92.0, 9.0, "zoom_out"),  # 9s (was 11)
    ("7_Four_Sessions.png", 101.0, 4.0, None),  # 4 seconds (was 2)
    ("15_Session4_Career_Advancement.png", 105.0, 8.0, "zoom_in"),  # 8s (was 10)
    ("11_Closing.png", 113.0, 3.0, None),  # 3s with silence
]

def create_ken_burns(effect_type, duration):
    """Smooth Ken Burns with full-screen crop"""
    if effect_type is None:
        return "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,setsar=1"

    fps = 30
    frames = int(duration * fps)
    base_scale = "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080"

    effects = {
        "zoom_in": f"{base_scale},zoompan=z='min(zoom+0.001,2.0)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "zoom_out": f"{base_scale},zoompan=z='if(lte(zoom,1.0),2.0,max(1.0,zoom-0.001))':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "pan_right": f"{base_scale},zoompan=z='1.5':d={frames}:x='min(iw/zoom*(on/{frames}),iw/zoom)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
        "pan_left": f"{base_scale},zoompan=z='1.5':d={frames}:x='iw/zoom-iw/zoom*(on/{frames})':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps},setsar=1",
    }
    return effects.get(effect_type, effects["zoom_in"])

def create_video_segment(image_file, duration, effect, segment_num):
    """Create segment with fast encoding"""
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
        "-preset", "ultrafast",  # FAST
        "-crf", "23",  # BALANCED
        "-pix_fmt", "yuv420p",
        "-r", "30",
        str(segment_path)
    ]

    subprocess.run(cmd, check=True, capture_output=True)
    return segment_path

def create_video():
    """Create final video - fast render"""

    print("=" * 80)
    print("FINAL VIDEO - Fast Lightweight Render")
    print("=" * 80)

    TEMP_DIR.mkdir(exist_ok=True)

    if not AUDIO_FILE.exists():
        print(f"ERROR: Audio not found: {AUDIO_FILE}")
        return False

    # Step 1: Create segments
    print("\nStep 1: Creating 13 segments...")
    segment_files = []

    for i, (image_file, _, duration, effect) in enumerate(timeline):
        image_path = PROJECT_DIR / image_file
        if not image_path.exists():
            print(f"ERROR: Missing {image_path}")
            return False

        effect_label = effect or "static"
        print(f"  [{i+1}/13] {image_file} ({duration}s, {effect_label})")
        segment_path = create_video_segment(image_file, duration, effect, i)
        segment_files.append(segment_path)

    # Step 2: Concat list
    print("\nStep 2: Creating concat list...")
    concat_file = TEMP_DIR / "concat_list.txt"
    with open(concat_file, 'w') as f:
        for segment in segment_files:
            f.write(f"file '{segment}'\n")

    # Step 3: Concatenate
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

    # Step 4: Add audio + 3 seconds silence
    print("\nStep 4: Adding audio with 3s silence at end...")

    # Create silent audio for last 3 seconds
    cmd = [
        str(FFMPEG_PATH), "-y",
        "-i", str(temp_video),
        "-i", str(AUDIO_FILE),
        "-filter_complex", "[1:a]apad=pad_dur=3[a]",  # Add 3s silence to audio
        "-map", "0:v",
        "-map", "[a]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-b:a", "128k",
        "-shortest",
        str(OUTPUT_FILE)
    ]

    subprocess.run(cmd, check=True, capture_output=True)

    # Cleanup
    print("\nStep 5: Cleaning up...")
    for segment in segment_files:
        segment.unlink()
    concat_file.unlink()
    temp_video.unlink()
    TEMP_DIR.rmdir()

    print("\n" + "=" * 80)
    print(f"SUCCESS: {OUTPUT_FILE}")
    print("=" * 80)
    print("\nFinal Settings:")
    print("  - Four Sessions: 4 seconds each (4 appearances)")
    print("  - Session images shortened by 2s each")
    print("  - Closing slide: 3 seconds with silence")
    print("  - Total duration: 1:56 (113s video + 3s silence)")
    print("  - Full-screen crop (no black borders)")
    print("  - Smooth Ken Burns effects")
    print("=" * 80)
    return True

if __name__ == "__main__":
    create_video()
