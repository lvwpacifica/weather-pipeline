from weather_extract import fetch_weather, save_weather, upload_to_azure
from transform import transform_weather
from load import init_db, insert_weather
from aggregate_spark import aggregate_weather_records

def run_pipeline():
    init_db()

    raw_data = fetch_weather()

    filename = save_weather(raw_data)
    upload_to_azure(filename)

    cleaned_data = transform_weather(raw_data)
    insert_weather(cleaned_data)

    aggregate_weather_records()

    print("Uploaded raw weather JSON to Azure:", filename)
    print("Saved to database:", cleaned_data)
    print("Updated weather_daily_summary table")

if __name__ == "__main__":
    run_pipeline()