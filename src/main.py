from weather_extract import fetch_weather, save_weather, upload_to_azure
from transform import transform_weather
from load import init_db, insert_weather

def run_pipeline():
    init_db()

    raw_data = fetch_weather()

    filename = save_weather(raw_data)
    upload_to_azure(filename)

    cleaned_data = transform_weather(raw_data)
    insert_weather(cleaned_data)

    print("Uploaded raw weather JSON to Azure:", filename)
    print("Saved to database:", cleaned_data)

if __name__ == "__main__":
    run_pipeline()