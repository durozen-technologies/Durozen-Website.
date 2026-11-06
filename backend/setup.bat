@echo off
setlocal
cd /d "%~dp0"

echo =======================================================
echo Setting up DUROZEN FastAPI Backend Environment
echo =======================================================

set PYTHON_CMD=python
if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
    set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
)

echo Using Python: %PYTHON_CMD%
"%PYTHON_CMD%" --version
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python not found. Please ensure Python 3.10+ is installed.
    pause
    exit /b 1
)

if not exist "venv" (
    echo Creating virtual environment in venv...
    "%PYTHON_CMD%" -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Upgrading pip and installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo =======================================================
echo Setup complete! You can now start the server with start.bat
echo =======================================================
pause

