# backend/app/services/supabase_service.py

import os
from supabase import Client, create_client
from uuid import uuid4
from dotenv import load_dotenv
import mimetypes

# Load environment variables
load_dotenv()

# Debug environment variables
print("Loading Supabase configuration...")
print(f"SUPABASE_URL exists: {'SUPABASE_URL' in os.environ}")
print(f"SUPABASE_KEY exists: {'SUPABASE_KEY' in os.environ}")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError(f"Supabase credentials are not properly configured. URL: {SUPABASE_URL}, KEY: {bool(SUPABASE_KEY)}")

def init_supabase_client(url: str, key: str) -> Client:
    """Initialize and return a Supabase client."""
    print(f"Initializing Supabase client with URL: {url[:20]}...")  # Print first 20 chars of URL for security
    client = create_client(url, key)
    print("Supabase client initialized successfully!")
    return client

def upload_audio_to_supabase(supabase: Client, local_file_path: str, user_email: str) -> str:
    """
    Upload a local audio file to Supabase Storage and return public URL.
    """
    # Guess MIME type
    content_type, _ = mimetypes.guess_type(local_file_path)
    if not content_type:
        content_type = "application/octet-stream"  # default fallback

    file_ext = local_file_path.split(".")[-1]
    file_name = f"{user_email}/{uuid4()}.{file_ext}"

    with open(local_file_path, "rb") as f:
        file_content = f.read()

    res = supabase.storage.from_("recordings").upload(
        file_name,
        file_content,
        file_options={"content-type": content_type}
    )

    if res.get("error"):
        raise Exception(f"Failed to upload audio to Supabase: {res['error']}")

    public_url = supabase.storage.from_("recordings").get_public_url(file_name)
    return public_url


def get_video_clip_url(supabase: Client, letter: str) -> str:
    """
    Get the public video clip URL for a letter.
    (Assuming you uploaded practice clips to Supabase under "practice-videos" bucket)
    """
    video_filename = f"{letter}.mp4"
    return supabase.storage.from_("practice-videos/").get_public_url(video_filename)

