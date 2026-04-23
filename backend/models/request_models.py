from pydantic import BaseModel, Field


class PromptRequest(BaseModel):
    prompt: str = Field(..., min_length=5, max_length=1000)


class GenerateReportRequest(BaseModel):
    prompt: str = Field(..., min_length=5, max_length=1000)
    stream: bool = False


class StoreMemoryRequest(BaseModel):
    report_id: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)
    metadata: dict[str, str] | None = None
