import pymysql
import json

from logger import getLogger
from mysql import *

log = getLogger('weatherRepo')

def w_info_all():
    con = dbConnect()
    cur = con.cursor()
    sql = 'SELECT * FROM w_info'
    cur.execute(sql)
    rows = cur.fetchall()

    log.debug(rows)

    con.close()

def w_info_seq(seq):
    con = dbConnect()
    cur = con.cursor()
    sql = f'SELECT * FROM w_info WHERE seq={seq}'
    cur.execute(sql)
    rows = cur.fetchall()

    log.debug(rows)

    con.close()

def saveWeather(data):
    con = dbConnect()
    cur = con.cursor()
    
    sql = 'INSERT INTO w_info(base, visibility, dt, timezone, id, w_name, cod) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    vals = (data['base'], data['visibility'], str(data['dt']), str(data['timezone']), str(data['id']), str(data['name']), data['cod'])
    cur.execute(sql, vals)
    seq = cur.lastrowid
    log.debug(vals)

    sql_coord = 'INSERT INTO w_coord(seq, lon, lat) VALUES(%s, %s, %s)'
    vals_coord = (seq, str(data['coord']['lon']), str(data['coord']['lat']))
    log.debug(vals_coord)
    cur.execute(sql_coord, vals_coord)

    sql_weather = 'INSERT INTO w_weather(seq, id, main, description, icon) VALUES(%s, %s, %s, %s, %s)'
    vals_weather = (seq, data['weather'][0]['id'], str(data['weather'][0]['main']), str(data['weather'][0]['description']), str(data['weather'][0]['icon']))
    log.debug(vals_weather)
    cur.execute(sql_weather, vals_weather)
    
    sql_main = 'INSERT INTO w_main(seq, temp, feels_like, temp_min, temp_max, pressure, humidity, sea_level, grnd_level) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    vals_main = (seq, data['main']['temp'], data['main']['feels_like'], data['main']['temp_min'], data['main']['temp_max'], data['main']['pressure'], data['main']['humidity'], data['main']['sea_level'], data['main']['grnd_level'])
    log.debug(vals_main)
    cur.execute(sql_main, vals_main)

    sql_wind = 'INSERT INTO w_wind(seq, speed, deg, gust) VALUES(%s, %s, %s, %s)'
    vals_wind = (seq, data['wind']['speed'], data['wind']['deg'], data['wind']['gust'])
    log.debug(vals_wind)
    cur.execute(sql_wind, vals_wind)

    sql_clouds = 'INSERT INTO w_clouds(seq, w_all) VALUES(%s, %s)'
    vals_clouds = (seq, data['clouds']['all'])
    log.debug(vals_clouds)
    cur.execute(sql_clouds, vals_clouds)

    sql_sys = 'INSERT INTO w_sys(seq, w_type, id, country, sunrise, sunset) VALUES(%s, %s, %s, %s, %s, %s)'
    vals_sys = (seq, data['sys']['type'], data['sys']['id'], str(data['sys']['country']), str(data['sys']['sunrise']), str(data['sys']['sunset']))
    log.debug(vals_sys)
    cur.execute(sql_sys, vals_sys)

    con.commit()
    con.close()

    return seq

if __name__ == '__main__':
    # data = '{"coord": {"lon": 126.9778, "lat": 37.5683}, "weather": [{"id": 802, "main": "Clouds", "description": "구름조금", "icon": "03d"}], "base": "stations", "main": {"temp": 30.66, "feels_like": 34.61, "temp_min": 28.69, "temp_max": 30.66, "pressure": 1015, "humidity": 62, "sea_level": 1015, "grnd_level": 1009}, "visibility": 10000, "wind": {"speed": 2.89, "deg": 226, "gust": 4.6}, "clouds": {"all": 37}, "dt": 1690337368, "sys": {"type": 1, "id": 5509, "country": "KR", "sunrise": 1690317018, "sunset": 1690368397}, "timezone": 32400, "id": 1835848, "name": "Seoul", "cod": 200}'
    # data = json.loads(data)
    # seq = saveWeather(data)
    # w_info_seq(seq)
    w_info_seq(1)
