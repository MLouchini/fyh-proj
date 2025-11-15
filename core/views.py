from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils import timezone
from django.db import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.base import ContentFile
from .models import (
    Homework, HomeworkFile, Submission, InterviewSession,
    QuestionFeedback, InterviewQuestion, StudyPlan
)
from .ai_service import AIFeedbackService
from .transcription_service import TranscriptionService
import random
import string
import json
import os

# Initialize AI service on module load
try:
    ai_service = AIFeedbackService()
except Exception as e:
    print(f"\n{'='*80}")
    print(f"⚠️  AI SERVICE INITIALIZATION FAILED")
    print(f"{'='*80}")
    print(f"{e}")
    print(f"{'='*80}\n")
    ai_service = None

# Initialize transcription service on module load  
try:
    transcription_service = TranscriptionService()
except Exception as e:
    print(f"\n{'='*80}")
    print(f"⚠️  TRANSCRIPTION SERVICE INITIALIZATION FAILED")
    print(f"{'='*80}")
    print(f"{e}")
    print(f"{'='*80}\n")
    transcription_service = None

# Home/Landing
def home(request):
    return render(request, 'home.html')

# Student Views
def student_home(request):
    return render(request, 'student/home.html')

def student_code_entry(request):
    if request.method == 'POST':
        code = request.POST.get('code', '').strip().upper()
        
        # VALIDATION: Code format
        if not code:
            messages.error(request, 'Please enter a homework code.')
            return render(request, 'student/code_entry.html')
        
        if len(code) < 10:  # Minimum length check
            messages.error(request, 'Invalid homework code format.')
            return render(request, 'student/code_entry.html')
        
        try:
            homework = Homework.objects.get(code=code, status='active')
            
            # Check if homework is past due (optional warning)
            if homework.due_date < timezone.now().date():
                messages.warning(request, 'Note: This homework is past the due date.')
            
            request.session['homework_id'] = homework.id
            return redirect('student_upload')
        except Homework.DoesNotExist:
            messages.error(request, 'Invalid homework code or homework is no longer active.')
    return render(request, 'student/code_entry.html')

def student_upload(request):
    homework_id = request.session.get('homework_id')
    if not homework_id:
        return redirect('student_code_entry')
    
    homework = get_object_or_404(Homework, id=homework_id)
    
    if request.method == 'POST':
        student_name = request.POST.get('student_name', '').strip()
        answer_text = request.POST.get('answer_text', '').strip()
        answer_file = request.FILES.get('answer_file')
        
        # VALIDATION: Student name is required
        if not student_name:
            messages.error(request, 'Please enter your name.')
            return render(request, 'student/upload.html', {'homework': homework})
        
        # VALIDATION: Must provide either answer text OR file
        if not answer_text and not answer_file:
            messages.error(request, 'Please provide your answer (either type it or upload a file).')
            return render(request, 'student/upload.html', {'homework': homework})
        
        # VALIDATION: File type and size checks
        if answer_file:
            # Check file extension
            allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.docx', '.doc', '.txt']
            file_ext = answer_file.name[answer_file.name.rfind('.'):].lower() if '.' in answer_file.name else ''
            if file_ext not in allowed_extensions:
                messages.error(request, f'Invalid file type. Allowed: {", ".join(allowed_extensions)}')
                return render(request, 'student/upload.html', {'homework': homework})
            
            # Check file size (max 10MB)
            max_size = 10 * 1024 * 1024  # 10MB in bytes
            if answer_file.size > max_size:
                messages.error(request, 'File too large. Maximum size is 10MB.')
                return render(request, 'student/upload.html', {'homework': homework})
        
        submission = Submission.objects.create(
            homework=homework,
            student_name=student_name,
            answer_text=answer_text,
            answer_file=answer_file,
            status='analyzing'
        )
        
        request.session['submission_id'] = submission.id
        return redirect('student_review_progress')
    
    return render(request, 'student/upload.html', {'homework': homework})

