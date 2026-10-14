@echo off
echo ========================================================
echo  Generating SocialSense Presentation in PDF Format
echo ========================================================
echo.

IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

python generate_pdf.py
echo.
echo PDF presentation generated at:
echo presentation\Social_Media_Sentiment_Topic_Analysis_Presentation.pdf
echo.
pause
