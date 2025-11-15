"""
Speech-to-Text Transcription Service using Hugging Face InferenceClient
"""
from huggingface_hub import InferenceClient
from django.conf import settings


class TranscriptionService:
    def __init__(self):
        """Initialize Hugging Face InferenceClient for ASR"""
        self.api_key = settings.HUGGINGFACE_API_KEY
        
        if not self.api_key:
            raise ValueError(
                "❌ HUGGINGFACE_API_KEY not configured!\n\n"
                "Set your API key in .env file:\n"
                "  1. Copy .env.example to .env\n"
                "  2. Edit .env and set: HUGGINGFACE_API_KEY=hf_your-key\n"
                "  3. Restart the server\n\n"
                "Get key from: https://huggingface.co/settings/tokens"
            )
        
        self.model = settings.HUGGINGFACE_ASR_MODEL
        # Use official Hugging Face InferenceClient (recommended way)
        self.client = InferenceClient(token=self.api_key)
        print(f"[OK] Transcription Service initialized with model: {self.model}")
        print(f"[OK] Using Hugging Face InferenceClient (official library)")
    
    def transcribe_audio(self, audio_file_path):
        """
        Transcribe audio file to text using Hugging Face Whisper via InferenceClient
        
        Args:
            audio_file_path: Path to audio/video file (will extract audio)
        
        Returns:
            str: Transcribed text
        
        Raises:
            Exception: If transcription fails
        
        Reference: https://huggingface.co/docs/huggingface_hub/guides/inference
        """
        try:
            print(f"[AUDIO] Transcribing audio file: {audio_file_path}")
            
            # Use InferenceClient for automatic speech recognition
            # Pass file directly - client handles file reading and API calls
            result = self.client.automatic_speech_recognition(
                audio_file_path,
                model=self.model
            )
            
            # Result can be a string or dict depending on model
            if isinstance(result, dict):
                transcription = result.get('text', '')
            else:
                transcription = str(result)
            
            if not transcription:
                raise ValueError("Empty transcription returned from API")
            
            print(f"[OK] Transcription successful: {len(transcription)} characters")
            print(f"[OK] Preview: {transcription[:100]}...")
            
            return transcription
        
        except FileNotFoundError:
            raise Exception(f"Audio file not found: {audio_file_path}")
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")
    
    def transcribe_with_timestamps(self, audio_file_path):
        """
        Transcribe with timestamp information (if supported by model)
        
        Returns:
            dict: {"text": "...", "chunks": [{"text": "...", "timestamp": [start, end]}]}
        """
        try:
            # Try to get timestamps if model supports it
            result = self.client.automatic_speech_recognition(
                audio_file_path,
                model=self.model,
                parameters={"return_timestamps": True}
            )
            
            print(f"[OK] Transcription with timestamps successful")
            return result
        
        except Exception as e:
            print(f"[WARNING] Timestamp transcription error: {e}")
            # Fallback to regular transcription
            text = self.transcribe_audio(audio_file_path)
            return {"text": text, "chunks": []}

