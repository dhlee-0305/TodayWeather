import pymysql

from config import loadConfig
from logger import getLogger

config = loadConfig()
log = getLogger('mysql')

def dbConnect():
    user_id=config['MYSQL']['USER_ID']
    password=config['MYSQL']['PASSWORD']
    db=config['MYSQL']['DB']

    con = pymysql.connect(host='localhost', user=user_id, password=password, db=db, charset='utf8')
    return con

def select(sql):
    try:
        con = dbConnect()
        cur = con.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
    finally:
        con.close()

    return rows

def delete(sql):
    try:
        con = dbConnect()
        cur = con.cursor()
        cur.execute(sql)
        cur.commit()
    finally:
        con.close()

def insert(sql, vals):
    try:
        con = dbConnect()
        cur = con.cursor()
        cur.execute(sql, vals)
        seq = cur.lastrowid
        cur.commit()
    finally:
        con.close()    

    return seq