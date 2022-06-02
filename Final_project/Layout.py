import PySimpleGUI as sg


def layout_builder():
    top_info = [[sg.Text(text='Noble Park', font='Courier 20 bold', text_color='#BCC9C2',
                         key='-location-', background_color='#27504B')],
                [sg.Text(text='Cloudy', font='Courier 12', text_color='#BCC9C2', size=(30, 3),
                         key='-weather_oneline-', background_color='#27504B')]
                ]
    top_image = sg.Image(key='-weather_image-', background_color='#27504B',
                         filename='download.png')

    middle_temp = [[sg.Text(text='19.5°C', font='Verdana 30 bold', text_color='#BCC9C2', key='-temp-',
                            background_color='#27504B')]]

    middle_stats = [[sg.Text(text='Feels-like', font='Courier 12', text_color='#BCC9C2',
                             key='-feels_like-', background_color='#27504B'), sg.Push(background_color='#27504B'),
                     sg.Text(text='15.0°C', font='Courier 12 bold', text_color='#BCC9C2',
                             key='-feels_like_value-', background_color='#27504B')],

                    [sg.Text(text='Wind', font='Courier 12', text_color='#BCC9C2', key='-wind-',
                             background_color='#27504B'), sg.Push(background_color='#27504B'),
                     sg.Text(text='45km/h', font='Courier 12 bold', text_color='#BCC9C2', key='-wind_value-',
                             background_color='#27504B')],

                    [sg.Text(text='Humidity', font='Courier 12', text_color='#BCC9C2', key='-humidity-',
                             background_color='#27504B'), sg.Push(background_color='#27504B'),
                     sg.Text(text='65%', font='Courier 12 bold', text_color='#BCC9C2', key='-humidity_value-',
                             background_color='#27504B')],

                    [sg.Text(text='Percip', font='Courier 12', text_color='#BCC9C2', key='-precip-',
                             background_color='#27504B'), sg.Push(background_color='#27504B'),
                     sg.Text(text='None', font='Courier 12 bold', text_color='#BCC9C2', key='-precip_value-',
                             background_color='#27504B')],

                    [sg.Text(text='Pressure', font='Courier 12', text_color='#BCC9C2', key='-pressure-',
                             background_color='#27504B'), sg.Push(background_color='#27504B'),
                     sg.Text(text='1011 hPa', font='Courier 12 bold', text_color='#BCC9C2',
                             key='-pressure_value-', background_color='#27504B')]
                    ]
    bottom_info = [sg.Text(text='Updated: May 27 07:56:41 PM', font='Courier 8', text_color='#BCC9C2',
                           key='-updated_on-', background_color='#27504B'),
                   sg.Button(button_text='click to change city', button_color='#27504B', font='Courier 8 italic'
                             , key='-button-')]

    layout = [[sg.Column(top_info, background_color='#27504B'), sg.Push(background_color='#27504B'), top_image,
               sg.Push(background_color='#27504B')],
              [sg.Column(middle_temp, background_color='#27504B'), sg.Column(middle_stats, background_color='#27504B')],
              [bottom_info]
              ]
    return layout

