# 🚀 Quick Start Guide

## For Windows Users:

1. Double-click `setup.bat` or run in Command Prompt:
   ```
   setup.bat
   ```

2. Follow the prompts to create a teacher account

3. Start the server:
   ```
   python manage.py runserver
   ```

4. Open your browser:
   - Student: http://localhost:8000/student/
   - Teacher: http://localhost:8000/teacher/login/

## For Mac/Linux Users:

1. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

2. Follow the prompts to create a teacher account

3. Start the server:
   ```bash
   python3 manage.py runserver
   ```

4. Open your browser:
   - Student: http://localhost:8000/student/
   - Teacher: http://localhost:8000/teacher/login/

## Manual Setup (if scripts don't work):

```bash
# Install dependencies
pip install -r requirements.txt

# Setup database
python manage.py makemigrations
python manage.py migrate

# Create teacher account
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## 🎮 Try It Out!

### As a Student:
1. Go to http://localhost:8000/student/
2. Click "Enter Homework Code"
3. Use code: `PHY-2024-A3B7` (or any code from the teacher side)
4. Upload a file or type answers
5. Experience the AI review and interview flow!

### As a Teacher:
1. Go to http://localhost:8000/teacher/login/
2. Login with your superuser credentials
3. Click "Create New Homework"
4. Fill in details and upload files
5. Get a homework code to share with students
6. View submissions and analytics!

## 📸 Screenshots

### Student Experience:
- ✨ Beautiful landing page with animations
- 📝 Drag-and-drop file upload
- 💬 Interactive interview interface
- 📊 Detailed feedback with tabs

### Teacher Experience:
- 📊 Comprehensive dashboard
- 🎯 Multi-step homework creation with progress bar
- 📈 Class analytics and insights
- 🎥 Student interview recordings

## 🎨 Design Features

- **Modern Gradients**: Purple-to-blue backgrounds throughout
- **Smooth Animations**: Fade-ins, hover effects, transitions
- **Rounded Corners**: Everything has that modern, friendly feel
- **Inner Shadows**: Depth and dimension on cards
- **Subtle Glows**: Highlighting important elements
- **Progress Indicators**: Visual feedback on multi-step processes

## 💡 Tips

1. **For Best Experience**: Use Chrome or Edge browser
2. **Responsive**: Works on desktop and tablets
3. **Sample Data**: The app uses demo data for quick testing
4. **Customization**: Colors can be changed in `templates/base.html`

## 🐛 Troubleshooting

**Server won't start:**
- Make sure Python 3.8+ is installed
- Try `python3` instead of `python`
- Check if port 8000 is already in use

**Can't login as teacher:**
- Make sure you created a superuser
- Try creating one again: `python manage.py createsuperuser`

**Static files not loading:**
- Run: `python manage.py collectstatic`

## 🎯 Next Steps

1. Customize the color scheme
2. Add your own images to the placeholders
3. Integrate real AI APIs (OpenAI, Anthropic)
4. Implement actual video recording
5. Connect to your LMS

Enjoy! 🎉

