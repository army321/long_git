import xlwings as xw
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os


# 创建多个Excel文件测试
def create_more_xlsx_file():
    app = xw.App(visible=True, add_book=False)
    for i in range(1, 3):
        workbook = app.books.add()
        workbook.save(f"E:\gittest\long_git\文件处理\excel_fly\分表{i}.xlsx")
        workbook.close()

    app.quit()


def mat_test():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    # plt.plot(x,y)  #折线图
    plt.bar(x, y)  # 柱形图
    plt.show()


def numpy_test():
    a = [1, 2, 3, 4, 5]
    b = np.array([1, 2, 3, 4, 5])
    e = [[1, 2], [2, 3], [4, 5]]
    f = np.array([[1, 2], [2, 3], [4, 5]])  # 二维数组
    g = np.arange(5, 30, 4)  # 起点，终点，步长 生成一个数组
    h = np.random.randint(0, 10, (4, 5))  # 创建一个4行5列的二维数组， 每个数都是0-10随机

    print(a * 2)
    print(b * 2)
    print(e)
    print(f)
    print(g)
    print(h)


# 可以指定行列的名字，索引，与Excel搭配更合适。
def pandas_test():
    s = pd.Series(["one", "two", "three"])
    print(s)

    a = pd.DataFrame([[1, 2], [3, 2], [5, 2], [7, 2]])
    b = pd.DataFrame(
        [[1, 2], [3, 2], [5, 2], [7, 2]],
        columns=["date", "score"],
        index=["a", "b", "c", "d"],
    )
    print(a)
    print(b)


# 获取文件路径下所有文件名，包括文件夹和文件
def get_path_file_name():
    file_path = f"F:\!英魂物品\!更新公告\!ago\\"
    file_list = os.listdir(file_path)
    for i in file_list:
        print(i)


# 重命名Excel文件中的工作簿名称
def rename_flie_sheet_name():
    file_path = f"E:\gittest\long_git\文件处理\excel_fly\转移情况test.xlsx"
    app = xw.App(visible=False, add_book=False)
    workbook = app.books.open(file_path)
    worksheets = workbook.sheets
    for i in range(len(worksheets)):
        worksheets[i].name = worksheets[i].name.replace("转移", "修改")
        print(worksheets[i].name)

    workbook.save(file_path)
    app.quit()


# 重命名文件名
def rename_flie_name():
    file_path = f"E:\gittest\long_git\文件处理\excel_fly"
    file_list = os.listdir(file_path)
    f

# 修改测试
def rename_flie_name():
    file_path = f"E:\gittest\long_git\文件处理\excel_fly"
    file_list = os.listdir(file_path)
    f


if __name__ == "__main__":
    print("开始执行")
    # create_more_xlsx_file()
    # mat_test()
    # numpy_test()
    # pandas_test()
    # get_path_file_name()
    rename_flie()
    print("执行完成")
