# Weather Data Ingestion Pipeline

This project implements an end-to-end cloud-based ETL pipeline that ingests weather data from the Open-Meteo API, stores raw JSON data in Azure Data Lake Storage Gen2, transforms the data using PySpark, and loads daily aggregated results into PostgreSQL for reporting in Power BI.

## Features

- Extracts weather data from the Open-Meteo API
- Stores raw JSON data in Azure Data Lake Storage Gen2
- Loads weather records into PostgreSQL
- Performs daily aggregations using PySpark
- Visualizes weather trends with Power BI
- Automates pipeline execution using GitHub Actions

## Tech Stack

- Python
- PySpark
- Azure Data Lake Storage Gen2
- PostgreSQL (Neon)
- Power BI
- GitHub Actions
- Git

## Data Source

Weather data provided by Open-Meteo.

https://open-meteo.com/

Data licensed under CC BY 4.0.
