import os
from urllib.parse import urlparse, parse_qs, unquote

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, max, min, count, to_date, col

# Parse the PostgreSQL connection string into JDBC format for PySpark
def parse_database_url(database_url):
    parsed = urlparse(database_url)

    username = unquote(parsed.username)
    password = unquote(parsed.password)
    host = parsed.hostname
    port = parsed.port or 5432
    database = parsed.path.lstrip("/")

    query_params = parse_qs(parsed.query)
    sslmode = query_params.get("sslmode", ["require"])[0]

    jdbc_url = f"jdbc:postgresql://{host}:{port}/{database}?sslmode={sslmode}"

    return jdbc_url, username, password

# Read raw weather data, perform daily aggregations, and write results back to PostgreSQL
def aggregate_weather_records():
    database_url = os.environ["DATABASE_URL"]

    jdbc_url, username, password = parse_database_url(database_url)

    # Path to the PostgreSQL JDBC driver required by Spark
    jar_path = os.path.join(os.path.dirname(__file__), "postgresql-42.7.3.jar")
    
    # Create a Spark session for data processing
    spark = SparkSession.builder \
        .appName("WeatherAggregation") \
        .master("local[*]") \
        .config("spark.driver.extraClassPath", jar_path) \
        .config("spark.executor.extraClassPath", jar_path) \
        .config("spark.shuffle.push.enabled", "false") \
        .getOrCreate()
    
    # Configure JDBC connection properties
    properties = {
        "user": username,
        "password": password,
        "driver": "org.postgresql.Driver"
    }
    
    # Read raw weather records from PostgreSQL
    weather_df = spark.read.jdbc(
        url=jdbc_url,
        table="weather",
        properties=properties
    )
    
    # Convert the timestamp column into a date for daily aggregation
    weather_df = weather_df.withColumn(
        "date",
        to_date(col("time"))
    )
    # Calculate daily weather summary metrics
    summary_df = weather_df.groupBy("date").agg(
        avg("temperature").alias("avg_temperature"),
        max("temperature").alias("max_temperature"),
        min("temperature").alias("min_temperature"),
        avg("windspeed").alias("avg_windspeed"),
        max("windspeed").alias("max_windspeed"),
        avg("precipitation").alias("avg_precipitation"),
        count("*").alias("record_count")
    )
    
    # Write the aggregated results back to PostgreSQL
    summary_df.write.jdbc(
        url=jdbc_url,
        table="weather_daily_summary",
        mode="overwrite",
        properties=properties
    )
    
    # Stop the Spark session
    spark.stop()


if __name__ == "__main__":
    aggregate_weather_records()
