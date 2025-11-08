"""
Create Dr. Gideon video with precise timing and Ken Burns effects
Timeline based on VTT timestamps
"""

import subprocess
from pathlib import Path

# Project paths
PROJECT_DIR = Path(__file__).parent
AUDIO_FILE = PROJECT_DIR.parent / "Dr_Gideon_Audio_Cleaned.mp3"
OUTPUT_FILE = PROJECT_DIR / "Dr_Gideon_Final_Video.mp4"

# Image timeline with Ken Burns effects
# Format: (image_file, start_time, duration, ken_burns_type)
# Ken Burns types: None, "zoom_in", "zoom_out", "pan_right", "pan_left"

timeline = [
    # Pre-sessions introduction (0:00 - 1:00)
    ("1_Opening.png", 0.0, 11.0, None),  # STATIC - no Ken Burns
    ("2_Leadership.png", 11.0, 13.0, "zoom_in"),
    ("4_Challenges.png", 24.0, 15.0, "pan_right"),
    ("6_Impact.png", 39.0, 21.0, "zoom_out"),

    # Four Sessions section (1:00 - 1:53)
    ("7_Four_Sessions.png", 60.0, 2.0, None),  # STATIC - 1st appearance
    ("12_Session1_Demystifying_AI.png", 62.0, 16.0, "zoom_in"),

    ("7_Four_Sessions.png", 78.0, 2.0, None),  # STATIC - 2nd appearance
    ("13_Session2_Executive_Assistant.png", 80.0, 8.0, "pan_left"),

    ("7_Four_Sessions.png", 88.0, 2.0, None),  # STATIC - 3rd appearance
    ("14_Session3_Data_Driven.png", 90.0, 11.0, "zoom_out"),

    ("7_Four_Sessions.png", 101.0, 2.0, None),  # STATIC - 4th appearance
    ("15_Session4_Career_Advancement.png", 103.0, 10.0, "zoom_in"),

    # Closing (1:53+)
    ("11_Closing.png", 113.0, 5.0, None),  # STATIC - no Ken Burns
]

def create_ken_burns_filter(effect_type, duration):
    """
    Create FFmpeg zoompan filter for Ken Burns effect
    1920x1080 target resolution
    """
    if effect_type is None:
        # Static image - just scale to fit
        return "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black"

    fps = 30
    frames = int(duration * fps)

    # Ken Burns effect variations
    effects = {
        "zoom_in": f"zoompan=z='min(zoom+0.0015,1.5)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "zoom_out": f"zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "pan_right": f"zoompan=z='1.3':d={frames}:x='min(iw/zoom*(on/{frames}),iw/zoom)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "pan_left": f"zoompan=z='1.3':d={frames}:x='iw/zoom-iw/zoom*(on/{frames})':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
    }

    return effects.get(effect_type, effects["zoom_in"])

def create_video():
    """Create video using FFmpeg with complex filter"""

    print("=" * 80)
    print("Creating Dr. Gideon Video")
    print("=" * 80)

    # Build FFmpeg filter complex
    filter_parts = []
    input_args = []

    # Add all image inputs
    for i, (image_file, _, _, _) in enumerate(timeline):
        image_path = PROJECT_DIR / image_file
        if not image_path.exists():
            print(f"ERROR: Missing image {image_path}")
            return False
        input_args.extend(["-loop", "1", "-t", str(timeline[i][2]), "-i", str(image_path)])

    # Add audio input
    input_args.extend(["-i", str(AUDIO_FILE)])

    # Create filters for each image
    for i, (_, _, duration, effect) in enumerate(timeline):
        filter_str = create_ken_burns_filter(effect, duration)
        filter_parts.append(f"[{i}:v]{filter_str}[v{i}]")

    # Concatenate all video streams
    concat_inputs = "".join(f"[v{i}]" for i in range(len(timeline)))
    filter_parts.append(f"{concat_inputs}concat=n={len(timeline)}:v=1:a=0[outv]")

    filter_complex = ";".join(filter_parts)

    # Build complete FFmpeg command
    audio_index = len(timeline)  # Audio is the last input

    ffmpeg_cmd = [
        "ffmpeg", "-y",
        *input_args,
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", f"{audio_index}:a",
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        str(OUTPUT_FILE)
    ]

    print("\nRendering video...")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Timeline: {len(timeline)} segments")
    print(f"Total duration: ~{sum(t[2] for t in timeline):.1f} seconds\n")

    # Execute FFmpeg
    try:
        result = subprocess.run(ffmpeg_cmd, check=True, capture_output=True, text=True)
        print("\n" + "=" * 80)
        print(f"SUCCESS: Video created at {OUTPUT_FILE}")
        print("=" * 80)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: FFmpeg failed")
        print(f"Command: {' '.join(ffmpeg_cmd)}")
        print(f"Error output: {e.stderr}")
        return False

if __name__ == "__main__":
    if not AUDIO_FILE.exists():
        print(f"ERROR: Audio file not found: {AUDIO_FILE}")
    else:
        create_video()
