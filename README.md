
# TodayWeather
오늘 날씨 조회하여 DB(MySQL)에 저장하는 파이썬 애플리케이션

## 패키지
pip install requests
pip install PyMysql

## 필요 계정
https://openweathermap.org/


## 설정 파일
**config.ini**
```
[ENV]
LOG_FILE_PATH = C:\Downloads\imsi\log\\
LOG_LEVEL = DEBUG

[OPENWEATHER]
API_KEY=(발급 API KEY)
CITY=Seoul
LANG=kr

[MYSQL]
USER_ID=(아이디)
PASSWORD=(패스워드)
DB=(DB명)
```

