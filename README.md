# 🎵 MoodMusic — AI Mood-Based Music Recommender

MoodMusic is a simple Flask web app that recommends songs based on your **mood**.  
It uses the **Last.fm API** to fetch tracks tagged with moods (like *chill*, *energetic*, *melancholy*, etc.), and displays them beautifully on a modern web interface.

> 🧠 The mood detection AI is assumed to exist separately — this app focuses on the music recommendation and frontend.

---

## 🚀 Features

- 🌈 Enter a mood (e.g., “chill”, “happy”, “sad”) to get song recommendations  
- 🎶 Fetches real tracks from **Last.fm** with proper album covers  
- 🧠 Automatically improves image quality using `track.getInfo` API calls  
- 💻 Clean modern frontend (HTML + CSS + JS)  
- ⚙️ Built with **Flask**, **Requests**, and **dotenv**

---

## 🧩 Project Structure

moodmusic/
│
├── backend/
│ ├── app.py # Flask app — serves frontend + API
│ ├── db.py # Handles Last.fm API requests
│ ├── templates/
│ │ └── index.html # Frontend page
│ ├── static/
│ │ └── style.css # Frontend styling
│ ├── .env # API key stored here
│ └── requirements.txt # Python dependencies

yaml
Copier le code

---

## 🔑 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/PaulFrp/moodmusic.git
cd moodmusic/backend
2. Create a virtual environment (recommended)
bash
Copier le code
python -m venv venv
source venv/bin/activate     # On macOS/Linux
venv\Scripts\activate        # On Windows
3. Install dependencies
bash
Copier le code
pip install -r requirements.txt
4. Get a Last.fm API key
Go to: https://www.last.fm/api/account/create

Create an API key.

Copy your key.

Then create a .env file inside the backend/ folder and add:

ini
Copier le code
LASTFM_API_KEY=your_api_key_here
5. Run the app
bash
Copier le code
python app.py
Flask will start a local web server at:

👉 http://127.0.0.1:5000