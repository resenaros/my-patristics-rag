FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl zstd && \
    rm -rf /var/lib/apt/lists/*

# Install uv
RUN curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz | tar xz && \
    mv uv*/uv /usr/local/bin/uv && \
    chmod +x /usr/local/bin/uv

# Install Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh

# Preload models during build (cached in image, no pull on restart)
RUN ollama pull phi3:mini
RUN ollama pull nomic-embed-text

# Create non-root user (HF Spaces requirement)
RUN useradd -m -u 1000 appuser

WORKDIR /app

# Copy project files
COPY . .

# Make entrypoint executable and install dependencies
RUN chmod +x entrypoint.sh && \
    uv sync && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# Expose ports
EXPOSE 7860 11434

# Health check for HF Space status monitoring
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:7860/ || exit 1

# Start application
CMD ["./entrypoint.sh"]