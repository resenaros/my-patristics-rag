# Local AI Agent (RAG): Ollama + LangChain + Gradio

A locally hosted Retrieval-Augmented Generation (RAG) AI agent powered by:

- **Ollama** (local LLM runtime)
- **LangChain** (RAG orchestration)
- **Chroma** (vector store)
- **Gradio** (GUI & API)
- **pandas** (CSV data handling)

## ⭐️ Project Features

- Modular, clean RAG pipeline
- Fully local LLM with Ollama
- Easy exchange to other LLM providers
- Self-contained dependencies for reproducibility
- GUI and API access
- Docker-ready for Hugging Face Spaces deployment

---

## 🚀 Quickstart: Local Development

### 1. Set up your environment

#### Using [uv](https://github.com/astral-sh/uv):
```bash
curl -Ls https://astral.sh/uv/install.sh | sh
uv init
uv venv
source .venv/bin/activate
uv add langchain langchain-chroma langchain-ollama gradio pandas
uv sync
```

#### Or classic pip:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install langchain langchain-chroma langchain-ollama gradio pandas
```

---

### 2. Prepare your CSV database

Main retrieval file: `patristics.csv`  
Example structure:
```csv
author,text,source
Ignatius of Antioch,"Where the bishop appears, there let the congregation be.","Letter to the Smyrnaeans"
```
Loaded into Chroma vector DB via `vector.py`.

---

### 3. Run locally

```bash
source .venv/bin/activate
python app.py
```
or
```bash
uv run python app.py
```

---

## 🐳 Docker Deployment (Hugging Face Spaces & Local Docker)

**For Hugging Face Spaces:**
- A `Dockerfile` specifying all dependencies and startup commands **(required)**
- An `app.py` as the entrypoint for Gradio (required)
- `[Optional]` An `entrypoint.sh` for managing Ollama and Gradio together (multi-process startup)
- `patristics.csv` and other code files in project root

> Spaces **does not** use `docker-compose.yaml` — it builds from `Dockerfile` only.

**Typical Dockerfile workflow:**
- Installs Ollama and pulls the required LLM model
- Installs Python requirements
- Starts Ollama and Gradio

> See `Dockerfile` (and `entrypoint.sh` if present) in this repo for details.

Learn more: [Hugging Face Spaces Docker Documentation](https://huggingface.co/docs/hub/spaces-docker-overview)

---

### 🔨 Docker Quickstart (Build & Run Locally)

**Build the image:**
```sh
docker build -t local-ai-agent-rag .
```

**Run the image:**
```sh
docker run -p 7860:7860 -p 11434:11434 local-ai-agent-rag
```

**[Optional] Run with Docker Compose (local/dev only):**
```sh
docker compose up --build
```
> You likely **do not need Compose on Spaces**. It is provided for multi-service local dev only.

---

## 📂 Project Structure

```
local-ai-agent-rag/
├── .gitignore               # Excludes DB/env artifacts
├── .dockerignore            # Excludes files from Docker build context
├── app.py                   # Gradio entrypoint
├── Dockerfile               # Space & Docker deployment configuration
├── patristics.csv           # Retrieval database
├── pyproject.toml / uv.lock # Optional: Python dep management
├── README.md
├── vector.py                # Embedding + ingest code
└── entrypoint.sh            # [Optional] Multi-process start script
```

**.gitignore** (example):
```
chroma_langchain_db/
.venv/
*.pyc
__pycache__/
```

**.dockerignore** (example):
```
.venv/
__pycache__/
*.pyc
chroma_langchain_db/
.git
*.ipynb
.env
```

---

## 🧩 Design Notes

- UI and engine code separated for clarity
- LLM provider logic isolated for easy swap
- CSV/embedding scripts reproducible & idempotent
- Local by default, cloud-ready via Docker/Spaces

---

## ℹ️ Ollama Notes

- Ollama enables fully local LLM inference for privacy and speed.
- Not natively supported on Spaces—**Docker deployment is required**.
- The container will run Ollama and Gradio together by default.

---

## 🗒️ Changelog

- Refactored: renamed `main.py` → `app.py`
- Updated: UI theme to Glass (via Gradio)
- Revised: `README.md` for Docker Spaces instructions
- Added: Pandas for CSV handling
- Improved: Reference extraction for church father texts in RAG agent

---

## 🙌 Dependency Management

Supports both **uv** and **pip**:
- Use `uv add` / `uv sync` for modern dependency management, or
- Use `pip install`, `pip freeze` as needed.

---

## 🛠️ Docker Deploy (HF Spaces or Local)

- Ensure `app.py`, `Dockerfile`, `[optional] entrypoint.sh`, and `patristics.csv` are in your repo root.
- Push to Hugging Face Spaces repo.
- Environment is built from your Dockerfile; no Compose file is needed for Spaces.

---