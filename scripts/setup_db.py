import sqlite3
from config import DB_PATH
import os

def create_tables():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS current_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        country TEXT,
        datetime_utc TIMESTAMP,
        temp_k REAL,
        feels_like_k REAL,
        humidity INTEGER,
        pressure INTEGER,
        wind_speed REAL,
        wind_deg INTEGER,
        weather_description TEXT,
        UNIQUE(city, datetime_utc)
    );
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS forecast_weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT,
        country TEXT,
        forecast_time_utc TIMESTAMP,
        forecast_created_at TIMESTAMP,
        temp_k REAL,
        feels_like_k REAL,
        humidity INTEGER,
        pressure INTEGER,
        wind_speed REAL,
        wind_deg INTEGER,
        weather_description TEXT,
        UNIQUE(city, forecast_time_utc)
    );
    ''')

    conn.commit()
    conn.close()
    
    print("Table created.")
    
if __name__ == "__main__":
    create_tables()
    print(os.path.abspath(DB_PATH))