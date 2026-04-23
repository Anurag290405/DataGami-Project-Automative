import asyncio

from agents.response_agent import compose_response
from services.google_vehicle_service import (
    generate_vehicle_image,
    generate_vehicle_summary,
    get_image_url,
)
from services.report_service import save_report
from utils.logger import get_logger

logger = get_logger(__name__)


async def generate_full_report(prompt: str) -> dict:
    """Generate a vehicle image and concise vehicle information using Google API."""
    logger.info("Orchestrator: Starting generation for prompt: %s", prompt[:60])

    summary = await asyncio.to_thread(generate_vehicle_summary, prompt)
    vehicle_name = summary["vehicle_name"]
    specifications = summary["specifications"]
    vehicle_details = summary["vehicle_details"]

    image_filename = ""
    image_url = ""
    image_error = ""
    try:
        image_filename = await asyncio.to_thread(generate_vehicle_image, prompt, vehicle_name)
        image_url = get_image_url(image_filename)
    except Exception as exc:
        image_error = str(exc)
        logger.error("Orchestrator: Image generation failed - %s", image_error)

    response = compose_response(
        prompt=prompt,
        vehicle_name=vehicle_name,
        specifications=specifications,
        vehicle_details=vehicle_details,
        image_filename=image_filename,
        image_url=image_url,
        image_error=image_error,
    )
    save_report(response)
    logger.info("Orchestrator: Generation complete - %s", response["report_id"])
    return response
