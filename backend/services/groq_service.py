from langchain_groq import ChatGroq

from config import get_settings


def get_groq_llm() -> ChatGroq:
    settings = get_settings()
    if not settings.groq_api_key:
        raise ValueError("GROQ_API_KEY is not set. Add it in backend/.env")

    return ChatGroq(
        groq_api_key=settings.groq_api_key,
        model=settings.groq_model,
        temperature=0.3,
    )
