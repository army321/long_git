#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
荣誉战场发奖数据
前100名根据排名和分数发奖
超过100名根据分数发奖
前100还有勋章奖励
"""
import os
import pymysql
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import datetime
import configparser
import csv

reward = {
    1: 300000,
    2: 250000,
    3: 200000,
    4: 160000,
    5: 120000,
    6: 90000,
    7: 60000,
    8: 30000,
}
reward_title = {
    1: "大元帅",
    2: "元帅",
    3: "大将军",
    4: "将军",
    5: "大都统",
    6: "都统",
    7: "大统领",
    8: "统领",
}


# 记录log
def write_log(log):
    logfile = open("荣誉战场奖励log.txt", "a", encoding="utf-8")

    t1 = time.time()
    time_local = time.localtime(t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    logfile.write(t2 + " : " + log + "\n")
    logfile.close

# 读取ini
def read_ini():
    print("read_ini")

    try:
        write_log("read ini start...")
        config = configparser.ConfigParser()
        config.read("rongyuzhanchang.ini", encoding="utf-8")

        excel_path = config.get("sql_path", "excel_path")
        script_path = config.get("sql_path", "script_path")
        column_name = config.get("column_name", "column")
        sql = config.get("sql_select", "sql_ini")

        for i in range(1, 2):
            print("read_ini111")
            get_dbname = config.get("dbname", str(i))
            print(get_dbname)
            write_excel_xlsx(
                get_dbname, get_dbname, column_name, sql, excel_path, script_path
            )
    except:
        write_log("read ini error...")
        print("err")


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

    # sql = '(select * from  dota_storage4 where owner_id =  440833 )union all (select * from  dota_storage9 where owner_id =  902624 )'

    try:
        cur.execute(sql)
        result = cur.fetchall()
        # print("select ::::",result)
        return result
    except:
        print("error!  select mysql error")

    con.close()


##can support excel 2007 ,support xlsx.  becouse .xls only support 65535 row

def write_excel_xlsx(dbname, file_name, column_name, sql, excel_path, script_path):
    wb = Workbook()
    sheet = wb.active

    result = connect_mysql(dbname, sql)

    fileds = column_name.split(",")
    idnum = 0

    dataList1 = []
    dataList_top100 = []
    try:
        write_log("判断排名")
        sheet.append(fileds)
        for row in range(1, len(result) + 1):
            idnum = idnum + 1
            sheet.cell(row=row + 1, column=1, value=idnum)
            userid = result[row - 1][0]
            # print(userid)
            area_id = result[row - 1][3]
            if idnum <= 100:
                dataList_top100.append(userid)
                dataList_top100.append(idnum)

                sheet.cell(row=row + 1, column=12, value=idnum)
                sheet.cell(row=row + 1, column=13, value=userid)
                attr = order_expand_attr(idnum)
                sheet.cell(row=row + 1, column=14, value=attr)

            # print(area_id)
            for col in range(0, len(fileds) - 1):
                sheet.cell(row=row + 1, column=col + 2, value=result[row - 1][col])
                try:
                    # write_log("判断排名")
                    if col == 2:
                        order = order_num(idnum, result[row - 1][col])
                        reward_num = reward.get(order)
                        reward_title_txt = reward_title.get(order)
                        sheet.cell(row=row + 1, column=7, value=order)
                        sheet.cell(row=row + 1, column=8, value=reward_num)
                        sheet.cell(row=row + 1, column=9, value=reward_title_txt)
                        sheet.cell(row=row + 1, column=10, value=area_id)

                        # write_log(sql_num)
                        dataList1.append(userid)
                        dataList1.append(area_id)
                        dataList1.append(reward_num)
                except:
                    write_log("error! 判断排名  error")
    except:
        print("error! write excel error")

    wb.save(excel_path + file_name + ".xlsx")
    print("baocun cheng gong")

    write_top100_sql(script_path, file_name, dataList_top100)
    write_sql(script_path, file_name, dataList1)


def write_top100_sql(script_path, filename, dataList1):
    write_log("write write_top100_sql start...")
    f1 = open(script_path + filename + ".sql", "a", encoding="ansi")

    f1.write("update role_list set expand_attr = expand_attr &(~8257536);\n")

    print(script_path + filename + ".sql")
    # print(filename)
    print(dataList1)

    try:
        for strlist in range(0, int(len(dataList1) / 2)):
            userid = dataList1[strlist * 2]
            idnum = dataList1[strlist * 2 + 1]
            expand_attr = order_expand_attr(idnum)
            k = (
                "update role_list set expand_attr = expand_attr |"
                + str(expand_attr)
                + " where id =  "
                + str(userid)
                + " limit 1;\n"
            )

            f1.write(k)
    except:
        write_log("写write_top100_sql错误")

    write_log("close f1")
    f1.close


def write_sql(script_path, filename, dataList1):
    write_log("write sql start...")
    f1 = open(script_path + filename + ".sql", "a", encoding="ansi")

    print(script_path + filename + ".sql")
    # print(filename)
    print(dataList1)

    try:
        for strlist in range(0, int(len(dataList1) / 3)):
            userid = dataList1[strlist * 3]
            area_id = dataList1[strlist * 3 + 1]
            reward = dataList1[strlist * 3 + 2]

            fenbiao = int(int(userid) / 1000000)

            # 	update role_list set expand_attr = expand_attr |131072 where id = 1136027 limit 1;

            k = (
                "update `pve_role_list"
                + str(fenbiao)
                + "` set pve_hornor = pve_hornor + "
                + str(reward)
                + " where role_id =  "
                + str(userid)
                + " and area_id =  "
                + str(area_id)
                + " limit 1;"
                + "\n"
            )

            # 	k = str(userid)+","+str(area_id)+","+str(reward)+","+"\n"
            f1.write(k)
    except:
        write_log("写sql错误")

    write_log("close f1")
    f1.close


def order_num(num, score):
    if score >= 400000:
        if num < 11:
            return 1
        elif num < 101:
            return 2
        else:
            return 3
    elif score >= 350000:
        if num < 101:
            return 2
        else:
            return 3
    elif score >= 310000:
        return 3
    elif score >= 270000:
        return 4
    elif score >= 230000:
        return 5
    elif score >= 200000:
        return 6
    elif score >= 170000:
        return 7
    else:
        return 8


def order_expand_attr(num):
    if num == 1:
        return 131072
    elif num == 2:
        return 262144
    elif num == 3:
        return 524288
    elif num < 11:
        return 1048576
    elif num < 51:
        return 2097152
    elif num < 101:
        return 4194304
    else:
        write_log("判断 expand_attr 错误")


if __name__ == "__main__":
    read_ini()
    print("zhixing wan cheng")

