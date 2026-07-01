# app.py
# Local Life Assistant 메인 실행 파일

from langchain_ollama import ChatOllama

from agent_rag import run_agent_rag


MODEL_NAME = "exaone3.5:7.8b"


def load_llm():
    """Ollama 로컬 LLM을 불러온다."""
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0.2,
    )


def main():
    print("Local Life Assistant를 시작합니다.")
    print("종료하려면 q, quit, exit 중 하나를 입력하세요.")
    print("모델 로딩 중입니다...\n")

    llm = load_llm()

    while True:
        user_text = input("무엇을 도와드릴까요? ").strip()

        if user_text.lower() in {"q", "quit", "exit"}:
            print("프로그램을 종료합니다.")
            break

        if not user_text:
            print("입력 내용이 비어 있습니다.\n")
            continue

        print("\n요청을 분석하고 생활 문서를 확인 중입니다...\n")

        try:
            answer = run_agent_rag(llm, user_text)
        except FileNotFoundError as error:
            print(f"[오류] {error}\n")
            continue

        print("[답변]")
        print(answer)
        print()


if __name__ == "__main__":
    main()