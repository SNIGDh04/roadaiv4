@echo off
setlocal
echo 🚀 ROADAI v4.0 — Windows Startup
echo ===================================

:: Ensure scripts find the right directory
cd /d "%~dp0"

:: 1. UI Selection Prompt
echo.
echo Select ROADAI UI Theme:
echo   1. Titanium (Current Premium Dark Mode)
echo   2. Sypher (New Light Mode Dashboard with OTP Login)
echo   3. Classic (Legacy UI)
set /p ui_choice="Enter choice [1-3] (Default: 1): "

if "%ui_choice%"=="2" (
    set UI_THEME=sypher
    echo 👉 Selected Theme: Sypher ^(Light^)
) else if "%ui_choice%"=="3" (
    set UI_THEME=classic
    echo 👉 Selected Theme: Classic
) else (
    set UI_THEME=titanium
    echo 👉 Selected Theme: Titanium ^(Dark^)
)

echo VITE_UI_THEME=%UI_THEME% > frontend\.env.local
echo.

:: 2. Start Backend in a new window
echo 🔧 Starting Backend API (FastAPI) on port 8000...
start "ROADAI Backend" cmd /c "call venv\Scripts\activate && python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000 --log-level info"

:: 2. Wait a few seconds for backend
echo ⏳ Warming up AI components...
timeout /t 5 /nobreak > nul

:: 3. Start Frontend in a new window
echo 🎨 Starting Frontend UI on port 5173...
cd frontend
start "ROADAI Frontend" cmd /c "npm run dev"
cd ..

echo ===================================
echo ✅ Services launched in separate windows.
echo 🌐 Dashboard:  http://localhost:5173
echo 📖 API Docs:   http://localhost:8000/docs
echo.
echo Close the separate command windows to stop the services.
pause
