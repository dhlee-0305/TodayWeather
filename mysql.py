import pymysql

from config import loadConfig
from logger import getLogger

config = loadConfig()
log = getLogger('mysql')

DB_EXCEPTION = -1

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
    except Exception as e:
        log.error(e)
        rows = DB_EXCEPTION
    finally:
        con.close()

    return rows

def delete(sql):
    try:
        con = dbConnect()
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    except Exception as e:
        log.error(e)
    finally:
        con.close()

def insert(sql, vals):
    try:
        con = dbConnect()
        cur = con.cursor()
        cur.execute(sql, vals)
        seq = cur.lastrowid
        con.commit()
    except Exception as e:
        log.error(e)
        seq = DB_EXCEPTION
    finally:
        con.close()    

    return seq

def insertEach(sqlList, valsList):
    try:
        con = dbConnect()
        cur = con.cursor()
        insertCount = 0
        for sql, vals in zip(sqlList, valsList):
            cur.execute(sql, vals)
            insertCount += 1

        con.commit()
    except Exception as e:
        log.error(e)
        insertCount = DB_EXCEPTION
    finally:
        con.close() 

    return insertCount

if __name__ == '__main__':
    fruit_name_list = ('apple', 'banana', 'grape', 'durian', 'orange')
    fruit_price_list = (5, 10, 20, 100, 8)
    sql = 'insert into insert_test(c_name, c_value) values(%s, %s)'
    sqls = []
    vals = []
    for fruit, price in zip(fruit_name_list, fruit_price_list):
        val = (fruit, price)
        vals.append(val)
        sqls.append(sql)
    
    count = insertEach(sqls, vals)
    print(count)

