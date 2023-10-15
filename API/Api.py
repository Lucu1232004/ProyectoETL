import requests

url = 'http://api.openweathermap.org/data/2.5/forecast?'
data = requests.get(url)
if data.status_code == 200:
    data = data.json()
    for e in data ['data']:
        print(e['title'])
