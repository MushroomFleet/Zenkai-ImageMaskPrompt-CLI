@echo off
echo Zenkai IMP Dataset Preparation Tool - Installation
echo ================================================

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Installation verification completed successfully.
echo Run 'run.bat' to start the Zenkai IMP Dataset Preparation Tool.
echo.
pause
