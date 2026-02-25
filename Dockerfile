FROM python:3.11-slim

# Install minimal runtime dependencies for Ollama and uv
RUN apt-get update && \
    apt-get install -y curl zstd && \
    rm -rf /var/lib/apt/lists/*

# Download and install the prebuilt uv binary
RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz | tar xz
RUN mv uv*/uv /usr/local/bin/uv && chmod +x /usr/local/bin/uv

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

WORKDIR /workspace

# Copy all project files, including pyproject.toml, code, and entrypoint
COPY . .

# Ensure entrypoint.sh is executable
RUN chmod +x entrypoint.sh

# Optional: Output uv version for build logs
RUN uv --version

# Install all Python project dependencies into a .venv using uv (with pyproject.toml)
RUN uv sync

# Expose the web ports Gradio and Ollama will use
EXPOSE 7860 11434

# Start everything: activates venv, launches Ollama and app
CMD ["./entrypoint.sh"]