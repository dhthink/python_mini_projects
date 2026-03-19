# import openmeteo_requests

# import pandas as pd
# import requests_cache
# from retry_requests import retry

# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)
# cities = [
#     {"name": "Indianapolis",  "latitude": 39.77,  "longitude": -86.16},
#     {"name": "Columbus OH",   "latitude": 39.96,  "longitude": -82.99},
#     {"name": "Myrtle Beach",  "latitude": 33.69,  "longitude": -78.89},]
# url = "https://api.open-meteo.com/v1/forecast"

# for city in cities:
#     params = {
#         "latitude": city["latitude"],
#         "longitude": city["longitude"],
#         "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
#         "temperature_unit": "fahrenheit",
#         "timezone": "America/Indiana/Indianapolis",
#     }

#     responses = openmeteo.weather_api(url, params=params)
#     response = responses[0]

#     daily = response.Daily()
#     daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
#     daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
#     daily_sunrise = daily.Variables(2).ValuesInt64AsNumpy()
#     daily_sunset = daily.Variables(3).ValuesInt64AsNumpy()

#     daily_data = {"date": pd.date_range(
#         start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
#         end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
#         freq = pd.Timedelta(seconds = daily.Interval()),
#         inclusive = "left"
#     )}

#     daily_data["temp_max_f"] = daily_temperature_2m_max.astype(int)
#     daily_data["temp_min_f"] = daily_temperature_2m_min.astype(int)
#     daily_data["sunrise"]    = pd.to_datetime(daily_sunrise, unit="s", utc=True).tz_convert("America/Indiana/Indianapolis")
#     daily_data["sunset"]     = pd.to_datetime(daily_sunset,  unit="s", utc=True).tz_convert("America/Indiana/Indianapolis")

#     daily_dataframe = pd.DataFrame(data = daily_data)

#     # Format date and times
#     daily_dataframe["date"]    = daily_dataframe["date"].dt.strftime("%m-%d-%Y")
#     daily_dataframe["sunrise"] = daily_dataframe["sunrise"].dt.strftime("%I:%M %p")
#     daily_dataframe["sunset"]  = daily_dataframe["sunset"].dt.strftime("%I:%M %p")

#     print(f"\n--- {city['name']} ---")
#     print(daily_dataframe.to_string(index=False, col_space=15))

import requests
import pandas as pd

cities = [
    {"name": "Indianapolis", "latitude": 39.77,  "longitude": -86.16},
    {"name": "Columbus OH",  "latitude": 39.96,  "longitude": -82.99},
    {"name": "Myrtle Beach", "latitude": 33.69,  "longitude": -78.89},
]

url = "https://api.open-meteo.com/v1/forecast"

for city in cities:
    params = {
        "latitude": city["latitude"],
        "longitude": city["longitude"],
        "daily": ["temperature_2m_max", "temperature_2m_min", "sunrise", "sunset"],
        "temperature_unit": "fahrenheit",
        "timezone": "America/Indiana/Indianapolis",
    }

    response = requests.get(url, params=params).json()
    daily = response["daily"]

    daily_dataframe = pd.DataFrame({
        "date":       pd.to_datetime(daily["time"]).strftime("%m-%d-%Y"),
        "temp_max_f": [int(t) for t in daily["temperature_2m_max"]],
        "temp_min_f": [int(t) for t in daily["temperature_2m_min"]],
        "sunrise":    pd.to_datetime(daily["sunrise"]).strftime("%I:%M %p"),
        "sunset":     pd.to_datetime(daily["sunset"]).strftime("%I:%M %p"),
    })

    print(f"\n--- {city['name']} ---")
    print(daily_dataframe.to_string(index=False, col_space=15))
    

