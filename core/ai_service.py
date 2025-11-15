"""
AI Service for generating feedback using OpenAI GPT-4
NO FALLBACK DATA - Requires valid API key to function
"""
import os
import json
from openai import OpenAI
from django.conf import settings


class AIFeedbackService:
    def __init__(self):
        """Initialize OpenAI client - REQUIRES valid API key"""
        api_key = settings.OPENAI_API_KEY
        
        if not api_key:
            raise ValueError(
                "❌ OPENAI_API_KEY not configured!\n\n"
                "Set your API key in .env file:\n"
                "  1. Copy .env.example to .env\n"
                "  2. Edit .env and set: OPENAI_API_KEY=sk-proj-your-key\n"
                "  3. Restart the server\n\n"
                "Get key from: https://platform.openai.com/api-keys"
            )
        
        self.client = OpenAI(api_key=api_key)
        self.model = settings.OPENAI_MODEL
        self.max_tokens = settings.OPENAI_MAX_TOKENS
        print(f"[OK] AI Service initialized with model: {self.model}")
    
    def analyze_written_work(self, homework_data, answer_text, answer_file_path=None):
        """
        Analyze student's written homework submission
        Returns: dict with overall_score, strengths, improvements, question_feedback
        RAISES: Exception if AI call fails
        """
        prompt = f"""You are an expert teacher analyzing a student's homework submission.

HOMEWORK DETAILS:
- Subject: {homework_data['subject']}
- Level: {homework_data['level']}
- Title: {homework_data['title']}
- Total Marks: {homework_data['total_marks']}
- Number of Questions: {homework_data['num_questions']}

STUDENT'S ANSWER:
{answer_text[:2000]}

TASK:
Provide detailed feedback in JSON format with:
{{
    "overall_score": <percentage 0-100>,
    "overall_strengths": ["strength1", "strength2", ...],
    "overall_improvements": ["improvement1", "improvement2", ...],
    "questions": [
        {{
            "number": 1,
            "title": "Question Topic",
            "marks_awarded": <int>,
            "marks_total": <int>,
            "percentage": <int>,
            "strengths": ["strength1", "strength2"],
            "improvements": ["improvement1", "improvement2"]
        }},
        ...
    ]
}}

IMPORTANT:
- Identify SPECIFIC MISCONCEPTIONS if present (e.g., "Student thinks force equals velocity, not acceleration")
- Be CONSTRUCTIVE but HONEST about errors and misunderstandings
- Provide ACTIONABLE feedback, not generic praise
- Generate exactly {homework_data['num_questions']} question entries."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert educational assessor who provides detailed, constructive feedback."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
            max_tokens=self.max_tokens
        )
        
        result = json.loads(response.choices[0].message.content)
        print(f"[OK] AI analyzed written work: {result['overall_score']}% score")
        return result
    
    def generate_interview_questions(self, homework_data, written_feedback):
        """
        Generate personalized interview questions based on written work analysis
        Returns: list of question dicts
        RAISES: Exception if AI call fails
        """
        weak_areas = written_feedback.get('overall_improvements', [])[:3]
        
        prompt = f"""Generate 5 interview questions to assess a student's understanding.

CONTEXT:
- Subject: {homework_data['subject']}
- Level: {homework_data['level']}
- Areas needing improvement: {', '.join(weak_areas) if weak_areas else 'General understanding'}

GENERATE 5 QUESTIONS:
1. Process question (explain their approach)
2. Concept question (deeper understanding)
3. Application question (real-world use)
4. Reflection question (metacognition)
5. Extension question (going further)

Return JSON:
{{
    "questions": [
        {{
            "number": 1,
            "type": "process",
            "title": "YOUR APPROACH",
            "question": "Specific question text here",
            "hints": ["hint1", "hint2"]
        }},
        ...
    ]
}}

