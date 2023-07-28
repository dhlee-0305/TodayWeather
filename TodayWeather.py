import requests
import json
from logger import getLogger
from config import loadConfig
from openweathermap import *
from weatherRepo import *

log = getLogger('TodayWeather')

def main():
    config = loadConfig()

    weatherData = weather()
    printWeather(weatherData)

    saveWeather(weatherData)
    
if __name__ == '__main__':
    main()