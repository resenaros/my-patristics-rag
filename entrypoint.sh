#!/bin/bash
set -e

# Activate Python virtual environment
source /app/.venv/bin/activate

# Start Ollama in background
ollama serve &

# Wait for Ollama to be ready (max 30 seconds)
TRIES=0
until curl -s http://localhost:11434/api/status >/dev/null || [ $TRIES -ge 30 ]; do
  echo "Waiting for Ollama server... ($TRIES/30)"
  sleep 1
  TRIES=$((TRIES+1))
done

echo "Ollama is ready!"

# Pull required models
ollama pull phi3:mini
ollama pull nomic-embed-text

# Start Gradio RAG app (models already preloaded in Dockerfile)
exec python app.py