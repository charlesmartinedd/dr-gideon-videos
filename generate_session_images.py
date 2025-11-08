"""
Generate 4 session images for Dr. Gideon video using Nano Banana (OpenRouter Gemini 2.5 Flash)
"""

import os
import requests
import base64
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent.parent.parent / '.env'
load_dotenv(env_path, override=True)

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')

def generate_image(prompt: str, output_filename: str):
    """Generate image using OpenRouter Gemini 2.5 Flash Image"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://alexandriasdesign.com",
        "X-Title": "TRPEC Video Session Images"
    }

    payload = {
        "model": "google/gemini-2.5-flash-image",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "modalities": ["image", "text"]  # Critical for image generation
    }

    print(f"\nGenerating: {output_filename}")
    print(f"Prompt: {prompt[:100]}...")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()

        result = response.json()
        images = result['choices'][0]['message'].get('images', [])

        if not images:
            print(f"ERROR: No images returned for {output_filename}")
            return False

        # Extract and save image
        for img_data in images:
            if isinstance(img_data, dict):
                img_url = img_data.get('image_url', {}).get('url', '') if 'image_url' in img_data else img_data.get('url', '')

                if img_url and img_url.startswith('data:image'):
                    # Extract base64 data
                    base64_data = img_url.split(',')[1]
                    img_bytes = base64.b64decode(base64_data)

                    # Save to file
                    output_path = Path(__file__).parent / output_filename
                    with open(output_path, 'wb') as f:
                        f.write(img_bytes)

                    print(f"SUCCESS: Saved {output_path} ({len(img_bytes):,} bytes)")
                    return True

        print(f"ERROR: Failed to extract image data for {output_filename}")
        return False

    except Exception as e:
        print(f"ERROR generating {output_filename}: {e}")
        return False

# Image prompts - professional, diverse, education-focused
prompts = [
    {
        "filename": "12_Session1_Demystifying_AI.png",
        "prompt": """Create a professional, modern educational scene showing an African American or Latino school administrator (principal or assistant principal in business attire) learning about AI ethics and technology in a bright, contemporary school setting. The administrator is engaged with a laptop or tablet displaying AI-related graphics. In the background, show diverse students (African American, Latino, Asian, White) of various ages using tablets and computers in a collaborative learning environment. The scene should convey innovation, professionalism, and inclusive education. Photorealistic style, warm lighting, 1920x1080 aspect ratio."""
    },
    {
        "filename": "13_Session2_Executive_Assistant.png",
        "prompt": """Create a professional scene showing a Latino or African American school administrator (wearing professional attire) working efficiently at a modern desk with dual monitors displaying AI-powered email drafts, reports, and communication tools. The workspace is organized and tech-forward. Through a glass window or in the background, show diverse students (multi-ethnic group including Black, Latino, Asian, and White students) collaborating with laptops and tablets in a modern classroom. The image should convey productivity, efficiency, and modern educational leadership. Photorealistic style, professional lighting, 1920x1080 aspect ratio."""
    },
    {
        "filename": "14_Session3_Data_Driven.png",
        "prompt": """Create a professional educational scene featuring an African American or Latino administrator analyzing colorful data dashboards and school trend visualizations on a large interactive display or tablet. The data visualizations should show graphs, charts, and student performance metrics in an easy-to-understand format. In the background or adjacent area, show diverse students (representing multiple ethnicities - African American, Latino, Asian, White) engaged with technology, tablets, and interactive learning tools. The scene should convey data-informed decision making, equity, and student success. Photorealistic style, bright professional lighting, 1920x1080 aspect ratio."""
    },
    {
        "filename": "15_Session4_Career_Advancement.png",
        "prompt": """Create an inspiring professional development scene showing a confident Latino or African American school leader working on career advancement materials - a polished resume, cover letter, or interview preparation notes displayed on a laptop or tablet. The setting should be professional yet warm, perhaps in a contemporary office or professional learning space. In the background, show diverse students (multi-ethnic representation including Black, Latino, Asian, White students) engaged in technology-enhanced learning, symbolizing the leader's impact on student success. The image should convey professional growth, ambition, and educational leadership excellence. Photorealistic style, motivational lighting, 1920x1080 aspect ratio."""
    }
]

def main():
    print("=" * 80)
    print("Generating Session Images for Dr. Gideon Video")
    print("=" * 80)

    if not OPENROUTER_API_KEY:
        print("ERROR: OPENROUTER_API_KEY not found in .env file!")
        return

    success_count = 0
    for prompt_data in prompts:
        if generate_image(prompt_data['prompt'], prompt_data['filename']):
            success_count += 1

    print("\n" + "=" * 80)
    print(f"Successfully generated {success_count}/{len(prompts)} images")
    print("=" * 80)

if __name__ == "__main__":
    main()
