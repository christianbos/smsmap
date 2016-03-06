import requests

url = 'https://rest.nexmo.com/sms/json?'
params = {'api_key': 'eb36559d',
        'api_secret': '38329e3cf2767439',
        'from': 'SMS Helper',
        'to': '5215537740689',
        'type': 'text',
        'text': 'HelpSMS MAPATON YUJUU'}
r = requests.get(url, params=params)
