@echo off
echo Starting English to Hindi Speech Translator...
echo.

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.10+ and add it to your PATH
    pause
    exit /b 1
)

REM Check if virtual environment exists
if exist venv (
    echo Activating virtual environment...
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment found. Installing dependencies globally...
)

REM Install/update requirements
echo Installing/updating dependencies...
pip install -r requirements.txt

REM Create uploads directory if it doesn't exist
if not exist uploads mkdir uploads

REM Start the application
echo.
echo Starting Flask application...
echo Access the app at: http://localhost:5000
echo Press Ctrl+C to stop the server
echo.

python app.py

pause