from flask import Flask, request, render_template
from db import get_tracks_by_mood
from emotion_bridge import text_to_mood


app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    mood = request.args.get("mood")
    tracks = None
    if mood:
        tracks = get_tracks_by_mood(mood)
        print(f"Retrieved {len(tracks)} tracks for mood: {mood}")
    return render_template("index.html", mood=mood, tracks=tracks)
from flask import request, jsonify

@app.route("/api/recommend_by_text", methods=["POST"])
def recommend_by_text():
    """
    Request JSON:
      { "text": "I feel ...", "k": 10 }   # k 可选，默认10
    Response JSON:
      { "mood": "...", "tracks": [ ... ] }
    """
    data = request.get_json(silent=True) or {}
    text = (data.get("text") or "").strip()
    k = int(data.get("k") or 10)

    if not text:
        return jsonify({"error": "text is required"}), 400
        
    mood = text_to_mood(text)

    tracks = get_tracks_by_mood(mood, k)

    return jsonify({"mood": mood, "tracks": tracks})
    
if __name__ == "__main__":
    app.run(debug=True)
