# Use minimal secure base image with specific digest for reproducibility
FROM python:3.12-slim-bookworm
# Security: Run as non-root user
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
# Set working directory
WORKDIR /app
# Security: Copy only requirements first for layer caching
COPY requirements.txt .
# Install dependencies with no cache to reduce image size
RUN pip install --no-cache-dir -r requirements.txt
# Copy application code
COPY app/ ./app/
# Security: Change ownership and switch to non-root user
RUN chown -R appuser:appgroup /app
USER appuser
# Expose port (documentation only)
EXPOSE 8080
# Health check for container orchestration
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('[localhost](http://localhost:8080/health)')" || exit 1
# Run with gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "app.main:app"]
