import requests
# from decouple import config
import requests
from rest_framework import status
import json

API_KEY = "4e17026bf4a14a999b8192040211406"
WEATHER_URL = "https://api.weatherapi.com/v1/forecast.json?key={}&q=Nairobi&days=4".format(API_KEY)



def get_erp_status_code(response):
    success = response.ok and (response.json().get('success') != False)

    return status.HTTP_200_OK if success else status.HTTP_400_BAD_REQUEST


def get_data(postfix, data):
    '''
    params:
        - postfix e.g /api/users for erp endpoint to hit
        - data e.g {"key": "value"} to pass to erp
    '''
    api_response = requests.get(f"{WEATHER_URL}{postfix}", data=json.dumps(data))
    return api_response



def make_defaults(defaults, data):
    '''
    params:
        - defaults - dictionary containing data keys with empty strings
        - data e.g {"key": "value"} to pass to erp

    '''
    return_value = {}
    for k, v in defaults.items():
        return_value[k] = data.get(k, v)
    return return_value
