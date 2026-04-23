from fastapi import APIRouter, HTTPException

from agents.prompt_enhancer_agent import enhance_prompt
from models.request_models import PromptRequest
from models.response_models import EnhancePromptResponse

router = APIRouter(tags=["prompts"])


@router.post("/enhance-prompt", response_model=EnhancePromptResponse)
def enhance_prompt_route(request: PromptRequest) -> EnhancePromptResponse:
    try:
        enhanced = enhance_prompt(request.prompt)
        return EnhancePromptResponse(enhanced_prompt=enhanced)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc)) from exc