def student_review_progress(request):
    submission_id = request.session.get('submission_id')
    if not submission_id:
        return redirect('student_code_entry')
    
    submission = get_object_or_404(Submission, id=submission_id)
    
    # Run AI analysis if not already done
    if submission.status == 'analyzing' and not submission.analysis_completed_at:
        try:
            # Prepare homework data for AI
            homework_data = {
                'subject': submission.homework.subject,
                'level': submission.homework.level,
                'title': submission.homework.title,
                'total_marks': submission.homework.total_marks,
                'num_questions': submission.homework.num_questions,
                'instructions': submission.homework.instructions,
            }
            
            # Get answer text (MUST have actual content - no placeholders)
            answer_text = submission.answer_text
            if not answer_text and submission.answer_file:
                # For file submissions, we need to extract text or inform AI about file
                # In production, you'd use OCR/PDF parsing here
                messages.error(request, 'File processing not yet implemented. Please type your answers in the text box.')
                submission.status = 'error'
                submission.save()
                return redirect('student_upload')
            
            if not answer_text:
                raise Exception("No answer text provided")
            
            # Run AI analysis - REQUIRED
            if not ai_service:
                raise Exception("AI service not initialized. Check OpenAI API key configuration.")
            
            feedback = ai_service.analyze_written_work(homework_data, answer_text)
            
            # Store overall feedback
            submission.written_score = feedback['overall_score']
            submission.overall_score = feedback['overall_score']
            submission.overall_strengths = json.dumps(feedback['overall_strengths'])
            submission.overall_improvements = json.dumps(feedback['overall_improvements'])
            submission.analysis_completed_at = timezone.now()
            submission.status = 'analyzed'
            submission.save()
            
            # Store question-level feedback
            for q_feedback in feedback.get('questions', []):
                QuestionFeedback.objects.create(
                    submission=submission,
                    question_number=q_feedback['number'],
                    question_title=q_feedback['title'],
                    marks_awarded=q_feedback['marks_awarded'],
                    marks_total=q_feedback['marks_total'],
                    percentage=q_feedback['percentage'],
                    strengths=json.dumps(q_feedback['strengths']),
                    improvements=json.dumps(q_feedback['improvements']),
                    detailed_analysis=q_feedback.get('detailed_analysis', '')
                )
        except Exception as e:
            print(f"[ERROR] Error during AI analysis: {e}")
            submission.status = 'error'
            submission.save()
            messages.error(request, f"AI analysis failed: {str(e)}")
            return redirect('student_code_entry')
    
    return render(request, 'student/review_progress.html', {'submission': submission})

def student_feedback(request):
    submission_id = request.session.get('submission_id')
    if not submission_id:
        return redirect('student_code_entry')
    
    submission = get_object_or_404(Submission, id=submission_id)
    
    # Get question feedbacks from database
    question_feedbacks = submission.question_feedbacks.all()
    
    # Parse JSON fields for template
    questions_feedback = []
    for qf in question_feedbacks:
        questions_feedback.append({
            'number': qf.question_number,
            'title': qf.question_title,
            'marks': qf.marks_awarded,
            'total': qf.marks_total,
            'percentage': qf.percentage,
            'strengths': json.loads(qf.strengths) if qf.strengths else [],
            'improvements': json.loads(qf.improvements) if qf.improvements else []
        })
    
    # Parse overall feedback
    overall_strengths = json.loads(submission.overall_strengths) if submission.overall_strengths else []
    overall_improvements = json.loads(submission.overall_improvements) if submission.overall_improvements else []
    
    context = {
        'submission': submission,
        'homework': submission.homework,
        'questions_feedback': questions_feedback,
        'overall_strengths': overall_strengths,
        'overall_improvements': overall_improvements,
    }
    
    return render(request, 'student/feedback.html', context)

