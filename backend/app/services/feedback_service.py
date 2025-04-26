# backend/app/services/feedback_service.py

from difflib import SequenceMatcher

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

    # Clean texts (remove extra spaces)
    transcript = transcript.replace(" ", "").strip()
    expected = expected.replace(" ", "").strip()

    matcher = SequenceMatcher(None, expected, transcript)
    wrong_letters = []

    for opcode, a0, a1, b0, b1 in matcher.get_opcodes():
        if opcode != 'equal':
            # Means mismatch
            mistake_in_expected = expected[a0:a1]
            wrong_letters.extend(list(mistake_in_expected))

    # Build feedback
    feedback = {
        "overall": "good" if len(wrong_letters) == 0 else "needs_practice",
        "mistakes": []
    }

    for letter in wrong_letters:
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
