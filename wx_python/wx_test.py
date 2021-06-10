#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import pyperclip

import text_file as t
import select_statement as sql
import class_fenghao
import fenghao_zhenghe


# https://www.cnblogs.com/ronyjay/p/12713078.html
# https://zhuanlan.zhihu.com/p/38277709
# https://www.cnblogs.com/guyuyun/p/7077612.html
# https://www.yiibai.com/wxpython/wx_gridbagsizer.html

"""
生成常用语句
自动把语句放入剪贴板
添加一个弹出界面
"""


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title=t.Frame_title, size=(800, 600))
        self.set_menu()
        self.btn_area()
        self.select_area()

    def btn_area(self):

        self.btn_panel = wx.Panel(self, -1, pos=(580, 10), size=(200, 500))  # 功能按钮区

        # 按钮生成
        self.btn_select = wx.Button(self.btn_panel, label=t.BTN_1)
        self.btn_openid = wx.Button(self.btn_panel, label=t.BTN_2)
        self.btn_exit = wx.Button(self.btn_panel, label=t.BTN_3)
        self.btn_exit2 = wx.Button(self.btn_panel, label=t.BTN_4)
        self.btn_online = wx.Button(self.btn_panel, label=t.BTN_5)
        self.btn_game_note = wx.Button(self.btn_panel, label=t.BTN_6)
        self.btn_status = wx.Button(self.btn_panel, label=t.BTN_7)
        self.btn_mails = wx.Button(self.btn_panel, label=t.BTN_8)
        self.btn_time = wx.Button(self.btn_panel, label=t.BTN_9)

        # 界面布局
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.box_sizer.Add(self.btn_select, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_exit, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_exit2, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_online, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_game_note, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_status, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_mails, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_openid, 0, wx.ALL, 10)
        self.box_sizer.Add(self.btn_time, 0, wx.ALL, 10)
        self.btn_panel.SetSizer(self.box_sizer)

        # 功能绑定
        self.btn_select.Bind(wx.EVT_BUTTON, self.on_click_nick_name)
        self.btn_openid.Bind(wx.EVT_BUTTON, self.on_click_openid)
        self.btn_exit.Bind(wx.EVT_BUTTON, self.on_click_rolelist)
        self.btn_exit2.Bind(wx.EVT_BUTTON, self.click_emoney)
        self.btn_online.Bind(wx.EVT_BUTTON, self.click_user_online)
        self.btn_game_note.Bind(wx.EVT_BUTTON, self.click_game_note)
        self.btn_status.Bind(wx.EVT_BUTTON, self.click_user_status)
        self.btn_mails.Bind(wx.EVT_BUTTON, self.on_click_mails)
        self.btn_time.Bind(wx.EVT_BUTTON, self.on_click_time)

        self.box_sizer.Layout()
        self.btn_panel.Layout()
        # self.Layout()

    def select_area(self):
        self.RightPanel = wx.Panel(self, -1, pos=(10, 10), size=(560, 500))  # 功能操作区
        self.text_nickname_txt = wx.StaticText(self.RightPanel, label="输入昵称")
        self.text_nickname = wx.TextCtrl(self.RightPanel)

        self.text_userid_txt = wx.StaticText(self.RightPanel, label="输入ID")
        self.text_userid = wx.TextCtrl(self.RightPanel)

        self.text_duankouhao = wx.StaticText(self.RightPanel, label="端口号")
        self.text_duankouhao_num = wx.StaticText(self.RightPanel)
        duankouhao_num = ""
        self.text_duankouhao_num.SetLabel(duankouhao_num)

        self.text_info = wx.TextCtrl(self.RightPanel, style=wx.TE_MULTILINE)

        self.sizer_right = wx.GridBagSizer(5, 5)  # 新增一个网格布局
        self.sizer_right.Add(self.text_nickname_txt, pos=(0, 0), flag=wx.ALL, border=5)
        self.sizer_right.Add(
            self.text_nickname,
            pos=(0, 1),
            span=(1, 20),
            flag=wx.EXPAND | wx.ALL,
            border=5,
        )
        self.sizer_right.Add(self.text_userid_txt, pos=(1, 0), flag=wx.ALL, border=5)
        self.sizer_right.Add(
            self.text_userid,
            pos=(1, 1),
            span=(1, 20),
            flag=wx.EXPAND | wx.ALL,
            border=5,
        )

        self.sizer_right.Add(self.text_duankouhao, pos=(2, 0), flag=wx.ALL, border=5)
        self.sizer_right.Add(
            self.text_duankouhao_num, pos=(2, 1), flag=wx.ALL, border=5
        )
        self.sizer_right.Add(
            self.text_info, pos=(3, 0), span=(10, 20), flag=wx.EXPAND | wx.ALL, border=5
        )
        # self.sizer_right.AddGrowableRow(4, 2)

        self.RightPanel.SetSizer(self.sizer_right)  # RightPanel设置为 这个新创建的网格布局

        self.sizer_right.Layout()
        self.RightPanel.Layout()
        # self.Layout()

    def on_click_nick_name(self, event):
        get_userid = self.text_nickname.GetValue()
        a = sql.statement.nick_name(self, get_userid)
        self.set_text(a[0], a[1])

    def click_emoney(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.e_moeny(self, get_userid)
        self.set_text(a[0], a[1])

    def click_user_online(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.user_online(self, get_userid)
        self.set_text(a[0], a[1])

    def click_game_note(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.game_note(self, get_userid)
        self.set_text(a[0], a[1])

    def click_user_status(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.user_status(self, get_userid)
        self.set_text(a[0], a[1])

    def on_click_rolelist(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.role_list(self, get_userid)
        self.set_text(a[0], a[1])

    def on_click_mails(self, event):
        get_userid = self.text_userid.GetValue()
        a = sql.statement.mails(self, get_userid)
        self.set_text(a[0], a[1])

    def on_click_openid(self, event):
        get_userid = self.text_nickname.GetValue()
        a = sql.statement.openid(self, get_userid)
        self.set_text(a[0], a[1])

    def on_click_time(self, event):
        get_userid = self.text_nickname.GetValue()
        a = sql.statement.get_time(self, get_userid)
        self.set_text(a[0], a[1])


    # 把sql写到对应的框中，用统一的方法
    def set_text(self, i, j):
        self.text_duankouhao_num.SetLabel("{}".format(i))
        self.text_info.SetLabel("{}".format(j))
        pyperclip.copy("{}".format(j))

    def set_menu(self):
        # 设置菜单栏
        my_menubar = wx.MenuBar()
        # 菜单栏用这个，这边本身没东西，要后续添加
        self.SetMenuBar(my_menubar)

        # 这两个不是直接“用的”，叫菜单。就是用来分类其他 菜单项 的文件夹
        filemenu = wx.Menu()
        filemenu2 = wx.Menu()

        # 设置菜单选项名字
        my_menubar.Append(filemenu, t.MENUBAR_1)
        my_menubar.Append(filemenu2, t.MENUBAR_2)

        # MenuItem 可以点击的菜单项
        newitem = wx.MenuItem(
            parentMenu=filemenu, id=101, text=t.MENU_1, kind=wx.ITEM_NORMAL
        )
        newitem.SetBitmap(wx.Bitmap("away.png"))

        newitem2 = wx.MenuItem(
            parentMenu=filemenu, id=102, text=t.MENU_2, kind=wx.ITEM_NORMAL
        )
        newitem2.SetBitmap(wx.Bitmap("away.png"))

        newitem3 = wx.MenuItem(
            parentMenu=filemenu, id=103, text=t.MENU_3, kind=wx.ITEM_NORMAL
        )
        newitem3.SetBitmap(wx.Bitmap("away.png"))

        filemenu.AppendItem(newitem)
        filemenu.AppendSeparator()  # 添加分割线
        filemenu.AppendItem(newitem2)
        filemenu.AppendSeparator()  # 添加分割线
        filemenu.AppendItem(newitem3)
        
        # 对整个菜单栏绑定功能，具体功能在菜单中根据getid判断
        self.Bind(wx.EVT_MENU, self.click_menu)

    # 菜单的功能通过获取的菜单ID判断，执行不同的程序
    def click_menu(self, event):
        get_id = event.GetId()
        if get_id == 101:
            self.create_new_frame_fenghao()
        if get_id == 102:
            self.create_new_frame_fenghaozhenghe()
        if get_id == 103:
            self.create_new_frame_data_consolidation()


    def create_new_frame_fenghao(self):
        APP2 = wx.App()
        MYFRAME2 = MyFrame2()
        MYFRAME2.Show()
        APP2.MainLoop()
        # print("menu.....")

    def create_new_frame_fenghaozhenghe(self):
        APP3 = wx.App()
        MYFRAME3 = MyFrame3()
        MYFRAME3.Show()
        APP3.MainLoop()
        # print("menu.....")

    # 整合多个文件的数据到一个文件中，然后生成封号脚本
    def create_new_frame_data_consolidation(self):
        APP4 = wx.App()
        MYFRAME4 = MyFrame4()
        MYFRAME4.Show()
        APP4.MainLoop()


# 弹出的每日封号数据生成界面
class MyFrame2(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="封号数据生成", size=(400, 300))
        self.new_area()

    def new_area(self):

        self.btn_panel = wx.Panel(self, -1, pos=(580, 10), size=(200, 500))  # 功能按钮区

        self.text_path_txt = wx.StaticText(
            self.btn_panel, label="输入封号数据所在路径，然后点击生成即可相应生成数据", style=wx.ALIGN_CENTRE
        )
        self.text_path = wx.TextCtrl(self.btn_panel)
        self.btn_create_sql = wx.Button(self.btn_panel, label="封号生成")
        # self.btn_create_sql_zhenghe = wx.Button(self.btn_panel, label="封号扣分生成")

        # 界面布局
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.box_sizer.Add(self.text_path_txt, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.text_path, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.btn_create_sql, 5, wx.EXPAND, 10)
        # self.box_sizer.Add(self.btn_create_sql_zhenghe, 5, wx.EXPAND, 10)
        self.btn_panel.SetSizer(self.box_sizer)

        self.box_sizer.Layout()
        self.btn_panel.Layout()
        # self.Layout()

        # 功能绑定
        self.btn_create_sql.Bind(wx.EVT_BUTTON, self.on_click_create)
        # self.btn_create_sql_zhenghe.Bind(wx.EVT_BUTTON, self.on_click_create_zhenghe)

    def on_click_create(self, event):
        # print("开始生成")
        get_path = self.text_path.GetValue()
        a = class_fenghao.get_file_name(get_path)
        self.text_path_txt.SetLabel("{}".format(a))


#  弹出的封号扣分数据生成界面
class MyFrame3(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="封号扣分数据生成", size=(400, 300))
        self.new_area()

    def new_area(self):

        self.btn_panel = wx.Panel(self, -1, pos=(580, 10), size=(200, 500))  # 功能按钮区

        self.text_path_txt = wx.StaticText(
            self.btn_panel, label="输入封号数据所在路径，然后点击生成即可相应生成数据", style=wx.ALIGN_CENTRE
        )
        self.text_path = wx.TextCtrl(self.btn_panel)
        # self.btn_create_sql = wx.Button(self.btn_panel, label="封号生成")
        self.btn_create_sql_zhenghe = wx.Button(self.btn_panel, label="封号扣分生成")

        # 界面布局
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.box_sizer.Add(self.text_path_txt, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.text_path, 5, wx.EXPAND, 10)
        # self.box_sizer.Add(self.btn_create_sql, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.btn_create_sql_zhenghe, 5, wx.EXPAND, 10)
        self.btn_panel.SetSizer(self.box_sizer)

        self.box_sizer.Layout()
        self.btn_panel.Layout()
        # self.Layout()

        # 功能绑定
        # self.btn_create_sql.Bind(wx.EVT_BUTTON, self.on_click_create)
        self.btn_create_sql_zhenghe.Bind(wx.EVT_BUTTON, self.on_click_create_zhenghe)

    def on_click_create_zhenghe(self, event):
        # print("开始生成")
        get_path = self.text_path.GetValue()
        a = fenghao_zhenghe.get_file_name(get_path)
        self.text_path_txt.SetLabel("{}".format(a))

#  data consolidation interface 
class MyFrame4(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, title="数据整合", size=(400, 300))
        self.new_area()

    def new_area(self):

        self.btn_panel = wx.Panel(self, -1, pos=(580, 10), size=(200, 500))  # 功能按钮区

        self.text_path_txt = wx.StaticText(
            self.btn_panel, label="输入路径", style=wx.ALIGN_CENTRE
        )
        self.text_path = wx.TextCtrl(self.btn_panel)
        # self.btn_create_sql = wx.Button(self.btn_panel, label="封号生成")
        self.btn_create_sql_zhenghe = wx.Button(self.btn_panel, label="整合数据")

        # 界面布局
        self.box_sizer = wx.BoxSizer(wx.VERTICAL)
        self.box_sizer.Add(self.text_path_txt, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.text_path, 5, wx.EXPAND, 10)
        # self.box_sizer.Add(self.btn_create_sql, 5, wx.EXPAND, 10)
        self.box_sizer.Add(self.btn_create_sql_zhenghe, 5, wx.EXPAND, 10)
        self.btn_panel.SetSizer(self.box_sizer)

        self.box_sizer.Layout()
        self.btn_panel.Layout()
        # self.Layout()

        # 功能绑定
        # self.btn_create_sql.Bind(wx.EVT_BUTTON, self.on_click_create)
        self.btn_create_sql_zhenghe.Bind(wx.EVT_BUTTON, self.on_click_create_zhenghe)

    def on_click_create_zhenghe(self, event):
        # print("开始生成")
        get_path = self.text_path.GetValue()
        a = fenghao_zhenghe.get_file_name(get_path)
        self.text_path_txt.SetLabel("{}".format(a))



if __name__ == "__main__":
    APP = wx.App()
    MYFRAME = MyFrame()
    MYFRAME.Show()

    APP.MainLoop()