def student_interview_prep(request):
    submission_id = request.session.get('submission_id')
    if not submission_id:
        return redirect('student_code_entry')
    
    submission = get_object_or_404(Submission, id=submission_id)
    
    if request.method == 'POST':
        # Get or create interview session (in case user went back/refreshed)
        interview, created = InterviewSession.objects.get_or_create(
            submission=submission,
            defaults={'status': 'in_progress'}
        )
        
        # If interview already exists, reset it for fresh start
        if not created:
            interview.status = 'in_progress'
            interview.completed_at = None
            interview.transcription = None
            interview.save()
            # Delete old questions
            interview.questions.all().delete()
        
        # Generate personalized interview questions using AI
        try:
            homework_data = {
                'subject': submission.homework.subject,
                'level': submission.homework.level,
                'title': submission.homework.title,
            }
            
            written_feedback = {
                'overall_improvements': json.loads(submission.overall_improvements) if submission.overall_improvements else []
            }
            
            # Generate AI questions - REQUIRED
            if not ai_service:
                raise Exception("AI service not initialized. Check OpenAI API key configuration.")
            
            questions = ai_service.generate_interview_questions(homework_data, written_feedback)
            
            # DEBUG: Log generated questions
            print(f"[DEBUG] AI generated {len(questions)} questions")
            for q in questions:
                print(f"[DEBUG] Q{q.get('number', '?')}: {q.get('question', '?')[:50]}...")
            
            # Store questions in database
            for q in questions:
                InterviewQuestion.objects.create(
                    interview=interview,
                    question_number=q['number'],
                    question_type=q['type'],
                    question_text=q['question']
                )
            
            print(f"[DEBUG] Stored {interview.questions.count()} questions in database")
        except Exception as e:
            print(f"[ERROR] Error generating questions: {e}")
            messages.error(request, f"Failed to generate interview questions: {str(e)}")
        
        return redirect('student_interview')
    
    return render(request, 'student/interview_prep.html', {'submission': submission})

