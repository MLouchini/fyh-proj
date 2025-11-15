#!/bin/bash

echo "🎓 BuddyBud Setup Script"
echo "======================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo "✅ Dependencies installed"
echo ""

# Run migrations
echo "🗄️  Running database migrations..."
python3 manage.py makemigrations
python3 manage.py migrate

if [ $? -ne 0 ]; then
    echo "❌ Failed to run migrations"
    exit 1
fi

echo "✅ Database migrations complete"
echo ""

# Create superuser
echo "👤 Create a teacher account (superuser)"
echo "You'll need this to log in as a teacher"
python3 manage.py createsuperuser

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 To start the server, run:"
echo "   python3 manage.py runserver"
echo ""
echo "📱 Then visit:"
echo "   Student portal: http://localhost:8000/student/"
echo "   Teacher portal: http://localhost:8000/teacher/login/"
echo ""

