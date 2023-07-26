import requests
import json
from logger import getLogger
from config import loadConfig
from openweathermap import *
from weatherRepo import *

log = getLogger('TodayWeather')

def main():
    config = loadConfig()

    data = weather()

    log.debug("===> " + data["name"] + "의 날씨입니다.")
    log.debug("날씨는 "+ data["weather"][0]["description"] + "입니다.")
    log.debug("현재 온도는 " + str(data["main"]["temp"]) + "입니다.")
    log.debug("하지만 체감 " + str(data["main"]["feels_like"]) + "일 거에요.")
    log.debug("최저 기온은 " + str(data["main"]["temp_min"]) + "입니다.")
    log.debug("최고 기온은 " + str(data["main"]["temp_max"]) + "입니다.")
    log.debug("습도는 " + str(data["main"]["humidity"]) + "입니다.")
    log.debug("기압은 " + str(data["main"]["pressure"]) + "입니다.")
    log.debug("풍향은 " + str(data["wind"]["deg"]) + "입니다.")
    log.debug("풍속은 " + str(data["wind"]["speed"]) + "입니다.")

    saveWeather(data)
    
if __name__ == '__main__':
    main()