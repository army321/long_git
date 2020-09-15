#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import configparser

"""
处理多次封号数据
判断账号区服情况，然后插入到已有数据中
#读取ini配置，筛选出多次封号源数据，筛选包含区服信息的数据

生成简单的界面，在界面上输入需要提取的路径即可生成最终文件。
修改了一些函数的返回，让函数不再互相调用，统一返回后再处理。

"""


def write_log(log):
    logfile = open("fenghao_log.txt", "a", encoding="utf-8")

    t1 = time.time()
    time_local = time.localtime(t1)
    t2 = time.strftime("%Y-%m-%d %H:%M:%S", time_local)

    logfile.write(t2 + " : " + log + "\n")
    logfile.close


def read_ini():
    try:
        write_log("read ini start...")
        config = configparser.ConfigParser()
        config.read("fenghao.ini", encoding="utf-8")

        source_file_name = config.get("fenghao", "source_file_name")
        source_mutant_file_name = config.get("fenghao", "source_totalMutant_name")
        serverName = config.get("fenghao_ini", "serverName")
        MailServerName = config.get("fenghao_ini", "MailServerName")

    except:
        write_log("read ini error...")

    # 读取的ini内容全部返回，按需使用，返回的是一个List。
    return (source_file_name, source_mutant_file_name, serverName, MailServerName)


# file_name = tk.StringVar()



def read_txt(source_path, source_file_name):
    write_log("read txt start...")
    f = open(source_path + source_file_name, "r", encoding="utf-8")
    dataList1 = []
    try:
        for l in f:
            strlist = l.split(",")
            if len(strlist) == 4:
                dataList1.append(strlist)
    except:
        write_log(" open txt file error")

    f.close
    # write_txt(dataList1,script_path)
    return dataList1  # 把读取后的list返回


# 多开封号
def read_multiple_txt(source_path, source_file_name):

    write_log("read txt start...")
    f = open(source_path + source_file_name, "r", encoding="utf-8")
    dataList1 = []
    try:
        for l in f:
            strlist = l.split(",")
            if len(strlist) == 4:

                dataList1.append(strlist)
    except:
        write_log(" open txt file error")

    f.close
    # write_multiple_txt(dataList1,script_path)
    return dataList1


# 多次开挂增加封号时间
def write_txt(txt, script_path, serverName):
    # print(txt, script_path, serverName)
    write_log("write sql start...")
    datalist = txt
    t1 = time.time()
    print("写入时的服务器名{}".format(serverName))
    for i in serverName:
        server_name_list = i.split(",")
        f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
        for strlist in datalist:
            if strlist[0] == server_name_list[0]:

                # f1 = open(script_path+server_name_list[1],'a',encoding = 'ansi')
                #
                #    for value in range(0,len(strlist)-3):
                t2 = int(t1) + 24 * 3600 * 30 * int(strlist[3])
                str1 = str(
                    "\n"
                    + "delete from  `status` where owner_id = "
                    + strlist[1]
                    + " and status = 19 limit 5;"
                )
                str2 = str(
                    "\n"
                    + "INSERT INTO `status`(`owner_id`,`status`,`power`,`sort`,`end_time`) VALUES ("
                    + strlist[1]
                    + ",19,1,19,"
                    + str(t2)
                    + ");"
                )
                f1.write(str1)
                f1.write(str2)
        f1.write("\n")
        f1.close


def write_multiple_txt(txt, script_path, serverName, MailServerName):
    write_log("write sql start...")
    datalist = txt
    t1 = time.time()
    for i in serverName:
        server_name_list = i.split(",")
        for strlist in datalist:
            if strlist[0] == server_name_list[0]:

                multiple_time = int(strlist[3])

                if multiple_time >= 3:
                    f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
                    t2 = int(t1) + 24 * 3600
                    # str1 = str("\n"+"delete from  `status` where owner_id = "+strlist[1]+" and status = 19 limit 5;")
                    str2 = str(
                        "\n"
                        + "INSERT INTO `status`(`owner_id`,`status`,`power`,`sort`,`end_time`) VALUES ("
                        + strlist[1]
                        + ",19,1,19,"
                        + str(t2)
                        + ");"
                    )
                    # f1.write(str1)
                    f1.write(str2)

                    f1.close

    for i in MailServerName:
        server_name_list = i.split(",")
        t3 = int(t1) + 24 * 3600 * 7
        today_time = time.strftime("%y%m%d0000", time.localtime(time.time()))
        for strlist in datalist:
            if strlist[0] == server_name_list[0]:

                multiple_time = int(strlist[3])
                if multiple_time >= 3:
                    f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
                    str1 = str("\n" + "set names gbk;")
                    f1.write(str1)
                    f1.close
                    break

        for strlist in datalist:
            if strlist[0] == server_name_list[0]:

                multiple_time = int(strlist[3])
                if multiple_time >= 3:
                    f1 = open(script_path + server_name_list[1], "a", encoding="ansi")
                    str2 = str(
                        "\n"
                        + "insert into mails (tar_user_id,prop,title,content,send_time,due_time,item1,item1_prop,item2,item2_prop,item3,item3_prop,item4,item4_prop,item5,item5_prop) values("
                        + strlist[1]
                        + ',1,"客服中心","亲爱的英魂玩家，检测到您使用多开软件进行游戏，已为您封停账号，为了您的账号安全，请勿使用非法软件进行游戏，祝您游戏愉快！",'
                        + str(today_time)
                        + ","
                        + str(t3)
                        + ",0,0,0,0,0,0,0,0,0,0);"
                    )
                    f1.write(str2)

                    f1.close


def get_file_name(file_name):
    # file_name = t1.get()
    new_file_name = eval(
        repr(file_name).replace(r"\\", r"/")
    )  # 先repr将字符串转为python原生字符串，再转换，最后eval转回正常字符串

    write_log("开始执行")
    get_ini = read_ini()
    print(get_ini)

    # read_txt(source_path,source_file_name,script_path)
    get_doucifenghao = read_txt(new_file_name, get_ini[0])  # 多次封号提取
    h = get_ini[2].split(";")  # 区服对应的sql文件名转成 List
    write_txt(get_doucifenghao, new_file_name, h)

    get_doukaifenghao = read_multiple_txt(new_file_name, get_ini[1])  # 多开封号提取
    h1 = get_ini[3].split(";")  # 邮件区服对应的sql文件名转成 List
    write_multiple_txt(get_doukaifenghao, new_file_name, h, h1)

    write_log("执行完成")
    return('执行完成')