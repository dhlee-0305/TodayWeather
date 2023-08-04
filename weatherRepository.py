import pymysql
import json

from logger import getLogger
from mysql import *
from elapsed import elapsed

log = getLogger('weatherRepo')

@elapsed
def w_info_all():
    sql = 'SELECT * FROM w_info'
    rows = select(sql)
    log.debug(rows)

@elapsed
def w_info_seq(seq):
    sql = f'SELECT * FROM w_info WHERE seq={seq}'
    rows = select(sql)
    log.debug(rows)

@elapsed
def saveWeather(data):
    con = dbConnect()
    cur = con.cursor()
    
    sql_w_info = 'INSERT INTO w_info(base, visibility, dt, timezone, id, w_name, cod) VALUES(%s, %s, %s, %s, %s, %s, %s)'
    vals_w_info = (data.get('base'), \
            data.get('visibility'), \
            str(data.get('dt')), \
            str(data.get('timezone')), \
            str(data.get('id')), \
            str(data.get('name')), \
            data.get('cod'))
    log.debug('vals_w_info: ' + str(vals_w_info))
    cur.execute(sql_w_info, vals_w_info)
    seq = cur.lastrowid

    sql_coord = 'INSERT INTO w_coord(seq, lon, lat) VALUES(%s, %s, %s)'
    vals_coord = (seq, \
                str(data.get('coord').get('lon')), \
                str(data.get('coord').get('lat')))
    log.debug('vals_coord: ' + str(vals_coord))
    cur.execute(sql_coord, vals_coord)

    sql_weather = 'INSERT INTO w_weather(seq, id, main, description, icon) VALUES(%s, %s, %s, %s, %s)'
    vals_weather = (seq, \
                    data.get('weather')[0].get('id'), \
                    str(data.get('weather')[0].get('main')), \
                    str(data.get('weather')[0].get('description')), \
                    str(data.get('weather')[0].get('icon')))
    log.debug('vals_weather: ' + str(vals_weather))
    cur.execute(sql_weather, vals_weather)
    
    sql_main = 'INSERT INTO w_main(seq, temp, feels_like, temp_min, temp_max, pressure, humidity, sea_level, grnd_level) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
    vals_main = (seq, \
                data.get('main').get('temp'), \
                data.get('main').get('feels_like'), \
                data.get('main').get('temp_min'), \
                data.get('main').get('temp_max'), \
                data.get('main').get('pressure'), \
                data.get('main').get('humidity'), \
                data.get('main').get('sea_level'), \
                data.get('main').get('grnd_level'))
    log.debug('vals_main: ' + str(vals_main))
    cur.execute(sql_main, vals_main)

    sql_wind = 'INSERT INTO w_wind(seq, speed, deg, gust) VALUES(%s, %s, %s, %s)'
    vals_wind = (seq, \
                data.get('wind').get('speed'), \
                data.get('wind').get('deg'), \
                data.get('wind').get('gust'))
    log.debug('vals_wind: ' + str(vals_wind))
    cur.execute(sql_wind, vals_wind)

    sql_clouds = 'INSERT INTO w_clouds(seq, w_all) VALUES(%s, %s)'
    vals_clouds = (seq, data.get('clouds').get('all'))
    log.debug('vals_clouds: ' + str(vals_clouds))
    cur.execute(sql_clouds, vals_clouds)

    sql_sys = 'INSERT INTO w_sys(seq, w_type, id, country, sunrise, sunset) VALUES(%s, %s, %s, %s, %s, %s)'
    vals_sys = (seq, \
                data.get('sys').get('type'), \
                data.get('sys').get('id'), \
                str(data.get('sys').get('country')), \
                str(data.get('sys').get('sunrise')), \
                str(data.get('sys').get('sunset')))
    log.debug('vals_sys: ' + str(vals_sys))
    cur.execute(sql_sys, vals_sys)

    con.commit()
    con.close()

    return seq

if __name__ == '__main__':
    # data = '{"coord": {"lon": 126.9778, "lat": 37.5683}, "weather": [{"id": 802, "main": "Clouds", "description": "구름조금", "icon": "03d"}], "base": "stations", "main": {"temp": 30.66, "feels_like": 34.61, "temp_min": 28.69, "temp_max": 30.66, "pressure": 1015, "humidity": 62, "sea_level": 1015, "grnd_level": 1009}, "visibility": 10000, "wind": {"speed": 2.89, "deg": 226, "gust": 4.6}, "clouds": {"all": 37}, "dt": 1690337368, "sys": {"type": 1, "id": 5509, "country": "KR", "sunrise": 1690317018, "sunset": 1690368397}, "timezone": 32400, "id": 1835848, "name": "Seoul", "cod": 200}'
    # data = json.loads(data)
    # seq = saveWeather(data)
    # w_info_seq(seq)
    w_info_seq(38)
