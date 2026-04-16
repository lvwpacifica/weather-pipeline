from weather_extract import fetch_weather
from transform import transform_weather
from load import init_db, insert_weather

def run_pipeline():
    init_db()

    raw_data = fetch_weather()
    cleaned_data = transform_weather(raw_data)

    insert_weather(cleaned_data)

    print("Saved to database:", cleaned_data)

if __name__ == "__main__":
    run_pipeline()