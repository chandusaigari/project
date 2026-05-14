# -------- Stage 1: Builder --------
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# -------- Stage 2: Runtime --------
FROM python:3.10-slim

WORKDIR /app

# Create non-root user
RUN useradd -m appuser

# Copy installed dependencies from builder
COPY --from=builder /root/.local /home/appuser/.local

# Copy application code
COPY app.py .

# Set permissions
RUN chown -R appuser:appuser /app
USER appuser

ENV PATH=/home/appuser/.local/bin:$PATH

EXPOSE 5000

CMD ["python", "app.py"]