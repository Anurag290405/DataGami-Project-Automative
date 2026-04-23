from langchain_core.prompts import ChatPromptTemplate

from services.groq_service import get_groq_llm


def enhance_prompt(prompt: str) -> str:
    llm = get_groq_llm()
    template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an automotive prompt enhancement specialist. Return only the enhanced prompt."),
            ("human", "{prompt}"),
        ]
    )
    response = (template | llm).invoke({"prompt": prompt})
    return response.content.strip()
