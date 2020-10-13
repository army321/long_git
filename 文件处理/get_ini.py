import configparser
import csv

# 读取ini配置中对应的技能名字
# 读取csv文件内容
# 导出文本内容

# 记录log
def write_log(log):
    print(log)
    with open("ini_log.txt", "a", encoding="utf-8") as logfile:

        logfile.write(str(log) + "\n")


def read_ini():
    print("read_ini")

    # try:
    write_log("read ini start...")
    config = configparser.ConfigParser()
    config.read("P2PSkillDescript.ini", encoding="utf-8")
    config.read("skill2.ini", encoding="ansi")

    def get_name_1(skill_id):
        get_name_id = config.get(skill_id, "Name")
        name = config.get("P2P", get_name_id)
        return name

    with open("SQ.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            new_row = "{},{},{},{},{},{},{},{},{},{}".format(
                row[0],
                row[1],
                row[2],
                get_name_1(row[2]),
                row[3],
                get_name_1(row[3]),
                row[4],
                get_name_1(row[4]),
                row[5],
                get_name_1(row[5]),
            )
            print(new_row)
            with open("结果1.txt", "a", encoding="utf-8") as logfile:
                logfile.write(new_row + "\n")

if __name__ == "__main__":
    read_ini()
    # read_csv()
