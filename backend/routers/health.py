from fastapi import APIRouter

from config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health_check() -> dict:
    settings = get_settings()
    return {"status": "ok", "service": settings.app_name}
