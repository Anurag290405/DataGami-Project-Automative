from datetime import datetime, timezone
import uuid


def compose_response(
    prompt: str,
    vehicle_name: str,
    specifications: list[str],
    vehicle_details: str,
    image_filename: str,
    image_url: str,
    image_error: str = "",
) -> dict:
    report_id = f"rep_{uuid.uuid4().hex[:12]}"

    return {
        "report_id": report_id,
        "prompt": prompt,
        "vehicle_name": vehicle_name,
        "specifications": specifications,
        "vehicle_details": vehicle_details,
        "image_filename": image_filename,
        "image_url": image_url,
        "image_error": image_error,
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
