import pymysql

# 公用的连接数据库方式，返还查询到的结果。
def connect_mysql(dbname, chuan_sql):
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "passwd": "123456",
        "db": dbname,
    }

    con = pymysql.connect(**config)
    cur = con.cursor()
    sql = chuan_sql

    try:
        cur.execute(sql)
        result = cur.fetchall()
        con.close()  #关闭连接
        return result
    except:
        print("error!  select mysql error")

