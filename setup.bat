@echo off
setlocal
echo 🚀 ROADAI v4.0 — Windows Setup Sequence
echo ========================================

:: 1. Create Directories
echo 📁 Creating project directories...
if not exist "uploads" mkdir uploads
if not exist "outputs" mkdir outputs
if not exist "outputs\reports" mkdir outputs/reports
if not exist "config" mkdir config
if not exist "models\custom" mkdir models\custom
if not exist "models\runtime" mkdir models\runtime
if not exist "models\candidates" mkdir models\candidates

:: 2. Python Virtual Environment
echo 🐍 Setting up Python Virtual Environment...
if not exist "venv" (
    python -m venv venv
    echo ✅ Created 'venv'
) else (
    echo ℹ️ 'venv' already exists.
)

:: Activate and install requirements
echo 📦 Installing backend dependencies...
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
if %ERRORLEVEL% neq 0 (
    echo ❌ ERROR: Failed to install Python dependencies.
    pause
    exit /b %ERRORLEVEL%
)

:: 3. Frontend Dependencies
echo 🎨 Setting up Frontend UI...
cd frontend
if not exist "node_modules" (
    echo 📦 Installing Node modules (this may take a few minutes)...
    call npm install
) else (
    echo ℹ️ Node modules already installed.
)
cd ..

echo ========================================
echo ✅ Setup Complete! 
echo 💡 Use 'start.bat' to launch the platform.
pause
