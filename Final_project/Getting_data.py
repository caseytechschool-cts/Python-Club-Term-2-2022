import requests
from key import key


def search_postcode(postcode):
    url = f'http://v0.postcodeapi.com.au/suburbs/{postcode}.json'
    response = requests.get(url)
    data = None

    if response.status_code == 200:
        data = response.json()
    return data


def current_weather(latitude, longitude):
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={latitude},{longitude}&aqi=no'
    response = requests.get(url)
    return response.json()

