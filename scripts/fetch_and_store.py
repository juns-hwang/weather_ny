from utils import fetch_current_weather, insert_current_weather, fetch_forecast, insert_forecast

if __name__ == "__main__":
    current = fetch_current_weather()
    insert_current_weather(current)

    forecast = fetch_forecast()
    insert_forecast(forecast)