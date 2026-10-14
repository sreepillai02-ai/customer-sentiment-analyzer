@echo off
setlocal enabledelayedexpansion

echo ========================================================
echo    SocialSense: Push Project to Your GitHub Account
echo ========================================================
echo.

:: Check if git is installed
where git >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git is not installed on this system.
    echo.
    echo Installing Git automatically using winget...
    winget install --id Git.Git -e --source winget
    echo.
    echo Git has been installed! Please close and re-open this window,
    echo or restart PowerShell to complete the setup.
    pause
    exit /b
)

echo [OK] Git is available!
echo.
echo --------------------------------------------------------
echo STEP 1: Create a repository on https://github.com/new
echo         (Leave all checkboxes UNCHECKED)
echo --------------------------------------------------------
echo.
set /p REPO_URL="STEP 2: Paste your GitHub repository URL here: "

if "%REPO_URL%"=="" (
    echo [ERROR] No URL entered. Please re-run and paste your repository URL.
    pause
    exit /b
)

echo.
echo Initializing Git and staging files...
if not exist ".git" (
    git init
)

git add .
git commit -m "Initial commit: Customer Feedback Sentiment Analyzer"
git branch -M main

:: Remove origin if already exists
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo.
echo Pushing code to GitHub...
echo (A browser window may open to ask you to sign in to GitHub)
git push -u origin main

echo.
if %ERRORLEVEL% EQU 0 (
    echo ========================================================
    echo    SUCCESS! Your project has been pushed to GitHub!
    echo ========================================================
) else (
    echo [INFO] If prompted, make sure you signed into your GitHub account.
)

echo.
pause
