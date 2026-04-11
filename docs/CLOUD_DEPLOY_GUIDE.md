# 🚀 ROADAI v4.0: Cloud Deployment Guide

This guide provides step-by-step instructions to deploy the **ROADAI Enterprise Platform** using MongoDB Atlas, Render, and Netlify.

---

## 🏗️ Architecture Overview
- **Database**: MongoDB Atlas (Cloud NoSQL)
- **Backend API**: Render (FastAPI + AI Engine)
- **Frontend UI**: Netlify (React + Vite)

---

## 🗄️ Phase 1: MongoDB Atlas (Database)

1. **Log in** to your [MongoDB Atlas Dashboard](https://cloud.mongodb.com/).
2. **Cluster Selection**: Choose your existing cluster.
3. **Network Access**:
   - Go to **Network Access** in the sidebar.
   - Click **Add IP Address**.
   - Select **Allow Access From Anywhere (0.0.0.0/0)**. *Required for Render and Netlify to connect.*
4. **Database Access**:
   - Create a user with **Read and Write to any database** permissions.
5. **Connection String**:
   - Click **Connect** on your cluster.
   - Select **Drivers** and choose **Python**.
   - Copy the SRV string (e.g., `mongodb+srv://<username>:<password>@cluster0.abc.mongodb.net/roadai`).
6. **Local Verification**:
   - Set your environment variable: `export MONGODB_URL="your_srv_string"`
   - Run: `python3 scripts/check_mongodb.py`

---

## ⚙️ Phase 2: Render (Backend)

1. **GitHub Connection**:
   - Log in to [Render](https://dashboard.render.com/).
   - Click **New +** > **Blueprint**.
   - Connect your GitHub repository.
2. **Deployment**:
   - Render will detect the `render.yaml` file automatically.
   - It will create a **Web Service** named `roadai-enterprise-api`.
3. **Environment Variables**:
   In the Render dashboard, go to **Environment** and set:
   - `MONGODB_URL`: Your verified Atlas SRV string.
   - `MONGODB_DB`: `roadai`
   - `CORS_ORIGINS`: `*` (or your Netlify URL after Phase 3).
4. **Weights Handling**:
   - The small `check_2.pt` (6MB) and `yolov8n.pt` are included in the repo. They will load on startup.

---

## 🌐 Phase 3: Netlify (Frontend)

1. **GitHub Connection**:
   - Log in to [Netlify](https://app.netlify.com/).
   - Click **Add new site** > **Import an existing project**.
   - Connect your GitHub repository.
2. **Build Settings**:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `dist`
3. **Environment Variables**:
   Go to **Site configuration** > **Environment variables**:
   - Create `VITE_API_BASE_URL` and set it to your **Render Web Service URL** (e.g., `https://roadai-api.onrender.com`).
4. **Deploy**:
   - Click **Deploy site**.

---

## ✅ Final Verification

1. Access your Netlify URL (e.g., `https://roadai-v4.netlify.app`).
2. Log in with `admin` / `admin123`.
3. Open the **Admin Panel** > **System Info** to verify the Backend API is responding.
4. Check the **Dashboard** to see live metrics fetched from MongoDB Atlas.

---

## 🆘 Troubleshooting
- **500 Errors**: Check the Render logs for Python exception traceback.
- **CORS Errors**: Ensure the Render `CORS_ORIGINS` variable includes your Netlify URL.
- **Login Stuck**: Ensure the `VITE_API_BASE_URL` on Netlify does NOT have a trailing slash.
