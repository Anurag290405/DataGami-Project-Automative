from langchain_core.prompts import ChatPromptTemplate

from services.groq_service import get_groq_llm


def research(prompt: str) -> str:
    llm = get_groq_llm()
    template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are an automotive research analyst. Return factual, technical, structured insights only.",
            ),
            ("human", "{prompt}"),
        ]
    )
    response = (template | llm).invoke({"prompt": prompt})
    return response.content.strip()
