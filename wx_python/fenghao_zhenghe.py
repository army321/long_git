#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time

"""
整理多个文档到一个文档中
导出扣分的sql
"""

serverName = [
    "南方一区,nf1_3307.sql",
    "南方二区,nf2_3307.sql",
    "南方三区,nf3_3307.sql",
    "北方一区,bf1_3307.sql",
    "北方二区,bf2_3307.sql",
    "华东一区,sh1_3307.sql",
    "华东二区,sh2_3306.sql",
    "网龙联盟服,lmf_3306.sql",
    "综合一区,zh1q_3306.sql",
    "综合二区,zh2q_3306.sql",
    "7K,7k7k_3307.sql",
]
serverName2 = [
    "南方一区,nf1_3308.sql",
    "南方二区,nf2_3308.sql",
    "南方三区,nf3_3308.sql",
    "北方一区,bf1_3308.sql",
    "北方二区,bf2_3308.sql",
    "华东一区,sh1_3308.sql",
    "华东二区,sh2_3306.sql",
    "网龙联盟服,lmf_3306.sql",
    "综合一区,zh1q_3306.sql",
    "综合二区,zh2q_3306.sql",
    "7K,7k7k_3308.sql",
]


print("-------------888888888这里print")


def test():
    print("-=====================888888888这里print")


def write_log(log):
    logfile = open("zhenghe.txt", "a", encoding="utf-8")

    t1 = time.time()
    time_local = time.localtime(t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    logfile.write(t2 + " : " + log + "\n")
    logfile.close


def read_txt_fuc(openfile, script_path):
    print(openfile)
    write_log("read txt start...")
    f = open(openfile, "r", encoding="utf-8")

    dataList1 = []
    try:
        for l in f:
            strlist = l.split(",")
            if len(strlist) == 3:
                dataList1.append(strlist)
    except:
        write_log(" open txt file error")

    f.close
    write_txt(dataList1, script_path)


def write_txt(txt, script_path):
    write_log("write sql start...")
    datalist = txt
    for i in serverName:
        server_name_list = i.split(",")
        f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
        for strlist in datalist:
            if strlist[0] == server_name_list[0]:
                for value in range(0, len(strlist) - 2):
                    str1 = str(
                        "\n"
                        + "update game_note set score = score - 500, historymaxscore = historymaxscore - 500, season_max_score = season_max_score - 500 where roleid  = "
                        + strlist[value + 1]
                        + " and gamemode in (1101,1102) and score >500 and historymaxscore >500 limit 5;"
                    )
                    f1.write(str1)

        f1.close

    for i in serverName2:
        server_name_list = i.split(",")
        f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
        for strlist in datalist:
            if strlist[0] == server_name_list[0]:
                for value in range(0, len(strlist) - 2):
                    str1 = str(
                        "\n"
                        + "update dota_profiles set score = score - 500, max_score = max_score - 500 where userid  = "
                        + strlist[value + 1]
                        + " and gamemode in (1101,1102) and score >500 and max_score >500 limit 5;"
                    )
                    f1.write(str1)

        f1.close


def get_server_info(path):
    # print('{}  {}'.format(path,serverIP))
    server_info = []
    # write_log("相关服务器信息如下：\n")
    for root, dirs, files in os.walk(path):
        for i in files:
            server_info.append(i)  # 把服务器信息打到log中
    print(server_info)

    # return server_info
    new_file_path = "{}\\{}".format(path, "外挂封号")
    # 如果没有文件夹，则创建一个文件夹用于存放生成后的数据
    print(new_file_path)
    if not os.path.exists(new_file_path):
        os.makedirs(new_file_path)

    openfile = path + "totaldata.txt"

    # 把所有文件读到一个文件中
    for i in server_info:
        print(i)
        print(path + i)
        file_name = path + i
        fs = open(file_name, "r", encoding="utf-8")
        read_txt = fs.read()

        fw = open(openfile, "a", encoding="utf-8")
        fw.write(read_txt)
        fs.close
        fw.close

    read_txt_fuc(openfile, new_file_path + "\\")


def get_file_name(file_name):
    # 先repr将字符串转为python原生字符串，再转换，最后eval转回正常字符串
    new_file_name = eval(repr(file_name).replace(r"\\", r"/"))

    # write_log("开始执行")
    # get_ini = read_ini()
    print(new_file_name)
    get_server_info(new_file_name)
    return "执行完成"
