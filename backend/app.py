from flask import Flask, request, render_template
from db import get_tracks_by_mood

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    mood = request.args.get("mood")
    tracks = None
    if mood:
        tracks = get_tracks_by_mood(mood)
        print(f"Retrieved {len(tracks)} tracks for mood: {mood}")
    return render_template("index.html", mood=mood, tracks=tracks)

if __name__ == "__main__":
    app.run(debug=True)
