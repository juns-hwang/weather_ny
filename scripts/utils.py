import requests
import sqlite3
from datetime import datetime 
from config import API_KEY, CITY, COUNTRY, LAT, LON, DB_PATH, CURRENT_WEATHER_URL, FORECAST_URL

def fetch_current_weather():
    params = {
        'lat': LAT,
        'lon': LON,
        'appid': API_KEY
    }
    response = requests.get(CURRENT_WEATHER_URL, params = params)
    response.raise_for_status()
    return response.json()

def insert_current_weather(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT OR IGNORE INTO current_weather (
            city, country, datetime_utc, temp_k, feels_like_k,
            humidity, pressure, wind_speed, wind_deg, weather_description
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        CITY,
        COUNTRY,
        datetime.utcfromtimestamp(data['dt']),
        data['main']['temp'],
        data['main']['feels_like'],
        data['main']['humidity'],
        data['main']['pressure'],
        data['wind']['speed'],
        data['wind'].get('deg', 0),
        data['weather'][0]['description']
    ))
    conn.commit()
    conn.close()
    print("Current weather inserted.")
    
def fetch_forecast():
    params = {
        'lat': LAT,
            'lon': LON,
            'appid': API_KEY
        }
    response = requests.get(FORECAST_URL, params=params)
    response.raise_for_status()
    return response.json()
    
def insert_forecast(data):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
        
    for entry in data['list']:
        cursor.execute('''
           INSERT OR IGNORE INTO forecast_weather (
                city, country, forecast_time_utc, forecast_created_at,
                temp_k, feels_like_k, humidity, pressure,
                wind_speed, wind_deg, weather_description
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
        CITY,
        COUNTRY,
        datetime.utcfromtimestamp(entry['dt']),
        datetime.utcnow(),
        entry['main']['temp'],
        entry['main']['feels_like'],
        entry['main']['humidity'],
        entry['main']['pressure'],
        entry['wind']['speed'],
        entry['wind'].get('deg', 0),
        entry['weather'][0]['description']
        ))

    conn.commit()
    conn.close()
    print("Forecast weather inserted.")