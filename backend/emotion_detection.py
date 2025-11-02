# emotion_detection.py
import os
import requests

API_URL = "https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion"
API_TOKEN = os.getenv("HF_API_TOKEN")  # Set this in Heroku config vars

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def detect_emotion(text: str) -> str:
    """Call Hugging Face API to get emotion label."""
    if not text or not text.strip():
        return "neutral"

    payload = {"inputs": text}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()

        # Result format: [{'label': 'joy', 'score': 0.95}]
        label = result[0]["label"].lower().strip() if isinstance(result, list) else "neutral"

        mapping = {
            "joy": "joy", "happiness": "joy", "love": "joy", "optimism": "joy",
            "sadness": "sadness", "grief": "sadness",
            "anger": "anger", "annoyance": "anger",
            "fear": "fear", "anxiety": "fear", "nervousness": "fear",
            "surprise": "surprise",
        }
        return mapping.get(label, "neutral")
    except Exception:
        return "neutral"


def detect_mood(text: str) -> str:
    """Map emotion to mood for music retrieval."""
    raw_emotion = detect_emotion(text)
    mapping = {
        "joy": "happy",
        "sadness": "sad",
        "anger": "angry",
        "fear": "chill",
        "surprise": "surprised",
        "neutral": "chill"
    }
    return mapping.get(raw_emotion, "chill")


if __name__ == "__main__":
    samples = [
        "I just got promoted and I'm so excited!",
        "Today is awful. I feel empty.",
        "I'm worried about the exam tomorrow.",
        "Stop it. This is making me angry.",
        "Okay, let's keep going."
    ]
    for s in samples:
        print(s, "->", detect_emotion(s))
