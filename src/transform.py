def transform_weather(data):
    current = data["current_weather"]

    return {
        "temperature": current["temperature"],
        "windspeed": current["windspeed"],
        "time": current["time"]
    }