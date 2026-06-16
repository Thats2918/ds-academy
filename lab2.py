import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"
params = {"latitude": 37.57, "longitude": 126.98, "hourly": "temperature_2m"}
data = requests.get(url, params=params).json()

# 가지고 온 시각, 기온 정보 확인
# hourly = data["hourly"]

# print("첫 시각: ", hourly["time"][0])
# print("첫 기온: ", hourly["temperature_2m"][0])

# print("받은 시각 개수: ", len(hourly["time"]))

df = pd.DataFrame({"시각": data["hourly"]["time"],
                   "기온": data["hourly"]["temperature_2m"]})

print(df.head())