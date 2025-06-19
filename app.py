
from flask import Flask, jsonify, request
import json
import random
import requests

app = Flask(__name__)


# ---------- Headline ticker ----------
headlines = [
    {"category": "Tip", "headline": "Don’t crimp cables with pliers!", "link": "https://example.com"},
    {"category": "News", "headline": "New 8 MP turret released", "link": "https://example.com"},
]

@app.route("/ticker", methods=["GET"])
def get_ticker():
    selected = random.choice(headlines)
    return jsonify(selected)


# ---------- Weather test (static lat/lon for now) ----------
@app.route("/weather/lafayette", methods=["GET"])
def get_weather():
    try:
        api_key = "replace-with-your-OpenWeather-key"
        lat, lon = 30.1843, -92.0497
        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={api_key}&units=imperial"
        )
        data = requests.get(url).json()

        return jsonify({
            "city":  data["name"],
            "temp":  data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "condition":  data["weather"][0]["main"],
            "icon": data["weather"][0]["icon"]
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------- Recorder endpoint ----------
@app.route("/recorders", methods=["GET"])
def get_recorders():
    with open("recorders.json") as f:
        return jsonify(json.load(f))


# ---------- Locker endpoint ----------
@app.route("/locker", methods=["GET"])
def get_locker():
    with open("locker.json") as f:
        return jsonify(json.load(f))


# ---------- Knowledge endpoint ----------
@app.route("/Knowledge", methods=["GET"])
def get_Knowledge():
    try:
        with open("Knowledge.json") as f:
            return jsonify(json.load(f))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------- Run local ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
