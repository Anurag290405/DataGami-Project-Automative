from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import json

REPORT_STORE = Path("./database/reports/reports.json")


def _ensure_store() -> None:
    REPORT_STORE.parent.mkdir(parents=True, exist_ok=True)
    if not REPORT_STORE.exists():
        REPORT_STORE.write_text("[]", encoding="utf-8")


def list_reports() -> list[dict]:
    _ensure_store()
    data = json.loads(REPORT_STORE.read_text(encoding="utf-8"))
    data.sort(key=lambda x: x["created_at"], reverse=True)
    return data


def save_report(report_payload: dict) -> None:
    _ensure_store()
    data = json.loads(REPORT_STORE.read_text(encoding="utf-8"))
    if "created_at" not in report_payload:
        report_payload["created_at"] = datetime.now(timezone.utc).isoformat()
    data.append(report_payload)
    REPORT_STORE.write_text(json.dumps(data, indent=2), encoding="utf-8")
