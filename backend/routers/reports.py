from fastapi import APIRouter, HTTPException

from agents.orchestrator import generate_full_report
from models.request_models import GenerateReportRequest
from models.response_models import GenerateReportResponse, ReportListItem
from services.report_service import list_reports
from utils.logger import get_logger

logger = get_logger(__name__)
router = APIRouter(tags=["reports"])


@router.post("/generate-report", response_model=GenerateReportResponse)
async def generate_report_route(request: GenerateReportRequest) -> GenerateReportResponse:
    try:
        logger.info(f"API: Received generate-report request for: {request.prompt[:50]}...")
        result = await generate_full_report(request.prompt)
        logger.info(f"API: Report generated successfully - {result['report_id']}")
        return GenerateReportResponse(**result)
    except Exception as exc:
        logger.error(f"API: Report generation failed - {str(exc)}")
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@router.get("/reports", response_model=list[ReportListItem])
def get_reports_route() -> list[ReportListItem]:
    try:
        reports = list_reports()
        items: list[ReportListItem] = []
        for report in reports:
            items.append(
                ReportListItem(
                    report_id=report["report_id"],
                    title=report.get("vehicle_name", "Concept Vehicle")[:60],
                    created_at=report["created_at"],
                    snippet=report.get("vehicle_details", "")[:180],
                )
            )
        return items
    except Exception as exc:
        logger.error(f"API: Failed to fetch reports - {str(exc)}")
        raise HTTPException(status_code=500, detail=str(exc)) from exc