def student_interview(request):
    submission_id = request.session.get('submission_id')
    if not submission_id:
        return redirect('student_code_entry')
    
    submission = get_object_or_404(Submission, id=submission_id)
    
    # MUST have interview session (created in prep step)
    try:
        interview = submission.interview
    except InterviewSession.DoesNotExist:
        messages.error(request, "No interview session found. Please start interview from prep page.")
        return redirect('student_interview_prep')
    
    # Get interview questions from database - REQUIRED
    db_questions = interview.questions.all().order_by('question_number')
    
    if not db_questions.exists():
        messages.error(request, "Interview questions not generated. Redirecting to prep...")
        return redirect('student_interview_prep')
    
    # Use questions from database
    interview_questions = [
        {
            'number': q.question_number,
            'type': q.question_type,
            'title': q.question_type.upper().replace('_', ' '),
            'question': q.question_text,
            'hints': ['Take your time', 'Explain in your own words']
        }
        for q in db_questions
    ]
    
    # DEBUG: Check for duplicate question numbers
    question_numbers = [q['number'] for q in interview_questions]
    print(f"[DEBUG] Question numbers: {question_numbers}")
    if len(question_numbers) != len(set(question_numbers)):
        print(f"[ERROR] DUPLICATE question numbers detected!")
        duplicates = [num for num in question_numbers if question_numbers.count(num) > 1]
        print(f"[ERROR] Duplicates: {set(duplicates)}")
    
    if request.method == 'POST':
        # Complete interview and run analysis
        # REFRESH interview from database to get recording saved via AJAX
        interview.refresh_from_db()
        
        interview.status = 'completed'
        interview.completed_at = timezone.now()
        interview.duration_seconds = (timezone.now() - interview.started_at).seconds
        interview.save()
        
        # TRANSCRIBE the interview recording to text
        transcription = None
        try:
            # Debug logging
            print(f"[DEBUG] Interview recording field: {interview.recording}")
            if interview.recording:
                print(f"[DEBUG] Recording path: {interview.recording.path}")
                print(f"[DEBUG] File exists: {os.path.exists(interview.recording.path)}")
            
            if interview.recording and os.path.exists(interview.recording.path):
                if not transcription_service:
                    raise Exception("Transcription service not initialized. Check HUGGINGFACE_API_KEY configuration.")
                
                print(f"[AUDIO] Transcribing interview recording...")
                print(f"[AUDIO] File: {interview.recording.path}")
                transcription = transcription_service.transcribe_audio(interview.recording.path)
                
                # Store transcription in database
                interview.transcription = transcription
                interview.save()
                print(f"[OK] Transcription saved: {len(transcription)} characters")
            else:
                raise Exception("No interview recording found to transcribe")
        except Exception as e:
            print(f"[ERROR] Transcription failed: {e}")
            submission.status = 'error'
            submission.save()
            messages.error(request, f"Failed to transcribe interview: {str(e)}")
            return redirect('student_code_entry')
        
        # Run AI analysis of interview using TRANSCRIPTION
        try:
            homework_data = {
                'subject': submission.homework.subject,
                'level': submission.homework.level,
            }
            
            # Run AI analysis - REQUIRED with transcription
            if not ai_service:
                raise Exception("AI service not initialized. Check OpenAI API key configuration.")
            
            analysis = ai_service.analyze_interview_performance(
                homework_data,
                submission.written_score,
                interview.duration_seconds,
                transcription=transcription  # Pass REAL transcription
            )
            
            # Store interview analysis
            interview.problem_solving_score = analysis['problem_solving_score']
            interview.conceptual_understanding_score = analysis['conceptual_understanding_score']
            interview.creative_application_score = analysis['creative_application_score']
            interview.strong_moments = json.dumps(analysis['strong_moments'])
            interview.development_areas = json.dumps(analysis['development_areas'])
            interview.overall_analysis = analysis['overall_analysis']
            interview.save()
            
            # Update submission scores
            submission.interview_score = analysis['interview_score']
            submission.overall_score = (submission.written_score + submission.interview_score) // 2
            submission.status = 'complete'
            submission.save()
            
        except Exception as e:
            print(f"[ERROR] Error analyzing interview: {e}")
            submission.status = 'error'
            submission.save()
            messages.error(request, f"Interview analysis failed: {str(e)}")
            return redirect('student_code_entry')
        
        # Generate study plan
        try:
            question_feedbacks = [
                {
                    'title': qf.question_title,
                    'percentage': qf.percentage,
                }
                for qf in submission.question_feedbacks.all()
            ]
            
            submission_data = {
                'written_score': submission.written_score,
                'interview_score': submission.interview_score,
            }
            
            interview_analysis = {
                'problem_solving_score': interview.problem_solving_score,
                'conceptual_understanding_score': interview.conceptual_understanding_score,
            }
            
            # Generate study plan - REQUIRED
            if not ai_service:
                raise Exception("AI service not initialized. Check OpenAI API key configuration.")
            
            study_plan_data = ai_service.generate_study_plan(
                submission_data,
                question_feedbacks,
                interview_analysis
            )
            
            # Store study plan
            StudyPlan.objects.create(
                submission=submission,
                priority_topics=json.dumps(study_plan_data['priority_topics']),
                strength_topics=json.dumps(study_plan_data['strength_topics']),
                written_vs_verbal_analysis=study_plan_data['written_vs_verbal_analysis'],
                learning_style_insights=study_plan_data['learning_style_insights']
            )
        except Exception as e:
            print(f"[ERROR] Error generating study plan: {e}")
            # Study plan is optional, continue without it
        
        return redirect('student_final_results')
    
    context = {
        'submission': submission,
        'questions': interview_questions,
    }
    
    return render(request, 'student/interview.html', context)

