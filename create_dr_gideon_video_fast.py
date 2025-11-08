"""
Fast lightweight version of Dr. Gideon video - optimized for quick rendering
"""

import subprocess
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
AUDIO_FILE = PROJECT_DIR.parent / "Dr_Gideon_Audio_Cleaned.mp3"
OUTPUT_FILE = PROJECT_DIR / "Dr_Gideon_Video_Fast.mp4"
FFMPEG_PATH = Path(r"C:\Users\MarieLexisDad\CAAASA VIdeo\New Video\ffmpeg-8.0-essentials_build\bin\ffmpeg.exe")

# Simplified timeline - same structure but faster encoding
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
    if effect_type is None:
        return "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2:black"

    fps = 30
    frames = int(duration * fps)

    effects = {
        "zoom_in": f"zoompan=z='min(zoom+0.0015,1.5)':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "zoom_out": f"zoompan=z='if(lte(zoom,1.0),1.5,max(1.0,zoom-0.0015))':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "pan_right": f"zoompan=z='1.3':d={frames}:x='min(iw/zoom*(on/{frames}),iw/zoom)':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
        "pan_left": f"zoompan=z='1.3':d={frames}:x='iw/zoom-iw/zoom*(on/{frames})':y='ih/2-(ih/zoom/2)':s=1920x1080:fps={fps}",
    }
    return effects.get(effect_type, effects["zoom_in"])

def create_video():
    print("=" * 80)
    print("FAST RENDER MODE - Dr. Gideon Video")
    print("=" * 80)

    filter_parts = []
    input_args = []

    for i, (image_file, _, duration, _) in enumerate(timeline):
        image_path = PROJECT_DIR / image_file
        if not image_path.exists():
            print(f"ERROR: Missing {image_path}")
            return False
        input_args.extend(["-loop", "1", "-t", str(duration), "-i", str(image_path)])

    input_args.extend(["-i", str(AUDIO_FILE)])

    for i, (_, _, duration, effect) in enumerate(timeline):
        filter_str = create_ken_burns(effect, duration)
        filter_parts.append(f"[{i}:v]{filter_str}[v{i}]")

    concat_inputs = "".join(f"[v{i}]" for i in range(len(timeline)))
    filter_parts.append(f"{concat_inputs}concat=n={len(timeline)}:v=1:a=0[outv]")

    filter_complex = ";".join(filter_parts)
    audio_index = len(timeline)

    ffmpeg_cmd = [
        str(FFMPEG_PATH), "-y",
        *input_args,
        "-filter_complex", filter_complex,
        "-map", "[outv]",
        "-map", f"{audio_index}:a",
        "-c:v", "libx264",
        "-preset", "ultrafast",  # FAST ENCODING
        "-crf", "23",  # BALANCED QUALITY
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "128k",  # LOWER AUDIO BITRATE
        "-shortest",
        str(OUTPUT_FILE)
    ]

    print(f"\nRendering (FAST MODE)...")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Segments: {len(timeline)}")
    print(f"Est. time: 2-3 minutes\n")

    try:
        subprocess.run(ffmpeg_cmd, check=True)
        print("\n" + "=" * 80)
        print(f"SUCCESS: {OUTPUT_FILE}")
        print("=" * 80)
        return True
    except subprocess.CalledProcessError as e:
        print(f"\nERROR: Rendering failed - {e}")
        return False

if __name__ == "__main__":
    if not AUDIO_FILE.exists():
        print(f"ERROR: Audio not found: {AUDIO_FILE}")
    else:
        create_video()
