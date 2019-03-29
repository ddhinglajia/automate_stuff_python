#!/usr/bin/env python3

# prints the weather for a location from command line

import json, requests, sys

# compute location from command line arguments
if len(sys.argv) < 2:
    print('Usage: 056_quickWeather.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])

# download the json-data from OpenWeatherMap.prg's API

# url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' %(location)
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s' %(location)
response = requests.get(url).json()
response.raise_for_status()

# load json data into a python variable
weatherData = json.loads(response.text)

# print weather data

w = weatherData['list']

print(weatherData)


print('current weather in %s: ' %(location))
print(w[0]['weather'][0]['main'],'-', w[0]['weather'][0]['description'])
# print()
# print('tomorrow:')
# print(w[1]['weather'][0]['main'],'-', w[1]['weather'][0]['description'])
# print()
# print('day after tomorrow:')
# print(w[2]['weather'][0]['main'],'-', w[2]['weather'][0]['description'])
