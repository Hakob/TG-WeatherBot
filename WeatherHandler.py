# -*- coding: utf-8 -*-
import requests
from BotHandler import jsonify


class WeatherHandler:
    """
    Weather info Handler, which use https://openweathermap.org/ API
    """

    def __init__(self, api_key):
        self.key = api_key
        self.api_url = "http://api.openweathermap.org/data/2.5/weather"

    @jsonify
    def by_location(self, location, unit='metric'):
        params = {'appid': self.key, 'lat': location['latitude'],
                  'lon': location['longitude'], 'units': unit}  # units => <none>: Kelvin, metric: Celsius,
        resp = requests.get(self.api_url, params)                   # imperial: Fahrenheit
        return resp

    @jsonify
    def by_city(self, city_name, unit='metric'):
        params = {'appid': self.key, 'q': city_name, 'units': unit}
        resp = requests.get(self.api_url, params)
        return resp
