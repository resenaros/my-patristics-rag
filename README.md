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

---

## 🐳 Docker Deployment (Hugging Face Spaces)

**Spaces requires:**
- A `Dockerfile` specifying your dependencies and startup commands
- An `app.py` as the entrypoint (contains your Gradio UI/logic)
- [Optional] An `entrypoint.sh` for managing background services (Ollama + Gradio)

**Typical Dockerfile workflow:**
- Installs Ollama and pulls the required LLM model
- Installs Python requirements
- Starts Ollama and Gradio

> See `Dockerfile` and `entrypoint.sh` in this repo for specifics.

**Learn more:** [Hugging Face Spaces Docker Documentation](https://huggingface.co/docs/hub/spaces-docker-overview)

---

## 📂 Project Structure

```
local-ai-agent-rag/
├── .gitignore               # Excludes DB/env artifacts
├── app.py                   # Gradio entrypoint
├── Dockerfile               # Space deployment configuration
├── patristics.csv           # Retrieval database
├── pyproject.toml / uv.lock # Python dep mgmt (optional)
├── README.md
├── vector.py                # Embedding + ingest code
└── entrypoint.sh            # (if required for multi-process)
```

**.gitignore** should include:
```
chroma_langchain_db/
.venv/
*.pyc
__pycache__/
```

---

## 🧩 Design Notes

- UI and engine code separated for clarity
- LLM provider logic isolated for easy swap
- CSV/embedding scripts reproducible & idempotent
- Local by default, cloud-ready via Docker/Spaces

---

## ℹ️ Ollama Notes

- Ollama lets you run LLMs locally: privacy & performance
- Not natively supported on Spaces, so Docker deploy is required for hosting
- For Spaces, Ollama is installed in the container and run alongside Gradio

---

## 🗒️ Changelog

- Refactored: renamed `main.py` → `app.py`
- Updated: UI theme to Glass (via Gradio)
- Revised: `README.md` for Docker Spaces instructions
- Added: Pandas for CSV handling
- Improved: Reference extraction for church father texts in RAG agent

---

## 👾 How to Run Locally

```bash
python app.py
```
or
```bash
uv run python app.py
```

---

## 🙌 Dependency Management

Supports both **uv** and **pip**:
- Use `uv add` / `uv sync` for modern deps, or `pip install` / `pip freeze` as needed.

---

## 🛠️ Docker Deploy (Spaces)

- Make sure `app.py`, `Dockerfile`, [optional] `entrypoint.sh`, and `patristics.csv` are in root
- Push to a Hugging Face Spaces repo
- The environment will be built per your Docker config

---