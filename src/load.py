import sqlite3

def init_db():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            time TEXT,
            temperature REAL,
            windspeed REAL
        )
    """)

    conn.commit()
    conn.close()


def insert_weather(data):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO weather (time, temperature, windspeed)
        VALUES (?, ?, ?)
    """, (data["time"], data["temperature"], data["windspeed"]))

    conn.commit()
    conn.close()