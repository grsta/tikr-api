from flask import Flask, jsonify
import json

import random
import requests


app = Flask(__name__)

headlines = {
    "Fire": [
        {
            "headline": "🔥 Fire Code 907: Initiating Devices Explained",
            "link": "https://yoursite.com/fire-code-907"
        },
        {
            "headline": "🔥 Do You Need a Dedicated Panel Room? NFPA Says...",
            "link": "https://yoursite.com/fire-panel-room"
        }
    ],
    "Tech News": [
        {
            "headline": "📡 AI Cameras Are Now Reading License Plates",
            "link": "https://yoursite.com/ai-lpr"
        }
    ],
    "Installer Tips": [
        {
            "headline": "🧰 Don't Mount Detectors Near HVAC Vents (Here's Why)",
            "link": None
        }
    ]
}

@app.route("/ticker", methods=["GET"])
def get_ticker():
    available_categories = [cat for cat in headlines if headlines[cat]]
    selected_cat = random.choice(available_categories)
    selected_item = random.choice(headlines[selected_cat])

    return jsonify([
        {
            "category": selected_cat,
            "headline": selected_item["headline"],
            "link": selected_item["link"]
        }
    ])


@app.route("/weather/lafayette", methods=["GET"])
def get_weather():
    try:
        api_key = "eaecd5092b8080adcee4946894343355"  # ← replace this with your actual OpenWeatherMap key
        lat = 30.1843
        lon = -92.0497

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={api_key}&units=imperial"
        )
        response = requests.get(url)
        data = response.json()

        return jsonify([{
            "city": data["name"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition": data["weather"][0]["main"],
            "icon": data["weather"][0]["icon"]
        }])
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# --- Recorder endpoint ------------------------------------------


@app.route("/recorders", methods=["GET"])
def get_recorders():
    with open("recorders.json") as f:
        data = json.load(f)
    return jsonify(data)
# ----------------------------------------------------------------
@app.route("/locker", methods=["GET"])
def get_locker():
    try:
        with open("locker.json") as f:
            data = json.load(f)
        return jsonify(data)
        
 @app.route("/knowledge", methods=["GET"])
def get_knowledge():
    try:
        with open("knowledge.json") as f:
            data = json.load(f)
        return jsonify(data)
       
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
