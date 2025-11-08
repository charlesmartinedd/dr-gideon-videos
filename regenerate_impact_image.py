"""
Regenerate 6_Impact.png with correct spelling - professional development scene
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

def generate_impact_image():
    """Generate new 6_Impact.png image"""

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "https://alexandriasdesign.com",
        "X-Title": "TRPEC Impact Image"
    }

    prompt = """Create a professional, inspiring educational scene showing an African American or Latino school administrator (wearing professional business attire) presenting or facilitating a professional development session about AI in education. The administrator is confident and engaged, leading a dynamic workshop or presentation. In the background and around the room, show diverse K-12 students (African American, Latino, Asian, White) of various ages actively using tablets, laptops, and modern technology in collaborative learning. The scene should convey innovation, partnership, professional learning, and transformative leadership development. Modern classroom or professional learning space with contemporary furniture, bright natural lighting, educational posters on walls. Photorealistic style, inspirational and professional atmosphere, 1920x1080 aspect ratio."""

    payload = {
        "model": "google/gemini-2.5-flash-image",
        "messages": [{"role": "user", "content": prompt}],
        "modalities": ["image", "text"]
    }

    print("Generating new 6_Impact.png image...")
    print(f"Prompt: {prompt[:100]}...")

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        response.raise_for_status()

        result = response.json()
        images = result['choices'][0]['message'].get('images', [])

        if not images:
            print("ERROR: No images returned")
            return False

        for img_data in images:
            if isinstance(img_data, dict):
                img_url = img_data.get('image_url', {}).get('url', '') if 'image_url' in img_data else img_data.get('url', '')

                if img_url and img_url.startswith('data:image'):
                    base64_data = img_url.split(',')[1]
                    img_bytes = base64.b64decode(base64_data)

                    output_path = Path(__file__).parent / "6_Impact.png"
                    with open(output_path, 'wb') as f:
                        f.write(img_bytes)

                    print(f"SUCCESS: Saved {output_path} ({len(img_bytes):,} bytes)")
                    return True

        print("ERROR: Failed to extract image data")
        return False

    except Exception as e:
        print(f"ERROR: {e}")
        return False

if __name__ == "__main__":
    if not OPENROUTER_API_KEY:
        print("ERROR: OPENROUTER_API_KEY not found in .env file!")
    else:
        generate_impact_image()
