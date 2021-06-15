import json

import requests
from django.http import response
from rest_framework import generics, status
from rest_framework.response import Response

API_KEY = "4e17026bf4a14a999b8192040211406"
URL = "https://api.weatherapi.com/v1/forecast.json?key={}&q=Nairobi&days=4".format(API_KEY)

class GetWeatherForcastView(generics.RetrieveAPIView):

    def get(self, request):


        city = request.query_params.get('city')
        days = request.query_params.get('days')

        data = requests.get(
            f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}")

        response = data.json()
        print(response)

        datalist = {
            "maximum": response["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
            "minimum": response["forecast"]["forecastday"][0]["day"]["mintemp_c"],
            "average": response["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
            "median": ((response["forecast"]["forecastday"][0]["day"]["maxtemp_c"]) +
                       (response["forecast"]["forecastday"][0]["day"]["mintemp_c"])) / (2)}

        return Response(datalist)
