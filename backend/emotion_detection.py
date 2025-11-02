# emotion_detection.py
import os
import requests

HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"
HEADERS = {"Authorization": f"Bearer {HF_API_TOKEN}"}

print(">>> Starting program...")

def query_hf_api(text: str):
    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": text}, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(">>> Hugging Face API error:", e)
        return None

def detect_emotion(text: str) -> str:
    if not text or not text.strip():
        return "neutral"
    
    result = query_hf_api(text)
    print(">>> Raw API result:", result)  # debug output
    
    # Check structure
    if not result or not isinstance(result, list):
        print(">>> No valid response, defaulting to neutral")
        return "neutral"
    
    # If it's a nested list, take the first dict
    first_item = result[0]
    if isinstance(first_item, list):
        first_item = first_item[0]

    label = first_item.get("label", "neutral").lower().strip()
    
    mapping = {
        "joy": "joy",
        "happiness": "joy",
        "love": "joy",
        "optimism": "joy",
        "sadness": "sadness",
        "grief": "sadness",
        "anger": "anger",
        "annoyance": "anger",
        "fear": "fear",
        "anxiety": "fear",
        "nervousness": "fear",
        "surprise": "surprise",
    }
    detected = mapping.get(label, "neutral")
    print(f">>> Mapped emotion: {detected}")
    return detected

def detect_mood(text: str) -> str:
    raw_emotion = detect_emotion(text)
    mapping = {
        "joy": "happy",
        "sadness": "sad",
        "anger": "angry",
        "fear": "chill",
        "surprise": "surprised",
        "neutral": "chill"
    }
    mood = mapping.get(raw_emotion, "chill")
    print(f">>> Final mood: {mood}")
    return mood

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
