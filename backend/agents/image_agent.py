import asyncio
from services.image_service import generate_car_image, get_image_url
from utils.logger import get_logger

logger = get_logger(__name__)


async def generate_image(enhanced_prompt: str, style: str = "photorealistic") -> dict:
    """
    Image Agent: Generates concept car visuals based on enhanced prompt.
    
    Args:
        enhanced_prompt: The refined automotive design prompt
        style: Style modifier (photorealistic, concept art, wireframe)
        
    Returns:
        Dict with image_filename and image_url
    """
    logger.info(f"[IMG_AGENT] Starting: '{enhanced_prompt[:60]}...'")
    
    try:
        # Run blocking image generation in thread pool
        image_filename = await asyncio.to_thread(generate_car_image, enhanced_prompt, style)
        image_url = get_image_url(image_filename)
        
        logger.info(f"[IMG_AGENT] ✅ Success: {image_filename}")
        return {
            "image_filename": image_filename,
            "image_url": image_url,
            "status": "success"
        }
    except Exception as e:
        logger.error(f"[IMG_AGENT] ❌ Failed: {str(e)}", exc_info=True)
        return {
            "image_filename": "",
            "image_url": "",
            "status": "failed",
            "error": str(e)
        }
