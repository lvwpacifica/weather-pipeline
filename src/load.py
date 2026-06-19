import os
import psycopg

def get_connection():
    database_url = os.environ["DATABASE_URL"]
    return psycopg.connect(database_url)

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

def insert_weather(data):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO weather (time, temperature, windspeed, precipitation, weathercode)
                VALUES (%s, %s, %s, %s, %s)
            """, (data["time"], data["temperature"], data["windspeed"], data["precipitation"], data["weathercode"]))
        conn.commit()