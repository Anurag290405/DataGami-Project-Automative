from langchain_core.prompts import ChatPromptTemplate

from services.groq_service import get_groq_llm


def write_report(research_summary: str, enhanced_prompt: str) -> str:
    llm = get_groq_llm()
    template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a senior automotive technical writer. Produce a professional report with clear sections.",
            ),
            ("human", "Research:\n{research_summary}\n\nPrompt:\n{enhanced_prompt}"),
        ]
    )
    response = (template | llm).invoke(
        {"research_summary": research_summary, "enhanced_prompt": enhanced_prompt}
    )
    return response.content.strip()
