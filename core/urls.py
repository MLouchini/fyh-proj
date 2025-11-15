from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),
    
    # Student URLs
    path('student/', views.student_home, name='student_home'),
    path('student/code/', views.student_code_entry, name='student_code_entry'),
    path('student/upload/', views.student_upload, name='student_upload'),
    path('student/review/', views.student_review_progress, name='student_review_progress'),
    path('student/feedback/', views.student_feedback, name='student_feedback'),
    path('student/interview/prep/', views.student_interview_prep, name='student_interview_prep'),
    path('student/interview/', views.student_interview, name='student_interview'),
    path('student/results/', views.student_final_results, name='student_final_results'),
    path('student/save-recording/', views.save_interview_recording, name='save_interview_recording'),
    
    # Teacher URLs
    path('teacher/login/', views.teacher_login, name='teacher_login'),
    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
    path('teacher/create/', views.teacher_create_homework, name='teacher_create_homework'),
    path('teacher/homework/<int:homework_id>/created/', views.teacher_homework_created, name='teacher_homework_created'),
    path('teacher/homework/<int:homework_id>/results/', views.teacher_view_results, name='teacher_view_results'),
    path('teacher/submission/<int:submission_id>/', views.teacher_student_report, name='teacher_student_report'),
]

