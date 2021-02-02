#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import datetime
import configparser
'''
根据充值的档位生成相应的充值记录
插入记录到指定表中

'''

cost_type = {6: 101, 30: 102, 68: 103, 128: 104, 328: 105, 648: 106}

sql_insert = "INSERT INTO `upay` (`type`, `account_id`, `userid`, `chk_sum`, `time_stamp`, `used`, `ordernumber`, `flag`, `card_in_time`, `itemid`, `ditch`, `ip`, `cost`, `originalPrice`, `currency`, `num`) VALUES "
NUM = 0

# 记录log
def write_log(log):
    print(log)
    with open("log_slg_pay.txt", "a", encoding="utf-8") as logfile:
        logfile.write(log + "\n")


def read_ini():
    try:
        write_log("开始读取基础 ini 配置...")
        config = configparser.ConfigParser()
        config.read("slg_cz.ini", encoding="utf-8")
        source_file_name = config.get("sql_path", "source_file_name")
        card_in_time = config.get("sql_path", "card_in_time")

    except:
        write_log("read ini error...")

    return (source_file_name, card_in_time)


# 读取原始数据，并返回一个列表
def read_userid_txt(fileName):
    with open(fileName, "r", encoding="utf-8") as f:
        data = f.readlines()
        user_info = []
        for i in data:
            user_info.append(i.strip("\n"))
        return user_info


# 拼接sql语句
def get_sql(user_info, card_in_time, serverName_dict):
    qudao = []
    # 获取渠道号
    for one_user_info in user_info:
        user_list = one_user_info.split(",")
        if len(user_list) == 5:
            qudao.append(user_list[4])
        else:
            write_log("{} 数据异常 ".format(one_user_info))
    # print('qudao {}'.format(qudao))
    get_qudao = set(qudao)  # set可以对列表去重， 剩下需要导出的区服
    # print(get_qudao)

    # 根据渠道号生成脚本
    for k in get_qudao:
        # print('渠道号：{},区服名：{}'.format(k,serverName_dict[k]))
        qudao_sql = []
        for one_user_info in user_info:
            user_list = one_user_info.split(",")
            if len(user_list) == 5:
                # print("开始处理 {},{},{},{},{} ".format(user_list[0],user_list[1],user_list[2],user_list[3],user_list[4]))
                if k == user_list[4]:
                    # print ("渠道号 {}".format(k))
                    get_pay_num = int(user_list[3])
                    pay_type = get_type(user_list[2])
                    userid = "{}{}".format(user_list[0], user_list[4])
                    chk_sum = get_chk_sum(pay_type, int(user_list[0]), int(userid))
                    for i in range(get_pay_num):
                        global NUM
                        NUM += 1
                        new_card_in_time = int(card_in_time) + NUM
                        # (`type`, `account_id`, `userid`, `chk_sum`, `time_stamp`,
                        # `used`, `ordernumber`, `flag`, `card_in_time`, `itemid`,
                        # `ditch`, `ip`, `cost`, `originalPrice`, `currency`, `num`)
                        insert_sql = "({0},{1},{2},{3},0,0,'{4}',0,{5},{6},{7},NULL,{8},{9},0,0)".format(
                            pay_type,
                            user_list[0],
                            userid,
                            chk_sum,
                            new_card_in_time,
                            new_card_in_time,
                            pay_type,
                            user_list[1],
                            int(user_list[2]) * 100,
                            int(user_list[2]) * 100,
                        )
                        qudao_sql.append(insert_sql)
                        # print(insert_sql),

            else:
                write_log("{} 数据异常 ".format(one_user_info))

        # print('汇总后 、、、、、{}'.format(qudao_sql))

        write_sql(serverName_dict[k], qudao_sql)
    return "ok"


def write_sql(qufu_name, fenquList):

    write_log("写入 {} 的内容，一共 {} 条".format(qufu_name, len(fenquList)))
    new_qufu_name = qufu_name + ".sql"
    if os.path.exists(qufu_name):
        pass
    else:
        with open(new_qufu_name, "a", encoding="utf-8-sig") as f:
            # f.write("#数据生成;\n")
            f.write("set names utf8mb4;\n")

    with open(new_qufu_name, "a", encoding="utf-8-sig") as f:
        f.write(sql_insert)
        f.write("\n")
        timestamp_temp = 1
        # print(len(fenquList))
        for insert_line in fenquList:
            timestamp_temp += 1
            f.write(insert_line)
            if timestamp_temp == 10000:
                f.write(";\n")
                f.write(sql_insert + "\n")
            elif timestamp_temp - 1 == len(fenquList):
                f.write(";\n")
            else:
                f.write(",\n")
        # write_log("分段区域 {} ".format(num))


# 读取区服信息
def read_server_name_txt(source_file):
    write_log("开始读取源文件内容...")
    with open(source_file, "r", encoding="utf-8") as f:
        hangshu = 0
        serverName_dict = {}
        for l in f:
            hangshu += 1
            strlist = l.split("=")
            if len(strlist) == 2:
                if "#" in strlist[0]:
                    strlist_2 = strlist[0].split("#")
                    for i in strlist_2:
                        serverName_dict[i] = strlist[1].strip("\n")

                else:
                    serverName_dict[strlist[0]] = strlist[1].strip("\n")
        write_log(
            "读取成功，一共 {0} 个区服数据...服务器名字行数：{1} ".format(len(serverName_dict), hangshu)
        )
        return serverName_dict  # 把读取后的list返回


def get_type(cost_num):

    return cost_type[int(cost_num)]


def get_chk_sum(pay_type, account_id, userid):
    # 异或
    yihuo = pay_type ^ account_id
    # 位移动
    wyd = userid >> 1
    get_sum = yihuo + wyd
    return get_sum


if __name__ == "__main__":
    # get_sum = get_chk_sum(102, 249236, 2492360020)
    # print(get_sum)

    get_source_file_name = read_ini()
    get_user_info = read_userid_txt(get_source_file_name[0])
    # print(get_user_info)

    get_server_info = read_server_name_txt("serverName.txt")

    get_sql_1 = get_sql(get_user_info, get_source_file_name[1], get_server_info)
    # print(get_sql_1)

