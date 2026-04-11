# ROADAI v4.0 — Enterprise AI Road Analytics Platform 🛣️🤖

**ROADAI** is an advanced, full-stack intelligence platform designed for real-time road health monitoring, defect detection, and predictive maintenance. Version 4.0 (Enterprise Edition) transitions the platform to a modern **React + Vite** frontend and **MongoDB Atlas** cloud persistence.

---

## 🌟 Key Features

- **🚀 Modern React/Vite UI**: High-performance dashboard with "Titanium" dark theme, real-time metrics, and interactive map visualizations.
- **🧠 Deep Fusion Engine**: Synchronous multi-model inference combining **YOLOv8** (Defects), **DeepLabV3** (Layer Segmentation), and **MiDaS** (Depth Estimation).
- **📈 Predictive Analytics**: XGBoost-powered **Remaining Useful Life (RUL)** estimation for infrastructure lifecycle management.
- **🛰️ Geo-Persistence**: Integration with **MongoDB Atlas** for geospatial event tracking and maintenance segment aggregation.
- **📹 Universal Processing**: Support for high-res images, 4K video analysis, and low-latency **RTSP/Webcam** streams via WebSockets.
- **📱 Smart Alerts**: Automated **Twilio SMS** notifications for critical road failure detections.

---

## 📂 Project Structure

```text
/RoadAI_v2_GitHub
├── frontend/           # React 18 + Vite (Shadcn UI, Recharts, Framer Motion)
├── backend/            # FastAPI Microservices (Detection, Geo, Auth, Alerts)
├── models/             # AI Weight Management (Runtime and Candidate models)
├── docs/report/        # LaTeX Project Documentation & Reports
├── scripts/            # Training, Benchmarking, and Maintenance utilities
├── setup.sh            # Global environment provisioner
└── start.sh            # Dual-layer service orchestrator (Backend + Frontend)
```

---

## ⚡ Quick Start (Local Setup)

1. **Environment Provisioning**:
   Ensure you have Python 3.10+ and Node.js 18+ installed.
   ```bash
   bash setup.sh
   ```
   *This script handles system dependencies, Python venv, and NPM installation.*

2. **Configuration**:
   Copy `.env.example` to `.env` and populate your credentials:
   ```bash
   cp .env.example .env
   ```

3. **Launch Platform**:
   ```bash
   bash start.sh
   ```
   - **Dashboard**: `http://localhost:5173`
   - **API Documentation**: `http://localhost:8000/docs`

---

## 🛠️ Technology Stack

- **Frontend**: React 18, Vite, TypeScript, Tailwind CSS, Lucide, Framer Motion.
- **Backend**: Python 3.13, FastAPI, Uvicorn, Motor (Async MongoDB).
- **Core AI**: Ultralytics YOLOv8, PyTorch, Scikit-Learn, XGBoost.
- **Infrastructure**: MongoDB Atlas (Primary), Redis/Celery (Task Queue), Twilio (SMS).

---

## ☁️ Deployment Guide

### Backend (Render/Heroku)
- Connect repository and set the root directory to project root.
- Environment: Set all variables defined in `.env.example`.
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`

### Frontend (Netlify/Vercel)
- Base Directory: `frontend/`
- Build Command: `npm run build`
- Publish Directory: `frontend/dist/`
- Ensure the `VITE_API_BASE_URL` is set to your deployed backend.

---

Developed with ❤️ by the SNIGDHA & ROADAI Engineering Team.
