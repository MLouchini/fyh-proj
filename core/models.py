from django.db import models
from django.contrib.auth.models import User


class Homework(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='homeworks')
    code = models.CharField(max_length=20, unique=True, db_index=True)
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    due_date = models.DateField()
    total_marks = models.IntegerField()
    num_questions = models.IntegerField()
    instructions = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.title} ({self.code})"


class HomeworkFile(models.Model):
    FILE_TYPES = [
        ('questions', 'Questions'),
        ('mark_scheme', 'Mark Scheme'),
        ('model_answers', 'Model Answers'),
        ('textbook', 'Textbook'),
    ]
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='files')
    file_type = models.CharField(max_length=20, choices=FILE_TYPES)
    file = models.FileField(upload_to='homework_files/')
    file_name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.homework.code} - {self.file_type}"


class Submission(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='submissions')
    student_name = models.CharField(max_length=200)
    answer_file = models.FileField(upload_to='submissions/', blank=True, null=True)
    answer_text = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    written_score = models.IntegerField(default=0)
    interview_score = models.IntegerField(default=0)
    overall_score = models.IntegerField(default=0)
    
    # Overall feedback
    overall_strengths = models.TextField(blank=True)
    overall_improvements = models.TextField(blank=True)
    analysis_completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.homework.code}"


class QuestionFeedback(models.Model):
    """Stores detailed feedback for each question in a submission"""
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE, related_name='question_feedbacks')
    question_number = models.IntegerField()
    question_title = models.CharField(max_length=200)
    marks_awarded = models.IntegerField()
    marks_total = models.IntegerField()
    percentage = models.IntegerField()
    
    # Detailed feedback
    strengths = models.TextField()  # JSON array of strength points
    improvements = models.TextField()  # JSON array of improvement points
    detailed_analysis = models.TextField(blank=True)  # AI-generated detailed analysis
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question_number']
        unique_together = ['submission', 'question_number']

    def __str__(self):
        return f"{self.submission.student_name} - Q{self.question_number}"


class InterviewSession(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name='interview')
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    duration_seconds = models.IntegerField(default=0)
    video_url = models.CharField(max_length=500, blank=True)
    recording = models.FileField(upload_to='interview_recordings/', blank=True, null=True)
    transcription = models.TextField(blank=True, null=True)  # NEW: Speech-to-text transcription
    status = models.CharField(max_length=20, default='pending')
    
    # Interview analysis
    problem_solving_score = models.IntegerField(default=0)  # Out of 100
    conceptual_understanding_score = models.IntegerField(default=0)  # Out of 100
    creative_application_score = models.IntegerField(default=0)  # Out of 100
    
    strong_moments = models.TextField(blank=True)  # JSON array
    development_areas = models.TextField(blank=True)  # JSON array
    overall_analysis = models.TextField(blank=True)

    def __str__(self):
        return f"Interview - {self.submission.student_name}"


class InterviewQuestion(models.Model):
    """Stores individual interview questions and responses"""
    interview = models.ForeignKey(InterviewSession, on_delete=models.CASCADE, related_name='questions')
    question_number = models.IntegerField()
    question_type = models.CharField(max_length=50)  # process, concept, application, reflection
    question_text = models.TextField()
    
    # Would store transcription in production
    response_quality = models.IntegerField(default=0)  # Out of 100
    response_notes = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question_number']

    def __str__(self):
        return f"Q{self.question_number} - {self.interview.submission.student_name}"


class StudyPlan(models.Model):
    """Personalized study plan generated after complete analysis"""
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, related_name='study_plan')
    
    # Priority focus areas (JSON)
    priority_topics = models.TextField()  # JSON array of {topic, priority, score, actions}
    
    # Strengths to maintain
    strength_topics = models.TextField()  # JSON array
    
    # Learning insights
    written_vs_verbal_analysis = models.TextField()
    learning_style_insights = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Study Plan - {self.submission.student_name}"
