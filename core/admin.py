from django.contrib import admin
from .models import (
    Homework, HomeworkFile, Submission, InterviewSession,
    QuestionFeedback, InterviewQuestion, StudyPlan
)

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'subject', 'level', 'teacher', 'due_date', 'status']
    search_fields = ['code', 'title', 'subject']
    list_filter = ['status', 'subject', 'level']

@admin.register(HomeworkFile)
class HomeworkFileAdmin(admin.ModelAdmin):
    list_display = ['homework', 'file_type', 'file_name', 'uploaded_at']
    list_filter = ['file_type']

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ['student_name', 'homework', 'written_score', 'interview_score', 'overall_score', 'status', 'submitted_at']
    search_fields = ['student_name', 'homework__code']
    list_filter = ['status', 'homework']
    readonly_fields = ['submitted_at', 'analysis_completed_at']

@admin.register(QuestionFeedback)
class QuestionFeedbackAdmin(admin.ModelAdmin):
    list_display = ['submission', 'question_number', 'question_title', 'marks_awarded', 'marks_total', 'percentage']
    list_filter = ['submission__homework']

@admin.register(InterviewSession)
class InterviewSessionAdmin(admin.ModelAdmin):
    list_display = ['submission', 'status', 'started_at', 'completed_at', 'duration_seconds']
    list_filter = ['status']
    readonly_fields = ['started_at', 'completed_at']

@admin.register(InterviewQuestion)
class InterviewQuestionAdmin(admin.ModelAdmin):
    list_display = ['interview', 'question_number', 'question_type', 'response_quality']
    list_filter = ['question_type']

@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ['submission', 'created_at']
    readonly_fields = ['created_at']
