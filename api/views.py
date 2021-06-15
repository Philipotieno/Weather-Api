import json

import requests
from django.http import response
from rest_framework import generics, status
from rest_framework.response import Response

API_KEY = "4e17026bf4a14a999b8192040211406"
class GetWeatherForcastView(generics.RetrieveAPIView):

    def get(self, request):

        try:
            city = request.query_params.get('city')
            days = request.query_params.get('days')

            data = requests.get(
                f"https://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={city}&days={days}")

            response = data.json()

            datalist = {
                "maximum": response["forecast"]["forecastday"][0]["day"]["maxtemp_c"],
                "minimum": response["forecast"]["forecastday"][0]["day"]["mintemp_c"],
                "average": response["forecast"]["forecastday"][0]["day"]["avgtemp_c"],
                "median": ((response["forecast"]["forecastday"][0]["day"]["maxtemp_c"]) +
                        (response["forecast"]["forecastday"][0]["day"]["mintemp_c"])) / (2)}

            return Response(datalist)
        except:
            return Response({'data': 'Invalid city name', 'status': 404}, status=404)
