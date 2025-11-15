@echo off
echo.
echo 🎓 BuddyBud Setup Script
echo =======================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python found
python --version
echo.

REM Install dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Run migrations
echo 🗄️  Running database migrations...
python manage.py makemigrations
python manage.py migrate

if errorlevel 1 (
    echo ❌ Failed to run migrations
    pause
    exit /b 1
)

echo ✅ Database migrations complete
echo.

REM Create superuser
echo 👤 Create a teacher account (superuser)
echo You'll need this to log in as a teacher
python manage.py createsuperuser

echo.
echo ✅ Setup complete!
echo.
echo 🚀 To start the server, run:
echo    python manage.py runserver
echo.
echo 📱 Then visit:
echo    Student portal: http://localhost:8000/student/
echo    Teacher portal: http://localhost:8000/teacher/login/
echo.
pause

