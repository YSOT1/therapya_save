# backend/app/main.py

import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Add the backend directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.services.whisper_service import transcribe_audio
from app.services.feedback_service import analyze_pronunciation
from app.services.supabase_service import init_supabase_client, upload_audio_to_supabase, get_video_clip_url

# Initialize Supabase client
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Supabase credentials are not properly configured in environment variables")

supabase = init_supabase_client(SUPABASE_URL, SUPABASE_KEY)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("FRONTEND_URL", "http://localhost:8080")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Directory to temporarily save uploaded files
UPLOAD_DIR = os.getenv("UPLOAD_DIR", "./temp_uploads")
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...), email: str = Form(...)):
    """
    Upload audio recording, save to Supabase, return public URL.
    """
    try:
        local_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(local_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Upload to Supabase
        public_url = upload_audio_to_supabase(supabase, local_path, user_email=email)

        return JSONResponse({
            "status": "success",
            "audio_url": public_url
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.post("/analyze")
async def analyze(file: UploadFile = File(...), expected_sentence: str = Form(...)):
    """
    Analyze pronunciation by comparing transcript to expected sentence.
    """
    try:
        local_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(local_path, "wb") as f:
            content = await file.read()
            f.write(content)

        # Step 1: Transcribe
        transcript = transcribe_audio(local_path)

        # Step 2: Analyze pronunciation mistakes
        feedback = analyze_pronunciation(transcript, expected_sentence)

        return JSONResponse({
            "status": "success",
            "transcript": transcript,
            "feedback": feedback
        })

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)