@echo off
echo ========================================================
echo  Starting SocialSense: Customer Feedback Analytics App
echo ========================================================
echo.

IF EXIST "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
) ELSE (
    echo [INFO] Virtual environment not found. Using system python...
)

echo Starting Streamlit Dashboard...
streamlit run app.py
pause
