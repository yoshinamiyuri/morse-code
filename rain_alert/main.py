import requests
from twilio.rest import Client
import os

## https://www.ventusky.com/?p=25.061;87.263;9&l=rain-1h
## https://www.latlong.net/

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACc0484d599a3e3ac7c1d171f1d3b6a6ee"
auth_token = "34747c91763c13fa0b576c7ce96ab109"

weather_parameters = {
    "lat": 27.809460,
    "lon": 78.656920,
    "appid": "903576ae96c389a724f01259f24adf22",
    "exclude": "current,minutely,daily"
}

# response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}")
response = requests.get(OWN_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data)

id = weather_data["hourly"][0]["weather"][0]["id"]
print(id)

##　講師の方法
# will_rain = False
#
# weather_slice = weather_data["hourly"[:12]]
# print(weather_slice)
# for hour_data in weather_slice:
#     condition_code = hour_data["weather"][0]["id"]
#     if int(condition_code) < 700:
#         will_rain = True
#
# if will_rain:
#     print("Bring an umbrella.")


weather_data_for_12hs = [
    weather_data["hourly"][time]["weather"][0]["id"]
    for time in range(12)
    if weather_data["hourly"][time]["weather"][0]["id"] < 802
]
print("weather_data_for_12", weather_data_for_12hs)
if len(weather_data_for_12hs) > 0:
    print("傘を持ってくる")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="今日雨降るから気をつけてね〜☂️持っていって！",
        from_='+13462482501',
        to='+819092885387'
    )
    # print(message.sid)
    print(message.status)
