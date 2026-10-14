@echo off
echo ========================================================
echo  Running SocialSense Automated Test Suite
echo ========================================================
echo.

IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python -m unittest discover tests
echo.
pause
