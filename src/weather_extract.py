import requests
import json
from datetime import datetime
import os
from azure.storage.blob import BlobServiceClient

def upload_to_azure(filename):
    account_name = os.environ["AZURE_STORAGE_ACCOUNT_NAME"]
    account_key = os.environ["AZURE_STORAGE_ACCOUNT_KEY"]
    container_name = os.environ["AZURE_STORAGE_CONTAINER_NAME"]

    account_url = f"https://{account_name}.blob.core.windows.net"

    blob_service_client = BlobServiceClient(
        account_url=account_url,
        credential=account_key
    )

    blob_name = f"raw/{filename}"

    blob_client = blob_service_client.get_blob_client(
        container=container_name,
        blob=blob_name
    )

    with open(filename, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

    print(f"Uploaded {filename} to Azure container '{container_name}' as {blob_name}")



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
    return filename

if __name__ == "__main__":
    weather_data = fetch_weather()
    filename = save_weather(weather_data)
    upload_to_azure(filename)