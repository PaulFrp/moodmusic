# emotion_bridge.py
from emotion_detection import detect_mood

def text_to_mood(text: str) -> str:
    """
    Map free-form text to one of: happy/sad/angry/chill/surprised.
    Safe fallback: 'chill'
    """
    try:
        mood = detect_mood(text)
        if mood not in {"happy", "sad", "angry", "chill", "surprised"}:
            print(f"⚠️ detect_mood returned unexpected value: {mood}")
            return "chill"
        return mood
    except Exception as e:
        print(f"❌ Exception in text_to_mood: {e}")
        return "chill"
