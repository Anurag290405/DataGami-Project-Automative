from __future__ import annotations

import uuid
from pathlib import Path

from config import get_settings
from services.image_service import generate_vehicle_image as generate_fallback_image
from utils.logger import get_logger

logger = get_logger(__name__)

IMAGES_DIR = Path("./database/generated_images")
IMAGES_DIR.mkdir(parents=True, exist_ok=True)


def _get_client():
    """Return Google GenAI client lazily so missing package doesn't crash app startup."""
    settings = get_settings()
    if not settings.google_api_key:
        raise ValueError("GOOGLE_API_KEY is not set. Add it in backend/.env")
    try:
        from google import genai
    except Exception as exc:
        raise RuntimeError(
            "Google GenAI SDK is not installed in the active environment. Falling back to Pollinations is recommended."
        ) from exc
    return genai.Client(api_key=settings.google_api_key)


def generate_vehicle_summary(prompt: str) -> dict:
    """Return vehicle name, 3-4 specs, and concise details using Gemini LLM."""
    logger.info("Generating summary for prompt: %s", prompt[:50])
    
    try:
        client = _get_client()
        settings = get_settings()
        
        system_instruction = (
            "You are an automotive design expert. Based on the user's prompt, "
            "generate a concept vehicle name, 4 technical specifications, and a concise 2-sentence description. "
            "Respond ONLY in JSON format with keys: 'vehicle_name', 'specifications' (list of 4 strings), and 'vehicle_details'. "
            "Do NOT include any markdown formatting like ```json."
        )
        
        response = client.models.generate_content(
            model=settings.google_text_model,
            contents=[f"{system_instruction}\n\nPrompt: {prompt}"],
        )
        
        import json
        text = response.text.strip()
        # Remove markdown if present
        if text.startswith("```json"):
            text = text[7:]
        if text.endswith("```"):
            text = text[:-3]
        
        data = json.loads(text.strip())
        return {
            "vehicle_name": data.get("vehicle_name", "AutoMind Concept"),
            "specifications": data.get("specifications", ["Spec 1", "Spec 2", "Spec 3", "Spec 4"]),
            "vehicle_details": data.get("vehicle_details", f"A custom vehicle designed for: {prompt}"),
        }
    except Exception as exc:
        logger.warning("Gemini summary generation failed, using fallback: %s", str(exc))
        # Fallback logic (more flexible than before)
        lower = prompt.lower()
        body = "Vehicle"
        if "truck" in lower: body = "Truck"
        elif "sedan" in lower: body = "Sedan"
        elif "bike" in lower: body = "Motorcycle"
        elif "suv" in lower: body = "SUV"
        
        return {
            "vehicle_name": f"AutoMind {body} Concept",
            "specifications": [
                "Powertrain: Performance-tuned for specific road conditions.",
                "Performance: Dynamic power delivery with optimized efficiency.",
                "Design: Sculpted exterior with integrated aerodynamic elements.",
                "Cabin: Ergonomic interior with advanced driver assistance systems.",
            ],
            "vehicle_details": f"This {body.lower()} concept is meticulously designed based on your request: {prompt}.",
        }


def generate_vehicle_image(prompt: str, vehicle_name: str) -> str:
    """Generate vehicle image with Google API; fallback to Pollinations if Google is unavailable/fails."""
    settings = get_settings()
    client = None
    try:
        client = _get_client()
    except Exception as exc:
        logger.warning("Google client unavailable, using Pollinations fallback: %s", str(exc))
        return generate_fallback_image(prompt, style="photorealistic")

    image_prompt = (
        f"Create a photorealistic concept vehicle image. "
        f"Vehicle name: {vehicle_name}. "
        f"Design intent: {prompt}. "
        "Front three-quarter view, studio lighting, high detail, clean background."
    )

    try:
        response = client.models.generate_content(
            model=settings.google_image_model,
            contents=[image_prompt],
        )
    except Exception as exc:
        logger.warning("Google image generation failed, using Pollinations fallback: %s", str(exc))
        return generate_fallback_image(prompt, style="photorealistic")

    image_bytes = None
    for candidate in getattr(response, "candidates", []) or []:
        content = getattr(candidate, "content", None)
        parts = getattr(content, "parts", []) if content else []
        for part in parts:
            inline_data = getattr(part, "inline_data", None)
            data = getattr(inline_data, "data", None) if inline_data else None
            if data:
                image_bytes = data
                break
        if image_bytes:
            break

    if not image_bytes:
        logger.warning("Google image response had no image bytes, using Pollinations fallback")
        return generate_fallback_image(prompt, style="photorealistic")

    filename = f"{uuid.uuid4().hex}.png"
    filepath = IMAGES_DIR / filename
    filepath.write_bytes(image_bytes)

    logger.info("Saved Google-generated image: %s", filename)
    return filename


def get_image_url(filename: str) -> str:
    return f"/images/{filename}"
