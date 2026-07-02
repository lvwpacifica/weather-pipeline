# Extract and rename the weather fields needed for the ETL pipeline
def transform_weather(data):
    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "windspeed": current["wind_speed_10m"],
        "precipitation": current["precipitation"],
        "weathercode": current["weather_code"],
        "time": current["time"]
    }
