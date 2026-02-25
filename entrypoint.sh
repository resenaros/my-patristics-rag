#!/bin/bash
set -e

# Activate the Python virtual environment created by uv
source /workspace/.venv/bin/activate

# Start Ollama in the background
ollama serve &

# Wait until Ollama server is ready before pulling models
TRIES=0
until curl -s http://localhost:11434/api/status >/dev/null || [ $TRIES -ge 30 ]; do
  echo "Waiting for Ollama server to be available..."
  sleep 1
  TRIES=$((TRIES+1))
done

# Pull required models
ollama pull phi3:mini
ollama pull nomic-embed-text

# Start your Gradio RAG app
exec python app.py