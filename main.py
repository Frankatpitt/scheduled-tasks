import requests
import json
from twilio.rest import Client
def send_message(body):
    message=client.messages.create(
        from_='whatsapp:+14155238886',
        # content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
        # content_variables='{"1":"12/1","2":"3pm"}',
        body=body,
        to='whatsapp:+14125769428'
    )

ACCOUNT_SID="ACff0454cc55c0798d5fbd5d9b3cefdf9a"
AUTH_TOKEN="29889a6d32a2f985f223d01cdbcd1191"

API_KEY="2c81d90efa378062a3abf12780ce96a3"
parms={
    "lat":47.547,
    "lon":-124.233,
    "appid":API_KEY,
    "cnt":4
}

client=Client(ACCOUNT_SID,AUTH_TOKEN)

response=requests.get('https://api.openweathermap.org/data/2.5/forecast',params=parms)
response.raise_for_status()
output=response.json()

# print(json.dumps(output,indent=4))

send_message("From github")
weather_data=output['list'][0]['weather'][0]['id']

for index in range(0,4):
    if int(output['list'][index]['weather'][0]['id'])<700:
        send_message("Test again!")
        break
