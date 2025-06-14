from flask import Flask, jsonify
import random

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
    
       return jsonify([{
    "category": selected_cat,
    "headline": selected_item["headline"],
    "link": selected_item["link"]
}])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
