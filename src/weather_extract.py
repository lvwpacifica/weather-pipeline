import requests
import json
from datetime import datetime

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def save_weather(data):
    filename = f"weather_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Saved weather data to {filename}")

if __name__ == "__main__":
    weather_data = fetch_weather()
    save_weather(weather_data)