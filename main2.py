import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

api_key = os.getenv("api_key")
coordination = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q=Jamshedpur,India&appid={api_key}")
dictionary = {
    "lat" : coordination.json()[0]["lat"],
    "lon" : coordination.json()[0]["lon"],
    "appid": f"{api_key}",
    "cnt" : 4
}
response = requests.get(f"http://api.openweathermap.org/data/2.5/forecast",params=dictionary)
response.raise_for_status()
weather_data = response.json()

umb = False
for i in weather_data["list"]:
    if i["weather"][0]["id"] < 700:
        umb = True
        break

if umb:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
        from_=os.getenv("from_"),
        body="It's going to rain today so be sure to bring an umbrella today ☂️",
        to=os.getenv('to')
    )
    print(message.status)