@echo off
echo ========================================================
echo  Generating SocialSense PowerPoint Presentation (.pptx)
echo ========================================================
echo.

IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python generate_presentation.py
echo.
echo Presentation saved in presentation/ directory.
pause
