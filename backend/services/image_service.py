import requests
import uuid
from pathlib import Path
import logging
from utils.logger import get_logger

logger = get_logger(__name__)

IMAGES_DIR = Path("./database/generated_images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def generate_vehicle_image(enhanced_prompt: str, style: str = "photorealistic") -> str:
    """
    Generates vehicle image using Pollinations.ai — completely free, no API key needed.
    Uses FLUX model under the hood. THIS IS A SYNCHRONOUS FUNCTION (runs in thread pool).
    
    Args:
        enhanced_prompt: The refined automotive design prompt
        style: Style modifier (photorealistic, concept art, wireframe)
        
    Returns:
        Filename of the saved image
    """
    style_suffix_map = {
        "photorealistic": "ultra photorealistic automotive photography, studio lighting, 8K, professional vehicle magazine",
        "concept art": "automotive concept art, professional render, design studio, Behance quality, 3D render",
        "wireframe": "technical automotive blueprint, CAD wireframe, glowing lines, dark background, technical drawing",
    }

    full_prompt = f"{enhanced_prompt}. {style_suffix_map.get(style, style_suffix_map['photorealistic'])}"
    logger.info(f"[IMAGE] Full prompt: {full_prompt[:100]}...")

    try:
        # Pollinations.ai — free image generation API
        import urllib.parse
        encoded = urllib.parse.quote(full_prompt)
        url = f"https://image.pollinations.ai/prompt/{encoded}?width=1792&height=1024&nologo=true&enhance=true"

        logger.info(f"[IMAGE] Requesting: {url[:100]}...")
        response = requests.get(url, timeout=120)
        logger.info(f"[IMAGE] Status code: {response.status_code}")
        response.raise_for_status()

        filename = f"{uuid.uuid4().hex}.png"
        filepath = IMAGES_DIR / filename

        with open(filepath, "wb") as f:
            f.write(response.content)

        file_size = filepath.stat().st_size
        logger.info(f"[IMAGE] ✅ Saved: {filename} ({file_size / 1024:.1f} KB)")
        return filename

    except requests.exceptions.Timeout:
        logger.error(f"[IMAGE] ❌ Timeout: Image generation took too long")
        raise
    except requests.exceptions.ConnectionError as e:
        logger.error(f"[IMAGE] ❌ Connection error: {str(e)}")
        raise
    except requests.exceptions.HTTPError as e:
        logger.error(f"[IMAGE] ❌ HTTP error: {response.status_code} - {str(e)}")
        raise
    except Exception as e:
        logger.error(f"[IMAGE] ❌ Unexpected error: {str(e)}", exc_info=True)
        raise


def get_image_url(filename: str) -> str:
    """Returns the public URL for a stored image."""
    return f"/images/{filename}"
