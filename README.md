# Local Life Assistant

Ollama 기반 로컬 Agent RAG 생활 어시스턴트입니다.

`data` 폴더에 넣은 Markdown/PDF 문서를 ChromaDB 벡터DB로 만들고, 사용자의 질문을 분석한 뒤 필요한 문서를 검색해 답변합니다. 외부 LLM API를 사용하지 않고 로컬 Ollama 모델로 동작합니다.

## 프로젝트 개요

일상 업무, 조교 수업 관리, 연구실 생활 규칙, 논문 작성 스타일, 학교 안내 PDF처럼 자주 참고해야 하는 문서들을 로컬에서 검색하고 답변하기 위한 개인용 AI 어시스턴트입니다.

예를 들어 다음과 같은 질문에 답할 수 있습니다.

```text
시험 감독할 때 뭐 해야 해?
e-보강 동영상은 몇 분 이상이어야 해?
우리 연구실 스타일로 Discussion 섹션에는 뭘 넣어야 해?
조교 임용 관련 유의사항 알려줘
```

## 주요 기능

### 1. Agent RAG 기반 질의응답

사용자 요청을 먼저 분류한 뒤, 필요한 경우 로컬 문서 DB에서 관련 내용을 검색해 답변합니다.

```text
사용자 요청
→ 요청 유형 판단
→ 관련 문서 검색
→ 검색 결과 기반 답변 생성
```

### 2. 로컬 문서 기반 답변

`data` 폴더에 넣은 `.md`, `.txt`, `.pdf` 파일을 참고합니다.

예시 문서:

```text
data/personal_policy.md
data/lab_paper_style.md
data/e_makeup_class_rules.pdf
data/teaching_assistant_guidelines.pdf
data/lab_papers/paper_01.pdf
```

### 3. 연구실 논문 작성 스타일 지원

최근 연구실 논문 PDF와 `lab_paper_style.md`를 함께 사용해 Introduction, Experiments, Discussion 등 섹션별 작성 방식을 참고할 수 있습니다.

예시 질문:

```text
우리 연구실 스타일로 Experiment 섹션에는 뭘 넣어야 해?
Discussion에는 Grad-CAM을 어떻게 넣으면 좋아?
Mismatching cases는 어느 섹션에서 다루면 좋아?
```

## 기술 스택

- Python
- Ollama
- EXAONE 3.5 7.8B
- nomic-embed-text
- LangChain
- ChromaDB
- PyPDF
- Agent RAG

## 프로젝트 구조

```text
local-life-assistant/
├─ app.py
├─ agent_rag.py
├─ build_vector_db.py
├─ rag.py
├─ prompts.py
├─ requirements.txt
├─ README.md
├─ .gitignore
├─ data/
│  ├─ personal_policy.md
│  ├─ lab_paper_style.md
│  ├─ *.pdf
│  └─ lab_papers/
│     └─ *.pdf
└─ chroma_db/
```

## 파일 설명

| 파일 | 설명 |
| --- | --- |
| `app.py` | CLI 기반 로컬 생활 어시스턴트 실행 파일 |
| `agent_rag.py` | 요청 분류, 문서 검색, 답변 생성을 묶은 Agent RAG 흐름 |
| `build_vector_db.py` | `data` 폴더의 Markdown/TXT/PDF 문서를 ChromaDB로 변환 |
| `rag.py` | ChromaDB에서 관련 문서를 검색 |
| `prompts.py` | 요청 분류와 최종 답변 생성을 위한 프롬프트 |
| `data/personal_policy.md` | 개인 생활 규칙 및 조교 업무 규칙 |
| `data/lab_paper_style.md` | 연구실 논문 작성 스타일 요약 문서 |
| `requirements.txt` | 실행에 필요한 Python 패키지 목록 |

## 실행 방법

### 1. Ollama 모델 다운로드

```bash
ollama pull exaone3.5:7.8b
ollama pull nomic-embed-text
```

### 2. 가상환경 생성 및 활성화

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Git Bash:

```bash
source .venv/Scripts/activate
```

### 3. 패키지 설치

```bash
python -m pip install -r requirements.txt
```

### 4. 벡터DB 생성

`data` 폴더에 문서를 넣은 뒤 실행합니다.

```bash
python build_vector_db.py
```

문서를 추가하거나 수정하면 이 명령을 다시 실행해야 검색 결과에 반영됩니다.

### 5. 앱 실행

```bash
python app.py
```

실행 후 질문을 입력합니다.

```text
무엇을 도와드릴까요?
```

종료하려면 다음 중 하나를 입력합니다.

```text
q
quit
exit
```

## 사용 예시

```text
무엇을 도와드릴까요? 시험 감독할 때 준비할 것 알려줘
```

```text
무엇을 도와드릴까요? 우리 연구실 스타일로 Discussion 섹션에는 뭘 넣어야 해?
```

```text
무엇을 도와드릴까요? e-보강 1.5시간 수업은 동영상이 몇 분 이상이어야 해?
```

## Agent RAG 구조

```text
data 문서
→ 문서 로드
→ chunk 분할
→ nomic-embed-text로 임베딩
→ ChromaDB 저장
→ 사용자 질문 입력
→ 요청 분류
→ 관련 chunk 검색
→ exaone3.5:7.8b로 답변 생성
```

## 로컬 실행 특징

- 외부 LLM API를 사용하지 않습니다.
- Ollama 모델이 로컬에 설치되어 있으면 인터넷 없이도 답변할 수 있습니다.
- PDF와 Markdown 문서를 로컬에서 직접 검색합니다.
- 개인 문서나 연구실 문서를 GitHub에 올리지 않고 로컬에서만 사용할 수 있습니다.

## 주의사항

- `chroma_db/`는 다시 생성할 수 있으므로 GitHub에 포함하지 않습니다.
- `.venv/`는 로컬 가상환경이므로 GitHub에 포함하지 않습니다.
- PDF 원문은 용량, 저작권, 내부 문서 이슈가 있을 수 있으므로 public GitHub에는 올리지 않는 것을 권장합니다.
- `desktop.ini`는 Windows가 자동 생성하는 폴더 설정 파일이므로 GitHub에 올리지 않습니다.
