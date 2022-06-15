# Week 5: Python club

`pip install pyinstaller`

Remove the image reference from the `Layout` file that can be
found in the `top_image` variable.

Run in the terminal
`pyinstaller --onefile --noconsole <main script name>.py`

Open the `*.spec` file and add the following in the `pathex` list
`'.', '.\\venv\\Lib\\site-packages'`

Run in the terminal
`pyinstaller <main script name>.spec`

Check out the `dist` folder where you have the `EXE` file

Feel free to share the `EXE` file with your friends and family.

Requirement to run the EXE file:
User needs Internet connection to run the application. No other dependency.