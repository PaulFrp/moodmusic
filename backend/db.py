# db.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

LASTFM_API_KEY = os.getenv("LASTFM_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL = "https://ws.audioscrobbler.com/2.0/"

# Default placeholder hash (the gray star)
PLACEHOLDER_HASH = "2a96cbd8b46e442fc41c2b86b821562f"

def get_track_image(artist: str, track: str):
    """
    Fetch a more detailed album image for a track.
    Returns None if not found.
    """
    params = {
        "method": "track.getInfo",
        "artist": artist,
        "track": track,
        "api_key": LASTFM_API_KEY,
        "format": "json"
    }

    try:
        res = requests.get(BASE_URL, params=params, timeout=5)
        if res.status_code != 200:
            return None

        data = res.json()
        images = data.get("track", {}).get("album", {}).get("image", [])
        if not images:
            return None

        image_url = images[-1].get("#text")
        # Avoid returning placeholder
        if image_url and PLACEHOLDER_HASH not in image_url:
            return image_url
        return None

    except Exception as e:
        print(f"[WARN] Failed to get track image: {e}")
        return None


def get_tracks_by_mood(mood: str, limit: int = 10):
    """
    Fetch tracks from Last.fm using the mood as a tag.
    Adds a second request per track to fetch better album art if needed.
    """
    params = {
        "method": "tag.gettoptracks",
        "tag": mood,
        "api_key": LASTFM_API_KEY,
        "format": "json",
        "limit": limit
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        tracks = data.get("tracks", {}).get("track", [])
    except Exception as e:
        print(f"[ERROR] Failed to fetch top tracks: {e}")
        return []

    result = []
    for t in tracks:
        artist = t["artist"]["name"]
        title = t["name"]

        # Try to get the best image from tag.gettoptracks
        img = t["image"][-1]["#text"] if t["image"] else None

        # If it's missing or is the gray placeholder, fetch a better one
        if not img or PLACEHOLDER_HASH in img:
            better_img = get_track_image(artist, title)
            if better_img:
                img = better_img

        result.append({
            "title": title,
            "artist": artist,
            "url": t["url"],
            "image": img or "/static/default.jpg"
        })

    return result
