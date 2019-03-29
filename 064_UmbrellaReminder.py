#!/usr/bin/env python3

# practice : text reminder to pack umbrella 

import json, requests, sys
from twilio.rest import Client

location = sys.argv[1]

account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token  = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+****'
twilo_number = '+****'

def textMyself(message):
    twilo_cli = Client(account_sid, auth_token)
    twilo_cli.messages.create(body=message, from_=twilo_number, to=my_number)

def checkWeather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=%s' %(location)
    response = requests.get(url).json()
    response.raise_for_status()
    weatherData = json.loads(response.text)
    w = weatherData['list']
    rainF = w[0]['rain'][0]['3h']
    textMyself("today's rain forecast is %s" % rainF)





checkWeather()