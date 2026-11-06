@echo off
setlocal
cd /d "%~dp0"

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
    python run.py
) else (
    set PYTHON_CMD=python
    if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" (
        set "PYTHON_CMD=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
    )
    "%PYTHON_CMD%" run.py
)
pause

