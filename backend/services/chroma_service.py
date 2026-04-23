from __future__ import annotations

import uuid
from datetime import datetime, timezone

import chromadb

from config import get_settings

_client = None
_collection = None


def _get_collection():
    global _client, _collection
    if _collection is not None:
        return _collection

    settings = get_settings()
    _client = chromadb.PersistentClient(path=settings.chroma_persist_dir)
    _collection = _client.get_or_create_collection(
        name="automind_reports",
        metadata={"hnsw:space": "cosine"},
    )
    return _collection


def store_memory(content: str, metadata: dict[str, str] | None = None) -> str:
    collection = _get_collection()
    memory_id = uuid.uuid4().hex

    payload = dict(metadata or {})
    payload["created_at"] = datetime.now(timezone.utc).isoformat()

    collection.add(ids=[memory_id], documents=[content], metadatas=[payload])
    return memory_id


def query_memory(query: str, top_k: int = 5) -> list[dict]:
    collection = _get_collection()
    if collection.count() == 0:
        return []

    results = collection.query(query_texts=[query], n_results=min(top_k, collection.count()))

    items: list[dict] = []
    for idx, memory_id in enumerate(results["ids"][0]):
        items.append(
            {
                "memory_id": memory_id,
                "document": results["documents"][0][idx],
                "metadata": results["metadatas"][0][idx],
            }
        )
    return items
