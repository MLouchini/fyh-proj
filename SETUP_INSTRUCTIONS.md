# BuddyBud - Quick Setup Guide

## Prerequisites
- Python 3.12+
- pip

## Installation Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- Django 4.2.7
- Pillow 10.1.0
- python-dotenv 1.0.0
- **openai 1.54.3** (OpenAI GPT-4 client)

### 2. Configure Environment Variables

**Create `.env` file from template:**
```bash
# Copy the example file
cp .env.example .env

# Or on Windows
copy .env.example .env
```

**Edit `.env` file and set your OpenAI API key:**
```bash
OPENAI_API_KEY=sk-proj-your-actual-api-key-here
```

Get your API key from: https://platform.openai.com/api-keys

**Other optional settings in `.env`:**
- `SECRET_KEY` - Django secret key (change in production)
- `DEBUG` - Set to `False` in production
- `OPENAI_MODEL` - Default: gpt-4o-mini
- `OPENAI_MAX_TOKENS` - Default: 2000

### 3. Run Database Migrations
```bash
python manage.py migrate
```

###4. Create Superuser (Optional - for admin access)
```bash
python manage.py createsuperuser
```

### 5. Generate Sample Data (Optional)
```bash
python create_sample_data.py
```

This creates:
- Demo teacher account
- 3 sample homeworks with codes
- 10 sample student submissions with AI-generated feedback

### 6. Run Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000/

---

## Quick Test Flow

### Teacher Flow:
1. Go to http://localhost:8000/teacher/dashboard/
2. Click "Create Homework"
3. Fill in details (subject, level, questions, etc.)
4. Note the generated **homework code** (e.g., `PHY-2024-A3B7`)

### Student Flow:
1. Go to http://localhost:8000/student/
2. Click "Enter Homework Code"
3. Enter the code from teacher
4. Upload/type your answer
5. **AI analyzes your work** (takes ~5-10 seconds)
6. Review detailed per-question feedback
7. Complete interview (camera required)
8. **AI analyzes interview** performance
9. Get complete results with study plan

---

## Sample Homework Codes (if you ran create_sample_data.py)

Check your terminal output after running `create_sample_data.py` - it will show codes like:
- `PHY-2024-XXXX`
- `CHE-2024-XXXX`
- `MAT-2024-XXXX`

Or check the teacher dashboard at: http://localhost:8000/teacher/dashboard/

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install openai==1.54.3
```

### "Invalid API key"
- Check your API key is correct
- Ensure environment variable is set properly
- Restart terminal/server after setting environment variables

### System shows "AI SERVICE INITIALIZATION FAILED"
- **API key not configured**: 
  1. Copy `.env.example` to `.env`
  2. Edit `.env` and set `OPENAI_API_KEY=sk-proj-your-key`
  3. Restart the server
- **Invalid API key**: Check your key in `.env` is correct
- **.env file missing**: Make sure `.env` exists in project root

### System shows errors during submission
- **AI service not initialized**: Check `.env` file has valid `OPENAI_API_KEY`
- **OpenAI API errors**: Check account has credits
- **Rate limits**: Wait a few minutes and try again
- **Module errors**: Run `pip install -r requirements.txt`

### "No migrations to apply"
Database is already up to date. Skip this step.

---

## File Structure

```
buddybud/
├── buddybud/                 # Django project settings
│   ├── settings.py          # Configuration (includes OPENAI_API_KEY)
│   └── urls.py
├── core/                    # Main app
│   ├── models.py           # Database models (Homework, Submission, QuestionFeedback, etc.)
│   ├── views.py            # View logic with AI integration
│   ├── ai_service.py       # OpenAI GPT-4 integration
│   ├── admin.py            # Django admin configuration
│   └── urls.py
├── templates/              # HTML templates
│   ├── base.html          # Base template with barebones CSS
│   ├── home.html
│   ├── student/           # Student flow templates
│   └── teacher/           # Teacher flow templates
├── media/                 # Uploaded files (submissions, recordings)
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
├── create_sample_data.py # Sample data generator
├── DATABASE_AND_AI_IMPLEMENTATION.md  # Full technical documentation
└── SETUP_INSTRUCTIONS.md  # This file
```

---

## Key URLs

- **Homepage**: http://localhost:8000/
- **Student Portal**: http://localhost:8000/student/
- **Teacher Dashboard**: http://localhost:8000/teacher/dashboard/
- **Admin Panel**: http://localhost:8000/admin/ (requires superuser)

---

## Important Notes

### AI Service
- Uses `gpt-4o-mini` model (cost-effective)
- **NO FALLBACK DATA** - Requires valid API key
- **LIVE DATA ONLY** - All responses from OpenAI GPT-4
- All AI responses stored in database permanently
- Clear error messages if API key missing/invalid

### Video Recording
- Requires camera/microphone permissions
- Recordings saved to `media/interview_recordings/`
- Format: WebM

### Database
- SQLite (default)
- All feedback stored permanently
- No placeholder data

---

## Next Steps

1. **Try the flow**: Create homework → Submit as student → See AI feedback
2. **Explore admin panel**: http://localhost:8000/admin/
3. **Check database**: View QuestionFeedback, InterviewSession, StudyPlan records
4. **Read full docs**: DATABASE_AND_AI_IMPLEMENTATION.md

---

## Support & Documentation

- **Full Implementation Docs**: `DATABASE_AND_AI_IMPLEMENTATION.md`
- **OpenAI API Docs**: https://platform.openai.com/docs/guides/text
- **Django Docs**: https://docs.djangoproject.com/

---

## Production Deployment

Before deploying to production:

1. Set `DEBUG = False` in settings.py
2. Configure proper database (PostgreSQL recommended)
3. Set up file storage (S3, Cloud Storage)
4. Enable HTTPS/SSL
5. Set strong SECRET_KEY
6. Configure ALLOWED_HOSTS
7. Set up proper logging
8. Monitor OpenAI API usage and costs

---

Happy teaching! 🎓

