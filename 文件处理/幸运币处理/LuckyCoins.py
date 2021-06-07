#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
读取幸运币文件
整合生成文件

"""
# import os
# import datetime
# from openpyxl import load_workbook
import time
import configparser
from openpyxl import Workbook
import get_sql

# 异常捕获装饰器
def robust(actual_do):
    def add_robust(*args, **keyargs):
        try:
            time.sleep(1)
            return actual_do(*args, **keyargs)
        except:
            print("Error execute:{}".format(actual_do.__name__))
            time.sleep(5)

    return add_robust


# 装饰器测试代码，好像没啥用
def write_log_new(log):
    def outwrapper(func):
        def wrapper(*args, **keyargs):
            try:
                print(log)
                with open("幸运币log.txt", "a", encoding="utf-8") as logfile:
                    logfile.write(str(log) + "\n")
                return func(*args, **keyargs)
            except:
                print("Error execute:{}".format(func.__name__))

        return wrapper

    return outwrapper


@write_log_new("error")
@robust
def simple_test():
    return 5 / 0


# 获取时间 转成对应的格式
def get_time():
    t1 = time.time()
    time_local = time.localtime(t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
    return t2


# 记录log
def write_log(log):
    print(log)
    with open("幸运币log.txt", "a", encoding="utf-8") as logfile:
        logfile.write(str(log) + "\n")


# 读取ini
@robust
def read_ini():
    write_log("read_ini ... ")

    config = configparser.ConfigParser()
    config.read("LuckyCoins.ini", encoding="utf-8")

    source_file_name = config.get("sql_path", "source_file_name")
    script_path = config.get("sql_path", "script_path")
    db_name = config.get("dbname", "db_name")
    script_file_name = config.get("sql_path", "script_file_name")
    add_num = config.get("sql_path", "add_num")
    return (source_file_name, script_path, db_name, script_file_name, add_num)


# 读取原始数据，并返回一个列表
@robust
def read_userid_txt(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        data = f.readlines()
        user_info = []
        for i in data:
            user_info.append(i.strip("\n"))
        return user_info


# 定义查找语句
def select_line(userid_num):
    sql_line1 = "select iduser, quest_id, data2 from dotarole_task"
    sql_line2 = " where  quest_id =101030 and iduser = "
    sql_line3 = " limit 1;"
    dotarole_task = int(userid_num / 200000)

    select_sql = "{0}{1}{2}{3}{4}".format(
        sql_line1, dotarole_task, sql_line2, userid_num, sql_line3
    )
    # select iduser, quest_id, data2 from dotarole_task13 where  quest_id =101030 and iduser =  2664224 limit 1;

    return select_sql


def insert_sql(userid,lucky_coins_num,add_num):
    delete_sql = "DELETE FROM `dotarole_task{0}` WHERE `iduser`={1} and quest_id =101030 limit 1;\n".format(
        int(userid / 200000), userid
    )
    insert_sql = "INSERT INTO `dotarole_task{0}` (`iduser`, `quest_id`, `type`, `complete_flag`, `data1`, `data2`, `data3`, `data4`, `data5`, `data6`, `data7`, `begin_time`, `end_time`, `area_id`) VALUES ({1}, 101030, 2, 0, 0, {2}, 0, 0, 0, 0, 0, 210402, 0, 0);\n".format(
        int(userid / 200000), userid, lucky_coins_num + int(add_num)
    )

    return(delete_sql,insert_sql)

# 根据userid读取sql返还内容
@robust
def get_sql_result(dbname, userid, file_path, filename, add_num):

    get_all_result = []
    write_log("输出sql文件...")
    for i in userid:
        userid_num = int(i)
        all_sql = select_line(userid_num)
        try:
            result = get_sql.connect_mysql(dbname, all_sql)
            get_all_result.append(result)

            with open(file_path + filename + ".sql", "a", encoding="ansi") as f1:
                for j in range(1, len(result) + 1):
                    userid = result[j - 1][0]
                    lucky_coins_num = result[j - 1][2]
                    print(userid, lucky_coins_num)

                    sql_line=insert_sql(userid,lucky_coins_num,add_num)

                    f1.write(sql_line[0])
                    f1.write(sql_line[1])
        except:
            write_log("userid_num= {0} , 对应的表  dotarole_task{1}  不存在".format(userid_num,int(userid_num/200000)))


    write_log("输出sql文件...完成  OK")

    return get_all_result


# 把查询的结果导出一份txt
@robust
def output_txt(file_path, filename, get_all_result):

    write_log("输出txt文件...")
    with open(file_path + filename + "结果.txt", "a", encoding="ansi") as f1:
        for j in get_all_result:
            f1.write("{}\n".format(j))
    write_log("输出txt文件...完成  OK")


if __name__ == "__main__":
    write_log("--------------{0} 开始执行--------------".format(get_time()))
    # simple_test()

    # 读取ini配置
    # return (source_file_name, script_path, db_name, script_file_name, add_num)
    get_ini = read_ini()

    # 读取对应区服的角色名
    get_user_info = read_userid_txt(get_ini[0])

    # 根据角色名和配置信息，查找数据库中的信息，并生成sql语句
    all_result = get_sql_result(
        get_ini[2], get_user_info, get_ini[1], get_ini[3], get_ini[4]
    )

    # 把所有查找内容写入txt文件中
    output_txt(get_ini[1], get_ini[3], all_result)

    write_log("--------------{0} 执行完成--------------".format(get_time()))
