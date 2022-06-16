import base64
import time
import requests


def update_window(window, weather_data):
    location = weather_data['location']['name']
    weather_text = weather_data['current']['condition']['text']
    temp = f"{weather_data['current']['temp_c']}°C"
    feels_like = f"{weather_data['current']['feelslike_c']}°C"
    wind = f"{weather_data['current']['wind_kph']} km/h"
    humidity = f"{weather_data['current']['humidity']}%"
    precip = f"{weather_data['current']['precip_mm']} mm"
    pressure = f"{weather_data['current']['pressure_mb']} hPa"

    epoch = weather_data['current']['last_updated_epoch']
    updated_time = f"Updated: {time.strftime('%b %d %I:%M:%S %p', time.localtime(epoch))}"

    response = requests.get(f"http:{weather_data['current']['condition']['icon']}")
    base64_image = base64.b64encode(response.content)

    window['-location-'].update(value=location)
    window['-weather_oneline-'].update(value=weather_text)
    window['-temp-'].update(value=temp)
    window['-feels_like_value-'].update(value=feels_like)
    window['-wind_value-'].update(value=wind)
    window['-humidity_value-'].update(value=humidity)
    window['-precip_value-'].update(value=precip)
    window['-pressure_value-'].update(value=pressure)
    window['-updated_on-'].update(value=updated_time)
    window['-weather_image-'].update(source=base64_image)

