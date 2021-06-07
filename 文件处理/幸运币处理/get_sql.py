import pymysql
import configparser

# 公用的连接数据库方式，返还查询到的结果。
# 数据库配置读取ini


def connect_mysql(dbname, chuan_sql):
    config = configparser.ConfigParser()
    config.read("mysql_setting.ini", encoding="utf-8")

    host_name= config.get("mysql_setting", "host")
    port_name = config.get("mysql_setting", "port")
    user_name = config.get("mysql_setting", "user")
    passwd_txt = config.get("mysql_setting", "passwd")

    config = {
        "host": host_name,
        "port": int(port_name),
        "user": user_name,
        "passwd": passwd_txt,
        "db": dbname,
    }

    con = pymysql.connect(**config)
    cur = con.cursor()
    sql = chuan_sql

    try:
        cur.execute(sql)
        result = cur.fetchall()
    except:
        print("表不存在")
    con.close()  #关闭连接
    return result

