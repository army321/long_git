import os
import codecs

def get_path():
    new_file_name = "coslegend-other.sql"
    get_path = os.getcwd()

    print("当前路径：*****{}".format(get_path))

    with open(new_file_name, "a", encoding="utf-8-sig") as f:
        for filename in os.listdir(get_path):
            if ".sql" in filename:
                try:
                    print(filename)
                    with open(filename, encoding="utf-8") as sql_file:
                        all_line = sql_file.read()
                        f.write(all_line)
                except:
                    print(filename)
                    with open(filename, encoding="gbk") as sql_file:
                        all_line = sql_file.read()
                        f.write(all_line)


if __name__ == "__main__":
    get_path()