Make questions specific to the weak areas identified."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert teacher creating assessment questions."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.8,
            max_tokens=min(1000, self.max_tokens)
        )
        
        result = json.loads(response.choices[0].message.content)
        questions = result.get('questions', [])
        print(f"[OK] AI generated {len(questions)} interview questions")
        return questions
    
    def analyze_interview_performance(self, homework_data, written_score, interview_duration, transcription=None):
        """
        Analyze interview performance using ACTUAL TRANSCRIPTION
        
        Args:
            homework_data: Homework context
            written_score: Written work score
            interview_duration: Interview duration in seconds
            transcription: ACTUAL student's verbal responses (from speech-to-text)
        
        Returns: dict with scores, insights, and misconception detection
        RAISES: Exception if AI call fails
        """
        if not transcription:
            raise ValueError("Interview transcription is required for analysis")
        
        prompt = f"""You are an expert educational assessor analyzing a student's VERBAL INTERVIEW responses.

HOMEWORK CONTEXT:
- Subject: {homework_data['subject']}
- Level: {homework_data['level']}
- Written Score: {written_score}%

STUDENT'S VERBAL RESPONSES (from interview):
{transcription[:3000]}

INTERVIEW DURATION: {interview_duration} seconds

TASK:
Analyze the student's verbal understanding and identify:
1. **Misconceptions**: Any incorrect beliefs or misunderstandings revealed in their explanations
2. **Conceptual gaps**: Topics they struggle to explain clearly
3. **Strengths**: Concepts they understand well and can articulate
4. **Verbal vs Written**: How their verbal explanation compares to written work

Provide JSON:
{{
    "interview_score": <percentage 0-100 based on verbal understanding>,
    "problem_solving_score": <0-100, how well they explain their approach>,
    "conceptual_understanding_score": <0-100, depth of understanding shown verbally>,
    "creative_application_score": <0-100, ability to apply concepts in new ways>,
    "misconceptions": ["specific misconception 1", "specific misconception 2"],
    "strong_moments": ["moment1 with specific example", "moment2 with specific example"],
    "development_areas": ["specific area 1 with reason", "specific area 2 with reason"],
    "overall_analysis": "2-3 sentence analysis comparing verbal vs written performance and key insights"
}}

Be SPECIFIC - reference actual things the student said. Identify REAL misconceptions, not generic feedback."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are analyzing a student's interview performance."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
            max_tokens=min(500, self.max_tokens)
        )
        
        result = json.loads(response.choices[0].message.content)
        print(f"[OK] AI analyzed interview: {result.get('interview_score')}% score")
        
        # Log any misconceptions detected
        if result.get('misconceptions'):
            print(f"[WARNING] Misconceptions detected: {len(result['misconceptions'])}")
            for misc in result['misconceptions'][:3]:
                print(f"   - {misc}")
        
        return result
    
    def generate_study_plan(self, submission_data, question_feedbacks, interview_analysis):
        """
        Generate personalized study plan
        Returns: dict with priority topics, strengths, insights
        RAISES: Exception if AI call fails
        """
        weak_questions = [q for q in question_feedbacks if q['percentage'] < 70]
        strong_questions = [q for q in question_feedbacks if q['percentage'] >= 80]
        
        prompt = f"""Generate a personalized study plan for a student.

PERFORMANCE DATA:
- Written Score: {submission_data['written_score']}%
- Interview Score: {submission_data['interview_score']}%
- Weak Areas: {', '.join([q['title'] for q in weak_questions])}
- Strong Areas: {', '.join([q['title'] for q in strong_questions])}

Generate JSON:
{{
    "priority_topics": [
        {{
            "topic": "Topic Name",
            "priority": "high|medium",
            "current_score": <percentage>,
            "actions": ["action1", "action2", "action3"]
        }}
    ],
    "strength_topics": ["topic1", "topic2"],
    "written_vs_verbal_analysis": "Analysis comparing written vs interview performance",
    "learning_style_insights": "Insights about how the student learns best"
}}

Provide actionable, specific recommendations."""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are creating a personalized study plan."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7,
            max_tokens=min(1000, self.max_tokens)
        )
        
        result = json.loads(response.choices[0].message.content)
        print(f"[OK] AI generated study plan with {len(result.get('priority_topics', []))} priority topics")
        return result
