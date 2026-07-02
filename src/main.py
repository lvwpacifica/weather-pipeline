from weather_extract import fetch_weather, save_weather, upload_to_azure
from transform import transform_weather
from load import init_db, insert_weather
from aggregate_spark import aggregate_weather_records

# Execute the end-to-end weather data pipeline
def run_pipeline():
    # Initialize the PostgreSQL database
    init_db()
    
    # Extract weather data from the API
    raw_data = fetch_weather()

    # Store the raw JSON locally and upload it to Azure Data Lake Storage Gen2
    filename = save_weather(raw_data)
    upload_to_azure(filename)

    # Transform the raw data and load it into PostgreSQL
    cleaned_data = transform_weather(raw_data)
    insert_weather(cleaned_data)

    # Generate daily aggregated weather metrics using PySpark
    aggregate_weather_records()

    print("Uploaded raw weather JSON to Azure:", filename)
    print("Saved to database:", cleaned_data)
    print("Updated weather_daily_summary table")

if __name__ == "__main__":
    run_pipeline()
