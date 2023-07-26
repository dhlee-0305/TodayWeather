import requests
import json
from logger import getLogger
from config import loadConfig

def weather():
    log = getLogger('openweathermap')

    config = loadConfig()

    apiKey = config['OPENWEATHER']['API_KEY']
    city = config['OPENWEATHER']['CITY']
    lang = config['OPENWEATHER']['LANG']

    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}&units=metric"

    result = requests.get(api)
    #print(result.text)
    data = json.loads(result.text)

    log.debug(json.dumps(data, ensure_ascii=False, indent=2))

    return data

if __name__ == '__main__':
    weather()