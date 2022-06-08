# Week 4: Python club


## Task 1: Discussion, do you want a programming club for the next term?
Share your ideas about what you like, what we are missing and where we have
scope for improvements. 

## Task 2: Working with API
Last week, you have started working with API. To get the data into your Python 
program you need to install a package. You need the `requests` package to access
data from an API.

Copy the following line and paste it into the PyCharm terminal and press Enter

`pip install requests`

## Jargon's to remember
1. `Front-end:`
2. `Back-end:`
3. `Full-stack:`

## Task 3: Getting the postcode data

```python
import requests
url = f'http://v0.postcodeapi.com.au/suburbs/{postcode}.json'
response = requests.get(url)
data = response.json()
```

## Task 4: Passing the postcode data to the weather API
```python
url = f'http://api.weatherapi.com/v1/current.json?key={key}&q={latitude},{longitude}&aqi=no'
response = requests.get(url)
data = response.json()
```
