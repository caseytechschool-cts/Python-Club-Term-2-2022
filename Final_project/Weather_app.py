import PySimpleGUI as sg
from Layout import layout_builder
from Getting_data import search_postcode, current_weather
from Update_window import update_window

# Postcode API: http://v0.postcodeapi.com.au/suburbs/{postcode}.json
# reading image: https://www.adamsmith.haus/python/answers/how-to-read-an-image-data-from-a-url-in-python
# Weather API: http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude,longitude}&aqi=no


def main():
    layout = layout_builder()
    window = sg.Window(title='', layout=layout, background_color='#27504B',
                       use_custom_titlebar=True, titlebar_icon='',
                       titlebar_background_color='#27504B')

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == '-button-':
            postcode = sg.popup_get_text(message='Enter a postcode',
                                         default_text='',
                                         background_color='#27504B')
            if postcode:
                postcode_data = search_postcode(postcode)
                if postcode_data:
                    latitude = postcode_data[0]['latitude']
                    longitude = postcode_data[0]['longitude']

                    weather_data = current_weather(latitude, longitude)
                    update_window(window, weather_data)

    window.close()


if __name__ == '__main__':
    main()
