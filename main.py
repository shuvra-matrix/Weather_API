import requests
import os
from twilio.rest import Client

API_SITE = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("API_KEY")

account_sid = "ACcd587c473e96c7d2e9fe4c0e11648ae7"
auth_token = "" #YOUR AUTH_TOKEN

MY_PARAMETERS = {"lat": 23.647970, "lon": 88.128418, "appid": API_KEY, "exclude": "current,minutely,daily"}

request = requests.get(API_SITE, params=MY_PARAMETERS)
request.raise_for_status()
weather_data = request.json()
weather_id = weather_data["hourly"][:12]

will_rain = False

for weathers in weather_id:
    new_data = weathers["weather"][0]["id"]
    if new_data < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to be rain today! Bring an Umbrella ☂️ ",
        from_='',#PUT YOUR NUMBER
        to=''# PUT YOUR ANOTHER NUMBER
    )
    print(message.status)