def student_final_results(request):
    submission_id = request.session.get('submission_id')
    if not submission_id:
        return redirect('student_code_entry')
    
    submission = get_object_or_404(Submission, id=submission_id)
    
    # Get all feedback data with parsed JSON
    question_feedbacks_parsed = []
    for qf in submission.question_feedbacks.all():
        question_feedbacks_parsed.append({
            'question_number': qf.question_number,
            'question_title': qf.question_title,
            'marks_awarded': qf.marks_awarded,
            'marks_total': qf.marks_total,
            'percentage': qf.percentage,
            'strengths': json.loads(qf.strengths) if qf.strengths else [],
            'improvements': json.loads(qf.improvements) if qf.improvements else [],
        })
    
    try:
        interview = submission.interview
        interview_data = {
            'problem_solving_score': interview.problem_solving_score,
            'conceptual_understanding_score': interview.conceptual_understanding_score,
            'creative_application_score': interview.creative_application_score,
            'strong_moments': json.loads(interview.strong_moments) if interview.strong_moments else [],
            'development_areas': json.loads(interview.development_areas) if interview.development_areas else [],
        }
    except InterviewSession.DoesNotExist:
        interview_data = None
    
    try:
        study_plan = submission.study_plan
        study_plan_data = {
            'priority_topics': json.loads(study_plan.priority_topics) if study_plan.priority_topics else [],
            'strength_topics': json.loads(study_plan.strength_topics) if study_plan.strength_topics else [],
            'written_vs_verbal_analysis': study_plan.written_vs_verbal_analysis,
            'learning_style_insights': study_plan.learning_style_insights,
        }
    except StudyPlan.DoesNotExist:
        study_plan_data = None
    
    context = {
        'submission': submission,
        'homework': submission.homework,
        'question_feedbacks': question_feedbacks_parsed,
        'interview_data': interview_data,
        'study_plan_data': study_plan_data,
    }
    
    return render(request, 'student/final_results.html', context)

