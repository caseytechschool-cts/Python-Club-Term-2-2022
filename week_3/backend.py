import requests


def search_postcode(postcode):
    url = f'http://v0.postcodeapi.com.au/suburbs/{postcode}.json'
    response = requests.get(url)
    data = response.json()
    return data


def current_weather(key, lat, lng):
    url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lng}&aqi=no'
    response = requests.get(url)
    data = response.json()
    return data