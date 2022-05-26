import PySimpleGUI as sg

layout = [[sg.Text('Numerator')],
          [sg.Input(size=(12, 1))],
          [sg.Text('Denominator')],
          [sg.Input(size=(12, 1))],
          [sg.Text(key='output')],
          [sg.Button('Run')]]

window = sg.Window('Simple calculator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    numerator = float(values[0])
    denominator = float(values[1])
    result = numerator / denominator
    window['output'].update(result)

window.close()
