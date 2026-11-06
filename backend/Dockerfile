# ==========================================
# Backend - Multistage Dockerfile
# ==========================================

# Stage 1: Build virtual environment with dependencies
FROM python:3.12-slim AS builder

WORKDIR /app

# Install build dependencies for compiling Python extensions
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install python dependencies into virtualenv
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime image
FROM python:3.12-slim AS runner

WORKDIR /app

# Install runtime system libraries and curl for healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    libpq5 \
 && rm -rf /var/lib/apt/lists/*

# Copy installed virtual environment from builder stage
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Install Playwright chromium browser & dependencies for screenshots
RUN playwright install --with-deps chromium && \
    rm -rf /var/lib/apt/lists/*

# Copy application source code
COPY . /app

# Ensure runtime directories exist and seed existing screenshots
RUN mkdir -p /app/uploads /public/screenshots && \
    cp -r /app/uploads/screenshots/* /public/screenshots/ 2>/dev/null || true

# Expose backend API port
EXPOSE 8000

# Health check against /api/health endpoint
HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/api/health || exit 1

# Start FastAPI server using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
