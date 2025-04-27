import whisper
import ssl
import os
import certifi
import re
# Load Whisper model once (efficient)
model = whisper.load_model("base")  # or "small" if you want better accuracy but a bit slower

os.environ['SSL_CERT_FILE'] = certifi.where()

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe the given audio file to text using Whisper.
    """
    result = model.transcribe(file_path, language="ar", task="transcribe")  # Force Arabic
    text = result.get("text", "").strip()

    # Ensure text is not corrupted by non-Arabic characters in the transcription
    text = re.sub(r'[^\u0600-\u06FF\s]', '', text)  # Removing non-Arabic characters
    return text
