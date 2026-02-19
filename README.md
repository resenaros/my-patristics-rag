# Local AI Agent (RAG) — Ollama + LangChain + Gradio

A locally hosted Retrieval-Augmented Generation (RAG) AI agent using:

- Ollama (local LLM runtime)
- LangChain (RAG orchestration)
- Chroma (vector store)
- Gradio (UI layer)
- uv (modern Python package manager)
- WSL (Linux development environment)

---

## Project Goals

- Clean, modular RAG system
- Fully local LLM (Ollama)
- Production-ready architecture
- Swappable LLM provider (e.g., Hugging Face)
- Clean dependencies and docs
- Deployment-ready

---

## Development Environment Setup (WSL + uv)

### 1. Install WSL

(Windows Subsystem for Linux)

---

### 2. Install `uv` (Python Package Manager)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Reload shell:
```bash
source $HOME/.local/bin/env
```

Verify installation:
```bash
uv --version
```

---

### 3. Initialize Project

Inside project directory:
```bash
uv init
```
Creates:
- `pyproject.toml`
- `.python-version`

---

### 4. Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

---

### 5. Add Dependencies

```bash
uv add langchain
uv add langchain-chroma
uv add langchain-ollama
uv add gradio
uv sync
uv pip list
```

#### Dependencies

```toml
dependencies = [
    "langchain",
    "langchain-chroma",
    "langchain-ollama",
    "gradio"
]
```

Other dependencies resolved/locked in `uv.lock`.

---

## Planned Architecture

```
local-ai-agent-rag/
│
├── app.py              # Gradio UI
├── rag/
│   ├── __init__.py
│   ├── llm.py          # LLM provider (swappable)
│   ├── retriever.py    # Chroma setup
│   ├── chain.py        # RAG pipeline
│
├── data/               # Source docs
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## Design Principles

- UI separated from logic
- LLM provider isolated for future swaps
- Dependency management/reproducibility via uv & uv.lock
- Local-first; deployment-ready architecture

---

## Why Ollama?

- Run LLMs locally
- No API costs
- Full model control
- Offline use

**Note:** Ollama cannot be freely hosted on platforms like Hugging Face Spaces or Streamlit Cloud, since it needs a persistent model server. For public deployment, swap LLM provider to an inference API.

---

## Next Steps

- Implement `rag/llm.py`
- Implement Chroma retriever
- Build RAG chain
- Connect to Gradio UI
- Add usage instructions
- Prepare Hugging Face provider swap

---

## How to Run

```bash
source .venv/bin/activate
python app.py
```