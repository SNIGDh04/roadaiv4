# ROADAI v2 | High-Performance Cloud Dockerfile
# Optimized for Render, Railway, and DigitalOcean (Vanilla V2 Architecture)

FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (OpenCV & Video Processing requirements)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project code
# Includes /frontend (Vanilla HTML/JS), /backend, /models, /config
COPY . .

# Create persistent directories and set permissions
RUN mkdir -p uploads outputs/reports config models/custom models/runtime
RUN chmod -R 777 /app

# Port configuration (Standard Render/Cloud port)
EXPOSE 10000

# Start the FastAPI engine
# Note: Root index.html is served from /frontend via backend.main
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1"]
