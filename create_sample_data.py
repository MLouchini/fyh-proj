import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buddybud.settings')
django.setup()

from django.contrib.auth.models import User
from core.models import Homework, Submission
from datetime import datetime, timedelta
import random

print("Creating sample data for BuddyBud...")

# Create demo teacher
teacher, created = User.objects.get_or_create(
    username='demo_teacher',
    defaults={
        'first_name': 'Mr.',
        'last_name': 'Johnson',
        'email': 'teacher@buddybud.com'
    }
)
print(f"[OK] Teacher created: {teacher.get_full_name()}")

# Create sample homeworks
homeworks_data = [
    {
        'code': 'PHY-2024-A3B7',
        'title': 'Physics A-Level Practice Exam',
        'subject': 'Physics',
        'level': 'A-Level',
        'class_name': 'Year 13 Physics - Period 4',
        'total_marks': 60,
        'num_questions': 5,
        'instructions': 'Show all working. Include units. Use diagrams where appropriate.'
    },
    {
        'code': 'CHE-2024-M8K4',
        'title': 'Thermodynamics Quiz',
        'subject': 'Chemistry',
        'level': 'A-Level',
        'class_name': 'Year 12 Chemistry - Period 2',
        'total_marks': 45,
        'num_questions': 3,
        'instructions': 'Complete all questions. Calculator allowed.'
    },
    {
        'code': 'WAV-2024-P5N9',
        'title': 'Wave Motion Problems',
        'subject': 'Physics',
        'level': 'GCSE',
        'class_name': 'Year 11 Physics - Period 3',
        'total_marks': 50,
        'num_questions': 4,
        'instructions': 'Show your working clearly.'
    }
]

for hw_data in homeworks_data:
    homework, created = Homework.objects.get_or_create(
        code=hw_data['code'],
        defaults={
            'teacher': teacher,
            'title': hw_data['title'],
            'subject': hw_data['subject'],
            'level': hw_data['level'],
            'class_name': hw_data['class_name'],
            'due_date': datetime.now().date() + timedelta(days=7),
            'total_marks': hw_data['total_marks'],
            'num_questions': hw_data['num_questions'],
            'instructions': hw_data['instructions'],
            'status': 'active'
        }
    )
    if created:
        print(f"[OK] Homework created: {homework.title} ({homework.code})")
    
    # Create sample submissions for the first homework
    if hw_data['code'] == 'PHY-2024-A3B7':
        students = [
            ('Sarah Mitchell', 94, 96),
            ('James Thompson', 85, 89),
            ('Alice Kim', 80, 84),
            ('David Chen', 75, 81),
            ('Emma Rodriguez', 70, 72),
            ('Michael Brown', 62, 68),
        ]
        
        for student_name, written_score, interview_score in students:
            submission, created = Submission.objects.get_or_create(
                homework=homework,
                student_name=student_name,
                defaults={
                    'answer_text': f'Sample answers from {student_name}',
                    'submitted_at': datetime.now() - timedelta(days=random.randint(1, 3)),
                    'status': 'complete',
                    'written_score': written_score,
                    'interview_score': interview_score,
                    'overall_score': (written_score + interview_score) // 2
                }
            )
            if created:
                print(f"   [OK] Submission created: {student_name} - {submission.overall_score}%")

print("\n[SUCCESS] Sample data created successfully!")
print("\nYou can now:")
print("   - Visit http://localhost:8000/teacher/dashboard/")
print("   - Visit http://localhost:8000/student/code/")
print("   - Use code: PHY-2024-A3B7 to test student flow")

