# emotion_bridge.py
from emotion_detection import detect_mood

def text_to_mood(text: str) -> str:
    """
    Map free-form text to one of: happy/sad/angry/chill/surprised.
    Safe fallback: 'chill'
    """
    try:
        mood = detect_mood(text)
        return mood if mood in {"happy", "sad", "angry", "chill", "surprised"} else "chill"
    except Exception:
        return "chill"
