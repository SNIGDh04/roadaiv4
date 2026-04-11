#!/bin/bash
# ROADAI v4 — Enterprise Orchestrator
# Starts both FastAPI Backend (8000) and Vite Frontend (5173)

# 1. Cleanup existing ports to prevent "Address already in use"
echo "🔍 Clearing ports 8000 and 5173..."
fuser -k 8000/tcp 5173/tcp 2>/dev/null || true

# 2. Launch Backend (FastAPI)
echo "🚀 Starting ROADAI API (Port 8000)..."
export PORT=8000
export HOST=0.0.0.0
uvicorn backend.main:app --host $HOST --port $PORT --workers 1 &
BACKEND_PID=$!

# 3. Launch Frontend (Vite)
echo "🌐 Starting ROADAI UI (Port 5173)..."
if [ ! -d "frontend/node_modules" ]; then
    echo "⚠️  node_modules missing. Running npm install..."
    cd frontend && npm install && cd ..
fi

cd frontend
npm run dev -- --host 0.0.0.0 &
FRONTEND_PID=$!
cd ..

# 4. Cleanup logic for Ctrl+C
cleanup() {
    echo -e "\n🛑 Shutting down ROADAI Enterprise..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

trap cleanup SIGINT SIGTERM

echo "------------------------------------------"
echo "✅ ROADAI Enterprise is initializing..."
echo "🔗 Dashboard: http://localhost:5173"
echo "📖 API Docs:  http://localhost:8000/docs"
echo "------------------------------------------"

# Keep script running and wait for background processes
wait
