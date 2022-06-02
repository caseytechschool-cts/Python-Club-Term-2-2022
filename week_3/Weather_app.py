import PySimpleGUI as sg


# Postcode API: http://v0.postcodeapi.com.au/suburbs/{postcode}.json
# reading image: https://www.adamsmith.haus/python/answers/how-to-read-an-image-data-from-a-url-in-python
# Weather API: http://api.weatherapi.com/v1/current.json?key={api_key}&q={latitude,longitude}&aqi=no


layout = layout_builder()
window = sg.Window(title='Weather app', layout=layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-button-':
        postcode = sg.popup_get_text(message='Enter a postcode',
                                     default_text='')

window.close()




