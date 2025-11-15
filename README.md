# BuddyBud - AI-Powered Educational Platform

> **Production-Ready**: Database-driven, OpenAI GPT-4 integrated, NO placeholder data

## Overview

BuddyBud is an educational platform that uses AI to provide personalized homework feedback through:
- **Written Analysis**: Detailed per-question feedback
- **Video Interviews**: Understanding verification via recorded sessions
- **Study Plans**: Personalized learning recommendations

## Key Features
✅ **OpenAI GPT-4 Integration** - Real AI-generated feedback
✅ **Per-Question Breakdown** - Granular analysis storage
✅ **Video Recording** - Interview sessions saved
✅ **Personalized Learning** - AI-generated study plans
✅ **Teacher Analytics** - Class-wide performance insights
✅ **Barebones UI** - Clean, functional design

## Tech Stack

- **Backend**: Django 4.2.7 (Python)
- **AI**: OpenAI GPT-4o-mini
- **Database**: SQLite (default) / PostgreSQL (production)
- **Frontend**: Pure HTML, CSS, JavaScript
- **Video**: MediaRecorder API (WebRTC)

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Environment Variables
```bash
# Copy .env template
cp .env.example .env

# Edit .env and set your API key
# OPENAI_API_KEY=sk-proj-your-actual-key
```

Get API key from: https://platform.openai.com/api-keys

### 3. Setup Database
```bash
python manage.py migrate
python create_sample_data.py
```

### 4. Run Server
```bash
python manage.py runserver
```

Visit: http://localhost:8000/

## Documentation

- **Setup Guide**: `SETUP_INSTRUCTIONS.md` - Installation & configuration
- **Technical Docs**: `DATABASE_AND_AI_IMPLEMENTATION.md` - Full architecture
- **Placeholder Reference**: `PLACEHOLDER_DATA_REFERENCE.txt` - Removed fallback data

## Architecture

### Database Models (7 tables)

1. **Homework** - Teacher assignments
2. **HomeworkFile** - Uploaded materials
3. **Submission** - Student work + analysis
4. **QuestionFeedback** - Per-question breakdown
5. **InterviewSession** - Video interviews + AI scores
6. **InterviewQuestion** - Dynamically generated questions
7. **StudyPlan** - Personalized recommendations

### AI Integration Points

1. **Written Analysis** (`analyze_written_work`)
   - Input: Student answers + homework context
   - Output: Overall score + per-question feedback
   - Storage: Submission + QuestionFeedback records

2. **Question Generation** (`generate_interview_questions`)
   - Input: Weak areas from written work
   - Output: 5 personalized interview questions
   - Storage: InterviewQuestion records

3. **Interview Analysis** (`analyze_interview_performance`)
   - Input: Written score + interview duration
   - Output: Multi-dimensional scores + insights
   - Storage: InterviewSession fields

4. **Study Plan** (`generate_study_plan`)
   - Input: Complete performance data
   - Output: Priority topics + action items
   - Storage: StudyPlan record

## Student Flow

1. Enter homework code
2. Upload/type answers
3. **AI analyzes work** (~5-10 seconds)
4. Review per-question feedback
5. Complete video interview (5 questions)
6. **AI analyzes interview**
7. Receive complete results + study plan

## Teacher Flow

1. Create homework (code auto-generated)
2. Share code with students
3. View submissions as they arrive
4. Review class analytics (tabs):
   - Submissions list
   - Class analytics (score distribution)
   - Topic performance (per-question)
   - Interview insights (written vs verbal)
5. View individual student reports

## Cost Optimization

- **Model**: `gpt-4o-mini` (cost-effective GPT-4)
- **Token Limits**: 
  - Written analysis: 2000 tokens
  - Question generation: 1000 tokens
  - Interview analysis: 500 tokens
  - Study plan: 1000 tokens
- **Estimated Cost**: ~$0.05-0.10 per submission

## Production Deployment

Before deploying:

- [ ] Set real `OPENAI_API_KEY`
- [ ] Configure PostgreSQL
- [ ] Set up S3/Cloud Storage for files
- [ ] Enable HTTPS/SSL
- [ ] Set `DEBUG = False`
- [ ] Configure `ALLOWED_HOSTS`
- [ ] Set strong `SECRET_KEY`
- [ ] Set up logging
- [ ] Monitor API usage/costs

## Testing

1. Run server: `python manage.py runserver`
2. Teacher: Create homework at `/teacher/dashboard/`
3. Student: Use code at `/student/`
4. Check database: Visit `/admin/` (create superuser first)

Sample code (after running `create_sample_data.py`): `PHY-2024-A3B7`

## Error Handling

### "AI SERVICE INITIALIZATION FAILED"
→ Configure `OPENAI_API_KEY` and restart server

### "AI analysis failed"
→ Check API key is valid and account has credits

### Interview questions not generated
→ Restart from submission step

## Important Notes

⚠️ **NO FALLBACK DATA**: System requires valid OpenAI API key
✅ **LIVE DATA ONLY**: All feedback is AI-generated
✅ **PRODUCTION READY**: Complete database persistence
✅ **ERROR HANDLING**: Clear messages when AI fails

## File Structure

```
buddybud/
├── core/
│   ├── models.py          # 7 database models
│   ├── views.py           # Views with AI integration
│   ├── ai_service.py      # OpenAI GPT-4 client
│   └── admin.py           # Django admin
├── templates/
│   ├── base.html          # Barebones CSS
│   ├── student/           # Student flow
│   └── teacher/           # Teacher flow
├── media/                 # Uploads (submissions, recordings)
├── create_sample_data.py  # Sample data generator
├── requirements.txt       # Dependencies
└── *.md                   # Documentation
```

## License

MIT

## Support

- **Setup Issues**: See `SETUP_INSTRUCTIONS.md`
- **Technical Details**: See `DATABASE_AND_AI_IMPLEMENTATION.md`
- **OpenAI Docs**: https://platform.openai.com/docs

---

**Status**: Production-ready, fully functional with valid OpenAI API key
