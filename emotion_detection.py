# emotion_detection.py
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # fix OpenMP on macOS

print(">>> Starting program...")

from transformers import pipeline

MODEL_NAME = "bhadresh-savani/distilbert-base-uncased-emotion"  # lighter & fast

print(f">>> Loading model: {MODEL_NAME} (first run will download the model)")
emotion_cls = pipeline(
    task="text-classification",
    model=MODEL_NAME,
    return_all_scores=False
)
print(">>> Model loaded.")

def detect_emotion(text: str) -> str:
    if not text or not text.strip():
        return "neutral"
    result = emotion_cls(text)[0]  # {'label': 'joy', 'score': ...}
    label = result["label"].lower().strip()
    mapping = {
        "joy": "joy", "happiness": "joy", "love": "joy", "optimism": "joy",
        "sadness": "sadness", "grief": "sadness",
        "anger": "anger", "annoyance": "anger",
        "fear": "fear", "anxiety": "fear", "nervousness": "fear",
        "surprise": "surprise",
    }
    return mapping.get(label, "neutral")

def detect_mood(text: str) -> str:
    """
    Convert detailed emotion label to simple mood keyword for music retrieval.
    Output will be one of: happy, sad, angry, chill, surprised
    """
    raw_emotion = detect_emotion(text)  # you already have this function

    mapping = {
        "joy": "happy",
        "sadness": "sad",
        "anger": "angry",
        "fear": "chill",
        "surprise": "surprised",
        "neutral": "chill"  # safety fallback
    }

    return mapping.get(raw_emotion, "chill")



if __name__ == "__main__":
    print(">>> Running quick tests...")
    samples = [
        "I just got promoted and I'm so excited!",
        "Today is awful. I feel empty.",
        "I'm worried about the exam tomorrow.",
        "Stop it. This is making me angry.",
        "Okay, let's keep going."
    ]
    for s in samples:
        print(s, "->", detect_emotion(s))
    print(">>> Done.")
