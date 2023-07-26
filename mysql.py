import pymysql

from config import loadConfig

config = loadConfig()

# def select(original_func):
#     def _db(*args, **kwargs):
#         con = pymysql.connect(host='localhost', user='dhlee', password='happy3119', db='study', charset='utf8')
#         result = original_func(*args, **kwargs)
#         con.close()
#         return result
#     return _db

def dbConnect():
    user_id=config['MYSQL']['USER_ID']
    password=config['MYSQL']['PASSWORD']
    db=config['MYSQL']['DB']

    con = pymysql.connect(host='localhost', user=user_id, password=password, db=db, charset='utf8')
    return con