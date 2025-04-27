# backend/app/services/feedback_service.py

from difflib import SequenceMatcher
from backend.app.services.arabic_to_latin import arabic_to_latin
# Example dictionary for Darija letter practice videos
LETTER_PRACTICE = {
    "س": {
        "tip": "ابتسم قليلا وضع لسانك خلف أسنانك الأمامية.",
        "video_url": "/static/videos/seen.mp4",
        "explanation": "حرف \"س\" يحتاج إلى إخراج الهواء بشكل ناعم بين الأسنان."
    },
    "ش": {
        "tip": "اجعل لسانك قريب من سقف الفم وادفع الهواء مع صوت خفيف.",
        "video_url": "/static/videos/sheen.mp4",
        "explanation": "حرف \"ش\" يصدر مع تضييق بسيط للمسار الهوائي في الفم."
    },
    # Add more letters as needed
}


def analyze_pronunciation(transcript: str, expected: str) -> dict:
    """
    Compare transcript with expected sentence and find letter pronunciation issues.
    """
    print(f"Transcript: {transcript}")
    print(f"Expected: {expected}")

    # Transliterate the expected sentence (if in Arabic) to Latin
    expected_latin = arabic_to_latin(expected)

    # Clean texts (already in Latin for comparison)
    transcript = transcript.lower().replace(" ", "").strip()
    expected_latin = expected_latin.lower().replace(" ", "").strip()

    wrong_letters = []

    # Compare character by character
    for i in range(min(len(expected_latin), len(transcript))):
        if expected_latin[i] != transcript[i]:
            wrong_letters.append(expected_latin[i])

    # If expected is longer than transcript, missing letters are also wrong
    if len(expected_latin) > len(transcript):
        wrong_letters.extend(expected_latin[len(transcript):])

    # Build feedback
    feedback = {
        "overall": "good" if len(wrong_letters) == 0 else "needs_practice",
        "mistakes": []
    }

    for letter in set(wrong_letters):  # unique mistakes only
        if letter in LETTER_PRACTICE:
            feedback["mistakes"].append({
                "letter": letter,
                "tip": LETTER_PRACTICE[letter]["tip"],
                "video_url": LETTER_PRACTICE[letter]["video_url"],
                "explanation": LETTER_PRACTICE[letter]["explanation"]
            })
        else:
            feedback["mistakes"].append({
                "letter": letter,
                "tip": "تدرب على نطق هذا الحرف بوضوح.",
                "video_url": "",
                "explanation": "لا يوجد شرح خاص لهذا الحرف حاليا."
            })

    return feedback