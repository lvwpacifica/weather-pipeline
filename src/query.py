import sqlite3

# Connect to the local SQLite database
conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

# Retrieve all weather records
cursor.execute("SELECT * FROM weather")
rows = cursor.fetchall()

# Display each weather record
for row in rows:
    print(row)

# Close the database connection
conn.close()
