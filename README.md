# Dr. Gideon's Videos - The Right Path Educational Consulting

Professional development video series for K-12 school administrators featuring AI leadership training.

## Project Overview

**Client**: The Right Path Educational Consulting Incorporated
**Lead Consultant**: Dr. William Gideon
**Target Audience**: ACSA Region 14 K-12 Administrators
**Video Series**: AI for Educational Leadership Professional Learning

## Video Details

**Final Video**: `Dr_Gideon_Final_Video.mp4`
**Duration**: 1 minute 56 seconds
**Resolution**: 1920x1080 (Full HD)
**Format**: MP4 with AAC audio

### Content Structure

1. **Introduction** (0:00-1:00)
   - Opening slide with Dr. Gideon introduction
   - AI in education messaging
   - Administrator challenges
   - Partnership proposal

2. **Four Session Series** (1:00-1:53)
   - Session 1: Demystifying AI for School Leaders
   - Session 2: AI as Your Executive Assistant
   - Session 3: Data-Driven Decision Making with AI
   - Session 4: AI for Career Advancement

3. **Closing** (1:53-1:56)
   - Contact information and call to action

## Assets

### Images (15 total)
- `1_Opening.png` - Dr. Gideon introduction slide
- `2_Leadership.png` - Leadership excellence theme
- `4_Challenges.png` - Administrator challenges
- `6_Impact.png` - Professional development impact (AI-generated, diverse educators)
- `7_Four_Sessions.png` - Four sessions overview (appears 4x in video)
- `11_Closing.png` - Contact information
- `12_Session1_Demystifying_AI.png` - AI ethics and workflow (AI-generated)
- `13_Session2_Executive_Assistant.png` - AI automation tools (AI-generated)
- `14_Session3_Data_Driven.png` - Data dashboards (AI-generated)
- `15_Session4_Career_Advancement.png` - Professional growth (AI-generated)

### Audio
- `Dr. Gideon First Video Updated.wav` - Final narration audio
- `Dr. Gideon First Video.vtt` - Subtitle/timing file

### Scripts
- `create_final_video_fast.py` - Main video rendering script
- `generate_session_images.py` - AI image generation (Nano Banana/OpenRouter)
- `regenerate_impact_image.py` - Regenerated 6_Impact.png without misspellings

## Technical Specifications

### Video Features
- **Full-screen coverage**: All images crop to fill 1920x1080 (no black borders)
- **Ken Burns effects**: Smooth zoom/pan animations on dynamic slides
- **Static slides**: Opening, Four Sessions (all 4 appearances), Closing
- **Audio sync**: Perfectly timed with narration timestamps
- **Closing silence**: 3 seconds of silence with closing slide visible

### AI-Generated Images
- **Tool**: OpenRouter Gemini 2.5 Flash Image ("Nano Banana")
- **Style**: Photorealistic, professional, diverse representation
- **Focus**: African American and Latino administrators with multi-ethnic students
- **Resolution**: Optimized for 1920x1080 display

## Production Timeline

### Segment Timing
| Segment | Image | Duration | Effect | Timestamp |
|---------|-------|----------|--------|-----------|
| 1 | Opening | 11s | Static | 0:00-0:11 |
| 2 | Leadership | 13s | Zoom In | 0:11-0:24 |
| 3 | Challenges | 15s | Pan Right | 0:24-0:39 |
| 4 | Impact | 21s | Zoom Out | 0:39-1:00 |
| 5 | Four Sessions | 4s | Static | 1:00-1:04 |
| 6 | Session 1 | 14s | Zoom In | 1:04-1:18 |
| 7 | Four Sessions | 4s | Static | 1:18-1:22 |
| 8 | Session 2 | 6s | Pan Left | 1:22-1:28 |
| 9 | Four Sessions | 4s | Static | 1:28-1:32 |
| 10 | Session 3 | 9s | Zoom Out | 1:32-1:41 |
| 11 | Four Sessions | 4s | Static | 1:41-1:45 |
| 12 | Session 4 | 8s | Zoom In | 1:45-1:53 |
| 13 | Closing | 3s | Static | 1:53-1:56 |

## Rendering

### Fast Render Mode
- **Preset**: ultrafast
- **CRF**: 23 (balanced quality)
- **Audio**: AAC 128k
- **Render time**: ~30 seconds for 1:56 video

### Requirements
- FFmpeg 8.0 or higher
- Python 3.11+
- OpenRouter API key (for image regeneration)

## Usage

To regenerate the video:

```bash
python create_final_video_fast.py
```

To regenerate specific session images:

```bash
python generate_session_images.py
```

## Credits

**Video Production**: Alexandria's Design
**Client**: The Right Path Educational Consulting Inc.
**AI Image Generation**: OpenRouter Gemini 2.5 Flash
**Video Editing**: FFmpeg with Ken Burns effects
**Project Management**: Claude Code + Alexandria's Design Team

---

© 2025 Alexandria's Design | The Right Path Educational Consulting Inc.
