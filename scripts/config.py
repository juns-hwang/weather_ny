import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITY = "New York"
COUNTRY = "US"

# Coordinates for NYC
LAT = 40.7128
LON = -74.0060

DB_PATH = "../data/db/weather.db"

CURRENT_WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"