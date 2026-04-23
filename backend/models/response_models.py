from pydantic import BaseModel


class EnhancePromptResponse(BaseModel):
    enhanced_prompt: str


class StoreMemoryResponse(BaseModel):
    status: str
    memory_id: str


class GenerateReportResponse(BaseModel):
    report_id: str
    prompt: str
    vehicle_name: str
    specifications: list[str]
    vehicle_details: str
    image_url: str
    image_filename: str
    image_error: str = ""
    created_at: str


class ReportListItem(BaseModel):
    report_id: str
    title: str
    created_at: str
    snippet: str
