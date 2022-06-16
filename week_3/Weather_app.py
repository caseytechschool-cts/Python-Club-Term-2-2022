import PySimpleGUI as sg
from Layout import layout_builder
from backend import search_postcode, current_weather
from Update_window import update_window


# Postcode API: http://v0.postcodeapi.com.au/suburbs/{postcode}.json
# reading image: https://www.adamsmith.haus/python/answers/how-to-read-an-image-data-from-a-url-in-python
# Weather API: http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude,longitude}&aqi=no


layout = layout_builder()
window = sg.Window(title='', layout=layout,
                   background_color='#27504B',
                   titlebar_icon='',
                   use_custom_titlebar=True,
                   titlebar_background_color='#27504B'
                   )

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-button-':
        postcode = sg.popup_get_text(message='Enter a postcode',
                                     default_text='')

        data = search_postcode(postcode)
        lat, lng = data[0]['latitude'], data[0]['longitude']

        key = '7aa275ff85904a07a5a93655222605'
        data = current_weather(key, lat, lng)
        # print(data)
        location = data['location']['name']
        weather_text = data['current']['condition']['text']

        # window['-location-'].update(value=location)
        # window['-weather_oneline-'].update(value=weather_text)
        update_window(window, data)
        print(location, weather_text)

window.close()