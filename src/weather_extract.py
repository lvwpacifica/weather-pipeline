import requests

def fetch_weather():
    url = "https://api.open-meteo.com/v1/forecast?latitude=32.78&longitude=-96.8&current_weather=true"
    response = requests.get(url)
    return response.json()