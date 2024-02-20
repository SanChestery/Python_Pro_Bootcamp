import requests
from twilio.rest import Client
import os
from keys import *


parameters = {
    "lat": 36.83749460,
    "lon": 10.19273890,
    "cnt": 4,
    "appid": weather_api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:

    ''' Send Notification through Twilio SMS '''
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages \
        .create(
        body="It will be rainy, bring an umbrella",
        from_=twilio_num,
        to=pers_num
    )

    print(message.status)