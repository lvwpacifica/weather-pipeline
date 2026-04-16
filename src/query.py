import sqlite3

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM weather")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()