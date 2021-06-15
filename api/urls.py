
from django.urls import path
from .views import (GetWeatherForcastView)

urlpatterns = [
    path('locations', GetWeatherForcastView.as_view()),
]
