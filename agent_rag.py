# agent_rag.py
# 질문 의도 판단, 검색, 최종 답변 생성을 묶은 Agent RAG 흐름

from langchain_core.messages import HumanMessage, SystemMessage

from prompts import get_agent_answer_prompt, get_agent_decision_prompt
from rag import search_life_docs


VALID_ACTIONS = {
    "life_answer",
    "plan",
    "rewrite",
    "checklist",
    "general",
}

RETRIEVAL_ACTIONS = {
    "life_answer",
    "plan",
    "rewrite",
    "checklist",
}

def invoke_text(llm, system_prompt: str, user_prompt: str) -> str:
    """LLM을 호출하고 문자열 응답만 반환한다."""
    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(content=user_prompt),
        ]
    )
    return response.content.strip()


def decide_action(llm, user_text: str) -> str:
    """사용자 요청에 맞는 작업 종류를 고른다."""
    decision = invoke_text(
        llm=llm,
        system_prompt="당신은 요청을 분류하는 라우팅 에이전트입니다.",
        user_prompt=get_agent_decision_prompt(user_text),
    )

    action = decision.splitlines()[0].strip().lower()
    if action not in VALID_ACTIONS:
        return "life_answer"

    return action


def run_agent_rag(llm, user_text: str, k: int = 4) -> str:
    """
    Agent RAG 흐름을 실행한다.

    1. 사용자 요청 의도 판단
    2. 필요한 경우 생활 문서 검색
    3. 검색 결과를 바탕으로 최종 답변 생성
    """
    action = decide_action(llm, user_text)

    if action in RETRIEVAL_ACTIONS:
        context = search_life_docs(user_text, k=k)
    else:
        context = "문서 검색을 사용하지 않았습니다."

    answer_prompt = get_agent_answer_prompt(
        action=action,
        context=context,
        user_text=user_text,
    )

    return invoke_text(
        llm=llm,
        system_prompt="당신은 로컬 생활 문서를 활용하는 Agent RAG 어시스턴트입니다.",
        user_prompt=answer_prompt,
    )
