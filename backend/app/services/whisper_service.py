# backend/app/services/whisper_service.py

import whisper
import ssl
import os
import certifi

# Load Whisper model once (efficient)
model = whisper.load_model("base")  # or "small" if you want better accuracy but a bit slower

os.environ['SSL_CERT_FILE'] = certifi.where()

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe the given audio file to text using Whisper.
    """
    result = model.transcribe(file_path, language="ar")  # Force Arabic (Darija close)
    text = result.get("text", "").strip()
    return text
