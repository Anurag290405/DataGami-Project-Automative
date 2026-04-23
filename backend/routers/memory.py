from fastapi import APIRouter, HTTPException

from models.request_models import StoreMemoryRequest
from models.response_models import StoreMemoryResponse
from services.chroma_service import store_memory

router = APIRouter(tags=["memory"])


@router.post("/store-memory", response_model=StoreMemoryResponse)
def store_memory_route(request: StoreMemoryRequest) -> StoreMemoryResponse:
    try:
        memory_id = store_memory(request.content, request.metadata)
        return StoreMemoryResponse(status="stored", memory_id=memory_id)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
