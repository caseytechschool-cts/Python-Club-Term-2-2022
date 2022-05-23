# Building Graphical User Interface (GUI) using Python

This week we focus on how to build GUI using Python. There are many ways we could do it, some of them are harder then others, 
but each way comes with its pros and cons. Python's default library for GUI is `Tkinter` and it
ships with it. However, we will use another package/library which is easier to use for new users.

## Installing `pysimplegui`
1. Make sure you have internet connection.
2. Open an existing or new project in `pyCharm` and click on the `Terminal` tab from the bottom tray.
3. Copy and paste the following in the terminal and press `Enter`
   `pip install pysimplegui`
4. Wait until the installation process is finished.

## Activities
1. Design a GUI interface by hand using the provided pen and paper.
2. Keep it simple.
3. Level different section.
4. Translate the design into code.

For an example, please take a look the following design
![hand design](../media/hand-design.jpg)

## A starter code 

```python
import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
```
