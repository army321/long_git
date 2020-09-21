#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import time
import datetime
import configparser

"""
指定文档整合到一个文档中

"""


def write_log(log):
    logfile = open("pvp_sql_zhenghe.txt", "a", encoding="utf-8")

    t1 = time.time()
    time_local = time.localtime(t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    logfile.write(t2 + " : " + log + "\n")
    logfile.close


def read_ini():
    try:
        write_log("read ini start...")
        config = configparser.ConfigParser()
        config.read("pvp_sql_zhenghe.ini")

        write_log("read ini start...2222")
        top_bezi_path = config.get("sql_path", "top_bezi_path")
        fenduan_beizi_path = config.get("sql_path", "fenduan_beizi_path")
        sql_beizi_path = config.get("sql_path", "sql_beizi_path")
        write_log("read ini start...3333")
        top_bezi_name = config.get("sql_select", "top")
        fenduan_beizi_fz_name = config.get("sql_select", "fz")
        fenduan_beizi_jz_name = config.get("sql_select", "jz")
        sql_title = "update role_list set expand_attr = expand_attr &(~8190);"

        for i in range(1, 12):
            print("read_ini111")
            get_dbname = config.get("dbname", str(i))
            print(get_dbname)

            sql_beizi = sql_beizi_path + get_dbname + top_bezi_name
            top_bezi = top_bezi_path + get_dbname + top_bezi_name
            fenduan_beizifz = fenduan_beizi_path + get_dbname + fenduan_beizi_fz_name
            fenduan_beizijz = fenduan_beizi_path + get_dbname + fenduan_beizi_jz_name
            print(sql_beizi + top_bezi + fenduan_beizifz + fenduan_beizijz + sql_title)
            write_sql(sql_beizi, top_bezi, fenduan_beizifz, fenduan_beizijz, sql_title)

    except:
        write_log("read ini error...")


def write_sql(
    sql_beizi, top_bezi_path, fenduan_beizi_path_fz, fenduan_beizi_path_jz, sql_title
):
    try:
        write_log("open file...")

        fw = open(sql_beizi, "a")

        fw.write(sql_title)

        fs = open(top_bezi_path, "r")
        read_txt = fs.read()
        fs.close
        fw.write(read_txt)

        fs = open(fenduan_beizi_path_fz, "r")
        read_txt = fs.read()
        fs.close
        fw.write(read_txt)

        fs = open(fenduan_beizi_path_jz, "r")
        read_txt = fs.read()
        fs.close
        fw.write(read_txt)

        fw.close

    except:
        write_log("open  error...")


if __name__ == "__main__":
    write_log("开始执行")
    print("开始执行")
    read_ini()
    print("执行完成")
    write_log("执行完成")

