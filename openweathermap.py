import requests
import json
from logger import getLogger
from config import loadConfig
from elapsed import elapsed
from time import *

log = getLogger('openweathermap')

@elapsed
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

def timeToString(dateStr=time()):
    tm = localtime(dateStr)
    return strftime('%Y-%m-%d %H:%M:%S', tm)

def printWeather(data):
    log.debug(data["name"] + "의 날씨입니다.")
    log.debug("날씨는 "+ data["weather"][0]["description"] + "입니다.")
    log.debug("현재 온도는 " + str(data["main"]["temp"]) + "입니다.")
    log.debug("하지만 체감 " + str(data["main"]["feels_like"]) + "일 거에요.")
    log.debug("최저 기온은 " + str(data["main"]["temp_min"]) + "입니다.")
    log.debug("최고 기온은 " + str(data["main"]["temp_max"]) + "입니다.")
    log.debug("습도는 " + str(data["main"]["humidity"]) + "입니다.")
    log.debug("기압은 " + str(data["main"]["pressure"]) + "입니다.")
    log.debug("풍향은 " + str(data["wind"]["deg"]) + "입니다.")
    log.debug("풍속은 " + str(data["wind"]["speed"]) + "입니다.")
    log.debug("일출은 " + timeToString(data.get('sys').get('sunrise')) + ' 입니다.')
    log.debug("일몰은 " + timeToString(data.get('sys').get('sunset')) + ' 입니다.')

if __name__ == '__main__':
    data = weather()
    print(data.get('wind').get('gust', '-'))