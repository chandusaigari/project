# =========================
# Stage 1 - Builder Stage
# =========================
FROM python:3.9-slim AS builder

# Set working directory
WORKDIR /app

# Copy requirements first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --user -r requirements.txt

# =========================
# Stage 2 - Production Stage
# =========================
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /root/.local /root/.local

# Copy project files
COPY . .

# Add local packages to PATH
ENV PATH=/root/.local/bin:$PATH

# Expose application port
EXPOSE 5000

# Start application
CMD ["python", "app.py"]
