import PySimpleGUI as sg
from Layout import layout_builder
from Getting_data import search_postcode, current_weather
from Update_window import update_window
import geocoder


# Postcode API: http://v0.postcodeapi.com.au/suburbs/{postcode}.json
# reading image: https://www.adamsmith.haus/python/answers/how-to-read-an-image-data-from-a-url-in-python
# Weather API: http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude,longitude}&aqi=no


def main():
    layout = layout_builder()
    window = sg.Window(title='', layout=layout, background_color='#27504B',
                       use_custom_titlebar=True, titlebar_icon='',
                       titlebar_background_color='#27504B')
    second_window = False
    multiple_postcode = False
    run_once = True

    g = geocoder.ipinfo('me')
    lat, lng = g.latlng
    print(lat, lng)
    weather_data = current_weather(lat, lng)
    print(weather_data)

    while True:
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED:
            break


        # weather_data = current_weather(lat, lng)
        if run_once:
            update_window(window, weather_data)
            run_once = not run_once

        if event == '-button-':
            postcode = sg.popup_get_text(message='Enter a postcode',
                                         default_text='',
                                         background_color='#27504B')
            if postcode:
                postcode_data = search_postcode(postcode)
                if postcode_data:
                    if len(postcode_data) >= 2 and not second_window:
                        second_window = True
                        multiple_postcode = True
                        window.Hide()
                        count = 0
                        radio_group = []
                        radio_group_2 = []
                        for data in postcode_data:
                            radio = sg.Radio(text=f"{data['name']}", group_id='radio1', key=count, text_color='#BCC9C2',
                                             background_color='#27504B')
                            radio_group_2.append(radio)
                            radio_group.append([radio])
                            count += 1

                        layout_2 = [[sg.Text('Choose a suburb', text_color='#BCC9C2', background_color='#27504B')],
                                    radio_group,
                                    [sg.Exit(key='-Exit-')]]

                        window_2 = sg.Window(title='', layout=layout_2, background_color='#27504B',
                                             use_custom_titlebar=True, titlebar_icon='',
                                             titlebar_background_color='#27504B')
                        while True:
                            event2, values2 = window_2.read()
                            if event2 == sg.WIN_CLOSED or event2 == '-Exit-':
                                window_2.close()
                                second_window = False
                                window.UnHide()
                                break

                    if multiple_postcode:
                        count = 0
                        for r in radio_group_2:
                            if r.get():
                                latitude = postcode_data[count]['latitude']
                                longitude = postcode_data[count]['longitude']
                                break
                            count += 1
                    else:
                        latitude = postcode_data[0]['latitude']
                        longitude = postcode_data[0]['longitude']

                    weather_data = current_weather(latitude, longitude)
                    update_window(window, weather_data)

    window.close()


if __name__ == '__main__':
    main()
