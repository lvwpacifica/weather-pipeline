import os
import psycopg

# Create a connection to the PostgreSQL database using the environment variable
def get_connection():
    database_url = os.environ["DATABASE_URL"]
    return psycopg.connect(database_url)

# Create the weather table if it does not already exist
def init_db():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS weather (
                    id SERIAL PRIMARY KEY,
                    time TIMESTAMP,
                    temperature REAL,
                    windspeed REAL,
                    precipitation REAL,
                    weathercode INTEGER
                )
            """)
        conn.commit()

# Insert a weather record into the weather table
def insert_weather(data):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO weather (time, temperature, windspeed, precipitation, weathercode)
                VALUES (%s, %s, %s, %s, %s)
            """, (data["time"], data["temperature"], data["windspeed"], data["precipitation"], data["weathercode"]))
        conn.commit()
