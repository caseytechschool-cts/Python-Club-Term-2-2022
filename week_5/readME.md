# Week 5: Python club

1. `pip install pyinstaller`

2. Remove the image reference from the `Layout` file that can be
found in the `top_image` variable.

3. Run in the terminal
`pyinstaller --onefile --noconsole <main script name>.py`

4. Open the `*.spec` file and add the following in the `pathex` list
`'.', '.\\venv\\Lib\\site-packages'`

5. Run in the terminal
`pyinstaller <main script name>.spec`

6. Check out the `dist` folder where you have the `EXE` file

Feel free to share the `EXE` file with your friends and family.

Requirement to run the EXE file:
User needs Internet connection to run the application. No other dependency.