def save_interview_recording(request):
    """Save video recording from interview session with validation"""
    if request.method == 'POST':
        try:
            submission_id = request.POST.get('submission_id')
            video_file = request.FILES.get('video')
            
            # VALIDATION: Required data
            if not submission_id or not video_file:
                return JsonResponse({'error': 'Missing submission ID or video file'}, status=400)
            
            submission = get_object_or_404(Submission, id=submission_id)
            
            # VALIDATION: Check if interview session exists
            try:
                interview = submission.interview
            except InterviewSession.DoesNotExist:
                return JsonResponse({'error': 'No interview session found. Please start interview first.'}, status=400)
            
            # VALIDATION: Check file type (must be video)
            if not video_file.content_type.startswith('video/'):
                return JsonResponse({'error': 'Invalid file type. Must be a video file.'}, status=400)
            
            # VALIDATION: Check file size (max 100MB for video)
            max_size = 100 * 1024 * 1024  # 100MB in bytes
            if video_file.size > max_size:
                return JsonResponse({'error': 'Video file too large. Maximum size is 100MB.'}, status=400)
            
            # VALIDATION: Minimum size check (at least 100KB)
            min_size = 100 * 1024  # 100KB
            if video_file.size < min_size:
                return JsonResponse({'error': 'Video too short. Please record a proper interview response.'}, status=400)
            
            # Save video file
            interview.recording.save(
                f'interview_{submission.id}_{timezone.now().strftime("%Y%m%d_%H%M%S")}.webm',
                video_file,
                save=True
            )
            
            return JsonResponse({'success': True, 'message': 'Recording saved successfully'})
            
        except Exception as e:
            print(f"[ERROR] Error saving recording: {e}")
            return JsonResponse({'error': f'Failed to save recording: {str(e)}'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Teacher Views
def teacher_login(request):
    # Skip login - redirect directly to dashboard
    return redirect('teacher_dashboard')

def teacher_dashboard(request):
    from django.contrib.auth.models import User
    
    # Get current teacher user (or create if none exists)
    # In production, this should be from request.user after proper authentication
    teacher_user = User.objects.filter(is_staff=True).first()
    if not teacher_user:
        # Create initial teacher if none exists
        teacher_user = User.objects.create_user(
            username='teacher',
            first_name='Teacher',
            last_name='Account',
            email='teacher@buddybud.com',
            is_staff=True
        )
    
    homeworks = Homework.objects.filter(teacher=teacher_user).order_by('-created_at')
    
    # Calculate stats
    total_students = Submission.objects.filter(homework__teacher=teacher_user).values('student_name').distinct().count()
    
    all_submissions = Submission.objects.filter(homework__teacher=teacher_user, status='complete')
    avg_score = all_submissions.aggregate(models.Avg('overall_score'))['overall_score__avg'] or 0
    
    total_possible = Submission.objects.filter(homework__teacher=teacher_user).count()
    completed = all_submissions.count()
    completion_rate = (completed / total_possible * 100) if total_possible > 0 else 0
    
    context = {
        'homeworks': homeworks,
        'total_students': total_students,
        'avg_score': int(avg_score),
        'completion_rate': int(completion_rate),
    }
    
    return render(request, 'teacher/dashboard.html', context)

def teacher_create_homework(request):
    from django.contrib.auth.models import User
    from datetime import datetime
    
    # Get current teacher user
    teacher_user = User.objects.filter(is_staff=True).first()
    if not teacher_user:
        teacher_user = User.objects.create_user(
            username='teacher',
            first_name='Teacher',
            last_name='Account',
            email='teacher@buddybud.com',
            is_staff=True
        )
    
    if request.method == 'POST':
        # VALIDATION: Required fields
        title = request.POST.get('title', '').strip()
        subject = request.POST.get('subject', '').strip()
        level = request.POST.get('level', '').strip()
        class_name = request.POST.get('class_name', '').strip()
        due_date = request.POST.get('due_date', '').strip()
        total_marks = request.POST.get('total_marks', '').strip()
        num_questions = request.POST.get('num_questions', '').strip()
        instructions = request.POST.get('instructions', '').strip()
        
        # Validate required fields
        if not all([title, subject, level, class_name, due_date, total_marks, num_questions]):
            messages.error(request, 'All fields are required.')
            return render(request, 'teacher/create_homework.html')
        
        # Validate numeric fields
        try:
            total_marks_int = int(total_marks)
            num_questions_int = int(num_questions)
            if total_marks_int <= 0 or num_questions_int <= 0:
                raise ValueError("Must be positive")
        except ValueError:
            messages.error(request, 'Total marks and number of questions must be positive integers.')
            return render(request, 'teacher/create_homework.html')
        
        # Validate due date format
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            messages.error(request, 'Invalid date format. Use YYYY-MM-DD.')
            return render(request, 'teacher/create_homework.html')
        
        # Generate unique code
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        code = f"{subject[:3].upper()}-{code[:4]}-{code[4:8]}"
        
        homework = Homework.objects.create(
            teacher=teacher_user,
            code=code,
            title=title,
            subject=subject,
            level=level,
            class_name=class_name,
            due_date=due_date,
            total_marks=total_marks_int,
            num_questions=num_questions_int,
            instructions=instructions,
            status='active'
        )
        
        # Handle file uploads with validation
        questions_file = request.FILES.get('questions_file')
        if questions_file:
            # Validate file type
            allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.docx', '.doc']
            file_ext = questions_file.name[questions_file.name.rfind('.'):].lower() if '.' in questions_file.name else ''
            if file_ext not in allowed_extensions:
                messages.error(request, f'Invalid questions file type. Allowed: {", ".join(allowed_extensions)}')
                homework.delete()  # Rollback
                return render(request, 'teacher/create_homework.html')
            
            # Validate file size (max 20MB for teacher uploads)
            max_size = 20 * 1024 * 1024
            if questions_file.size > max_size:
                messages.error(request, 'Questions file too large. Maximum size is 20MB.')
                homework.delete()  # Rollback
                return render(request, 'teacher/create_homework.html')
            
            HomeworkFile.objects.create(
                homework=homework,
                file_type='questions',
                file=questions_file,
                file_name=questions_file.name
            )
        
        mark_scheme_file = request.FILES.get('mark_scheme_file')
        if mark_scheme_file:
            # Validate file type
            allowed_extensions = ['.pdf', '.jpg', '.jpeg', '.png', '.docx', '.doc']
            file_ext = mark_scheme_file.name[mark_scheme_file.name.rfind('.'):].lower() if '.' in mark_scheme_file.name else ''
            if file_ext not in allowed_extensions:
                messages.error(request, f'Invalid mark scheme file type. Allowed: {", ".join(allowed_extensions)}')
                homework.delete()  # Rollback
                return render(request, 'teacher/create_homework.html')
            
            # Validate file size
            max_size = 20 * 1024 * 1024
            if mark_scheme_file.size > max_size:
                messages.error(request, 'Mark scheme file too large. Maximum size is 20MB.')
                homework.delete()  # Rollback
                return render(request, 'teacher/create_homework.html')
            
            HomeworkFile.objects.create(
                homework=homework,
                file_type='mark_scheme',
                file=mark_scheme_file,
                file_name=mark_scheme_file.name
            )
        
        return redirect('teacher_homework_created', homework_id=homework.id)
    
    return render(request, 'teacher/create_homework.html')

def teacher_homework_created(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)
    return render(request, 'teacher/homework_created.html', {'homework': homework})

def teacher_view_results(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)
    
    submissions = homework.submissions.all()
    completed_submissions = submissions.filter(status='complete')
    
    # Calculate stats
    avg_score = completed_submissions.aggregate(models.Avg('overall_score'))['overall_score__avg'] or 0
    completion_rate = (completed_submissions.count() / submissions.count() * 100) if submissions.count() > 0 else 0
    
    # Score distribution
    submissions_90_100 = completed_submissions.filter(overall_score__gte=90).count()
    submissions_80_89 = completed_submissions.filter(overall_score__gte=80, overall_score__lt=90).count()
    submissions_70_79 = completed_submissions.filter(overall_score__gte=70, overall_score__lt=80).count()
    submissions_60_69 = completed_submissions.filter(overall_score__gte=60, overall_score__lt=70).count()
    submissions_below_60 = completed_submissions.filter(overall_score__lt=60).count()
    
    # Interview insights
    higher_verbal = 0
    higher_written = 0
    consistent = 0
    
    for sub in completed_submissions:
        diff = abs(sub.written_score - sub.interview_score)
        if diff <= 5:
            consistent += 1
        elif sub.interview_score > sub.written_score:
            higher_verbal += 1
        else:
            higher_written += 1
    
    context = {
        'homework': homework,
        'avg_score': int(avg_score),
        'completion_rate': int(completion_rate),
        'submissions_90_100': submissions_90_100,
        'submissions_80_89': submissions_80_89,
        'submissions_70_79': submissions_70_79,
        'submissions_60_69': submissions_60_69,
        'submissions_below_60': submissions_below_60,
        'higher_verbal': higher_verbal,
        'higher_written': higher_written,
        'consistent': consistent,
    }
    
    return render(request, 'teacher/view_results.html', context)

def teacher_student_report(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    homework = submission.homework
    
    # Get question feedbacks
    question_feedbacks = submission.question_feedbacks.all()
    
    # Get interview data if exists
    try:
        interview = submission.interview
    except InterviewSession.DoesNotExist:
        interview = None
    
    context = {
        'submission': submission,
        'homework': homework,
        'question_feedbacks': question_feedbacks,
        'interview': interview,
    }
    
    return render(request, 'teacher/student_report.html', context)
