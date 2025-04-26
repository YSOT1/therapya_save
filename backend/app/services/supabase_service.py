# backend/app/services/supabase_service.py

import os
from supabase import create_client, Client
from uuid import uuid4

SUPABASE_URL = os.getenv("https://hpgzcjqykpnajdknhlij.supabase.co")
SUPABASE_KEY = os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhwZ3pjanF5a3BuYWpka25obGlqIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDU2Nzc5ODgsImV4cCI6MjA2MTI1Mzk4OH0.f1FN5xbyzkEv939qiKqHB7RvC1N9IQ_LbqB6I77xFMk")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Buckets assumed: "recordings", "practice_videos"


def upload_audio_to_supabase(local_file_path: str, user_email: str) -> str:
    """
    Upload a local audio file to Supabase Storage and return public URL.
    """
    file_ext = local_file_path.split(".")[-1]
    file_name = f"{user_email}/{uuid4()}.{file_ext}"

    with open(local_file_path, "rb") as f:
        res = supabase.storage.from_("recordings").upload(file_name, f)

    if res.get("error"):
        raise Exception("Failed to upload audio to Supabase")

    public_url = supabase.storage.from_("recordings").get_public_url(file_name)
    return public_url


def get_video_clip_url(letter: str) -> str:
    """
    Get the public video clip URL for a letter.
    (Assuming you uploaded practice clips to Supabase under "practice_videos/" bucket)
    """
    video_filename = f"{letter}.mp4"
    return supabase.storage.from_("practice_videos").get_public_url(video_filename)