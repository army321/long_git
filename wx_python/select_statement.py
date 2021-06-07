import time


class statement:
    def e_moeny(self, userid):
        duankou = 3306
        sql_txt = "select * from e_money where id_target ={0} or id_source ={0} order by time_stamp desc limit 500;".format(
            userid
        )
        return (duankou, sql_txt)

    def user_online(self, userid):
        duankou = 3306
        sql_txt = "select * from user_online_info where userid ={} order by timestamp desc limit 100;".format(
            userid
        )
        return (duankou, sql_txt)

    def game_note(self, userid):
        duankou = 3307
        sql_txt = "select * from game_note  where roleid = {} limit 1000;".format(
            userid
        )

        return (duankou, sql_txt)

    def user_status(self, userid):
        duankou = 3321
        sql_txt = "select * from status  where owner_id ={} limit 1000;".format(userid)
        return (duankou, sql_txt)

    def nick_name(self, nickname):
        duankou = 3306
        sql_txt = "select * from users where nickname like '%{}%' limit 10;".format(
            nickname
        )
        return (duankou, sql_txt)

    def openid(self, accountname):
        duankou = 3306
        sql_txt = "select * from role_list where accountname = '{}' limit 10;".format(
            accountname
        )
        return (duankou, sql_txt)

    def get_time(self, timestamp):
        try:
            sql_txt = time.gmtime(int(timestamp))
            strftime_time = time.strftime("%Y-%m-%d %H:%M:%S",sql_txt)
            VIP_time = int(timestamp)-(45*24*3600)
            VIP_sql_txt = time.gmtime(VIP_time)
            VIP_strftime_time ="减去45天后 ：{}".format(time.strftime("%Y-%m-%d %H:%M:%S",VIP_sql_txt)) 
            return (strftime_time, VIP_strftime_time)
        except:
            duankouhao_num = "输入的时间戳格式不正确！"
            return (duankouhao_num, duankouhao_num)


    def mails(self, userid):
        duankou = 3308
        sql_txt = "select * from mails where tar_user_id = {} limit 10;".format(userid)
        return (duankou, sql_txt)

    def role_list(self, userid):
        try:
            mod_userid = int(userid) % 3

            if mod_userid == 0:
                duankou = "3306"
            elif mod_userid == 1:
                duankou = "3319"
            else:
                duankou = "3320"

            log_duankou = int(userid) % 4 + 1
            return_text = ("{0} log分端口 :{1}").format(duankou, log_duankou)

            sql_txt = "select * from role_list where id = {} limit 10;".format(userid)
            return (return_text, sql_txt)

        except:
            duankouhao_num = "输入的userid不正确，应该要数字形式的！"
            return (duankouhao_num, duankouhao_num)
