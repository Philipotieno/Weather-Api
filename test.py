import requests
import json

r = requests.get(
    "https://api.weatherapi.com/v1/forecast.json?key=4e17026bf4a14a999b8192040211406&q=Nairobi")
res = r.json()

# Extract specific node content.
# print(res['quiz']['sport'])

# Dump data as string
data = json.dumps(res)
print(data)


[
    {"date": "2021-06-15",
     "date_epoch": 1623715200,
     "day": {"maxtemp_c": 25.5,
             "mintemp_c": 13.3,
             "avgtemp_c": 19.1,
             "condition": {}}}]
