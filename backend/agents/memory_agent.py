from services.chroma_service import store_memory


def save_memory(report_id: str, content: str, metadata: dict[str, str] | None = None) -> str:
    payload = dict(metadata or {})
    payload["report_id"] = report_id
    return store_memory(content=content, metadata=payload)
