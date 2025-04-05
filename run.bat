@echo off
echo Zenkai IMP Dataset Preparation Tool
echo ==================================

:: Check if config.json exists
if not exist config.json (
    echo Warning: config.json not found in the current directory.
    echo Creating a sample config.json file...
    
    echo { > config.json
    echo   "base_path": "C:/path/to/your/data/folder" >> config.json
    echo } >> config.json
    
    echo Sample config.json created. Please edit it with your actual data path.
    echo.
    pause
    exit /b 1
)

:: Run the main script
echo Running Zenkai IMP Dataset Preparation Tool...
echo.
python main.py %*

:: Check for errors
if %errorlevel% neq 0 (
    echo.
    echo Execution failed. Please check the error messages above.
    pause
    exit /b %errorlevel%
)

echo.
echo Processing complete.
pause
