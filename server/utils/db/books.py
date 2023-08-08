import datetime
from utils.utils import now_timestamp_mysql
from utils.utils.pos import loc2geocode, geocode2loc
from utils.db.connector import DataConnector

class Book(DataConnector):
    def __init__(self):
        super().__init__()

    def __del__(self):
        super().__del__()

    def get_stu_infos_limit(self):
        sql = 'SELECT * FROM user_info WHERE stu_permission = 3;'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            data.append(temp)
        return data

    # 查询和当前请求邮箱(登陆主键)相同的记录
    def get_matchemail(self, stu_name):
        sql = "select * from user_info where stu_name = '{}'".format(stu_name)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询是否存在与（highclass, highbatch, tutor）匹配的highclass_info记录
    def check_hctutor(self, hc, hb, hctutor):
        sql = f"select * from highclass_info where stu_highclass = {hc} and stu_highbatch = {hb} and hc_tutor = '{hctutor}';"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询当前学生信息
    def get_stu_infos(self, stu_uuid):
        sql = "select * from user_masterdest where stu_uuid = '{}';".format(stu_uuid)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询所有学生信息
    def get_allstu_infos(self):
        sql = "SELECT ui.stu_uuid, ui.stu_name FROM user_info as ui WHERE ui.stu_permission = 3;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询所有学生查看当前学生的权限信息
    def get_allstuperm_infos(self, stu_uuid):
        sql = "SELECT tab1.stu_fmuuid as stu_uuid, tab2.stu_name, tab1.stu_permissiontype as value FROM ((SELECT * " \
              "FROM (user_masterpermission as um) WHERE stu_touuid = '{}') as tab1 INNER JOIN (SELECT * FROM " \
              "user_info WHERE user_info.stu_permission <> 0) as tab2 ON tab1.stu_fmuuid = tab2.stu_uuid);".format(stu_uuid)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询当前用户名密码是否正确
    def get_user_password(self, username, password):
        sql = "select stu_uuid, stu_name, stu_idcid from user_info where stu_name = '{}' and stu_idcid = '{}';".format(username, password)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查看当前学生个人信息
    def get_stu_selfinfo(self, stu_uuid):
        # basic information
        sql = "SELECT stu_name, stu_nickname, stu_permission FROM user_info WHERE stu_uuid = '{}';".format(stu_uuid)
        self.cursor.execute(sql)
        stu_basicinfo = self.cursor.fetchone()
        if str(stu_basicinfo['stu_permission']) == '3':
            # highschool information
            sql = "SELECT * FROM user_highinfo WHERE stu_uuid = '{}';".format(stu_uuid)
            self.cursor.execute(sql)
            self_highschoolinfo = self.cursor.fetchone()
            # bachelor destination
            sql = "SELECT * FROM user_bachelordest WHERE stu_uuid = '{}';".format(stu_uuid)
            self.cursor.execute(sql)
            self_bachelorinfo = self.cursor.fetchone()
            # master destination
            sql = "SELECT * FROM user_masterdest WHERE stu_uuid = '{}';".format(stu_uuid)
            self.cursor.execute(sql)
            self_masterinfo = self.cursor.fetchone()
            tmp = self_masterinfo['stu_desttype']
            if tmp == 0:
                self_masterinfo['stu_desttype'] = "未知"
            elif tmp == 1:
                self_masterinfo['stu_desttype'] = "升学-非内地（出国，港澳台等地区）"
            elif tmp == 2:
                self_masterinfo['stu_desttype'] = "升学-内地"
            elif tmp == 3:
                self_masterinfo['stu_desttype'] = "工作"
            elif tmp == 4:
                self_masterinfo['stu_desttype'] = "待定"
            
        else:
            self_highschoolinfo = []
            self_bachelorinfo = []
            self_masterinfo = []

        return [stu_basicinfo, self_highschoolinfo, self_bachelorinfo, self_masterinfo]

    # 查看当前该学生的uuid (stu_name -> stu_uuid)
    def get_stuname2uuid(self, stu_name):
        sql = "SELECT stu_uuid FROM user_info WHERE stu_name = '{}';".format(stu_name)
        self.cursor.execute(sql)
        stu_uuid = self.cursor.fetchone()['stu_uuid']
        return stu_uuid

    # 查看当前该学生的高中年级和班级信息 {"stu_uuid", "stu_highclass", "stu_highbatch"}
    def get_stu_highinfos(self, stu_name):
        stu_uuid = self.get_stuname2uuid(stu_name=stu_name)
        sql = f"SELECT * FROM user_highinfo WHERE stu_uuid = '{stu_uuid}';"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查看当前学生可查看的本科信息
    def get_bachelor_infos(self, stu_params):
        stu_highbatch, stu_highclass = stu_params['stu_highbatch'], stu_params['stu_highclass']
        sql = f"SELECT tb1.* FROM (SELECT user_bachelordest.* FROM user_info inner join user_bachelordest on user_info.stu_uuid = user_bachelordest.stu_uuid WHERE stu_permission = 3) as tb1 INNER JOIN user_highinfo as uh WHERE tb1.stu_uuid = uh.stu_uuid and uh.stu_highbatch = '{stu_highbatch}' and uh.stu_highclass = '{stu_highclass}'; "
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询当前学生可查看的去向详细信息
    def get_stu_admittedinfos(self, stu_name, stu_params):
        stu_uuid = self.get_stuname2uuid(stu_name=stu_name)
        stu_highbatch, stu_highclass = stu_params['stu_highbatch'], stu_params['stu_highclass']
        sql = f"SELECT tab2.* FROM ( SELECT uh.stu_uuid FROM user_highinfo as uh INNER JOIN user_masterpermission as um WHERE uh.stu_uuid = um.stu_touuid and um.stu_permissiontype = 1 and uh.stu_highbatch = '{stu_highbatch}' and uh.stu_highclass = '{stu_highclass}') as tab1 INNER JOIN user_masterdest as tab2 ON tab1.stu_uuid = tab2.stu_uuid ORDER BY stu_master_lastupd_timestamp DESC, RAND();"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询当前学生不可查看的去向详细信息
    def get_stu_forbiddeninfos(self, stu_name, stu_params):
        stu_uuid = self.get_stuname2uuid(stu_name=stu_name)
        stu_highbatch, stu_highclass = stu_params['stu_highbatch'], stu_params['stu_highclass']
        sql = f"SELECT tab2.* FROM ( SELECT uh.stu_uuid FROM user_highinfo as uh INNER JOIN user_masterpermission as um WHERE uh.stu_uuid = um.stu_touuid and um.stu_permissiontype = 0 and uh.stu_highbatch = '{stu_highbatch}' and uh.stu_highclass = '{stu_highclass}') as tab1 INNER JOIN user_masterdest as tab2 ON tab1.stu_uuid = tab2.stu_uuid ORDER BY stu_master_lastupd_timestamp DESC, RAND();"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询所有学生姓名和uuid的对应关系
    def get_uuid2stuname(self):
        sql = "SELECT stu_uuid, stu_nickname FROM user_info;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 修改用户密码
    def update_userpassword(self, emailaddress, stu_npassword):
        sql = "UPDATE user_info SET stu_idcid = '{}' WHERE stu_name = '{}';".format(stu_npassword, emailaddress)
        self.cursor.execute(sql)
        return self.conn.commit()

    # 添加新吐槽信息
    def insert_spitslot(self, stu_uuid, spit_info):
        sql = "INSERT INTO user_spitslot (stu_uuid, spit_timestamp, spit_info) VALUES ('{}', now(), '{}');".format(stu_uuid, spit_info)
        self.cursor.execute(sql)
        return self.conn.commit()
    
    # 获取最近最多20条吐槽信息
    def get_recent_spitslot(self, spit_num):
        sql = f"SELECT * FROM user_spitslot ORDER BY spit_timestamp DESC LIMIT {spit_num};"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 注册新用户信息
    def insert_stuifonewuser(self, emailaddress, stu_name, stu_password, stu_highclass, stu_highbatch):
        try:
            now_time = datetime.datetime.now().strftime("%Y-%m-%d").split('-')
            now_year = now_time[0]
            now_month = now_time[1]
            now_day = now_time[2]
            stu_uuid = "USER" + str(now_year)[-2:] + str(now_month) + str(now_day) + "000"
            sql = "SELECT stu_uuid FROM user_info WHERE stu_uuid > '{}' ORDER BY stu_uuid DESC LIMIT 1;".format(stu_uuid)
            self.cursor.execute(sql)
            stu_uuid_base = self.cursor.fetchone()
            if stu_uuid_base is not None:
                new_uuid = str(int(stu_uuid_base['stu_uuid'][-3:]) + 1)
                stu_uuid = stu_uuid[0:-3] + ("0" * (3 - len(new_uuid))) + new_uuid
            else:
                stu_uuid = stu_uuid[0:-3] + "001"
            # user_info
            sql = f"INSERT INTO user_info (stu_uuid, stu_name, stu_nickname, stu_idcid) VALUES ('{stu_uuid}', '{emailaddress}', '{stu_name}', '{stu_password}')"
            self.cursor.execute(sql)
            self.conn.commit()
            # user_highinfo
            sql = f"INSERT INTO user_highinfo (stu_uuid, stu_highclass, stu_highbatch) VALUES ('{stu_uuid}', '{stu_highclass}', '{stu_highbatch}');"
            self.cursor.execute(sql)
            self.conn.commit()
            # init user_bachelordest and user_masterdest
            self.insert_init_bachelordest(stu_uuid=stu_uuid)
            self.insert_init_masterdest(stu_uuid=stu_uuid)
            return 0
        except Exception as ne:
            return 1

    # 添加学生个人信息：本科相关（初始化）
    def insert_init_bachelordest(self, stu_uuid):
        sql = f"INSERT INTO user_bachelordest (stu_uuid, stu_bachelorschool, stu_bachelormajor) VALUES ('{stu_uuid}', '未知', '未知');"
        self.cursor.execute(sql)
        self.conn.commit()        

    # 修改学生个人信息：本科相关
    def update_bachelordest(self, stu_name, params):
        sql = f"SELECT stu_uuid FROM user_info WHERE stu_name = '{stu_name}';"
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        stu_uuid = ret['stu_uuid']

        sql = f"SELECT * FROM user_bachelordest WHERE stu_uuid = '{stu_uuid}';"
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        old_school, old_city = ret['stu_bachelorschool'], ret['stu_bachelorcity']
        
        stu_school = params['bachelor_school']
        stu_city = params['bachelor_city']
        stu_major = params['bachelor_major']
        stu_major_second = params['bachelor_major_second']
        now_ts = now_timestamp_mysql()

        # check if school change
        if old_school != stu_school or old_city != stu_city:
            try:
                new_posx, new_posy = loc2geocode(address=' '.join([stu_city, stu_school]))
                sql = f"UPDATE user_bachelordest as ub SET ub.stu_bachelor_lastupd_timestamp = '{now_ts}', ub.stu_bachelorschool = '{stu_school}', ub.stu_bachelorcity = '{stu_city}', ub.stu_bachelormajor = '{stu_major}', ub.stu_bachelormajorsecond = '{stu_major_second}', ub.stu_bachelorxpos = {new_posx}, ub.stu_bachelorypos = {new_posy} WHERE ub.stu_uuid = '{stu_uuid}';"
            except Exception as ne:
                print(f"ignore Exception {ne} in function update_bachelordest") 
        else:
            sql = f"UPDATE user_bachelordest as ub SET ub.stu_bachelor_lastupd_timestamp = '{now_ts}', ub.stu_bachelorschool = '{stu_school}', ub.stu_bachelorcity = '{stu_city}', ub.stu_bachelormajor = '{stu_major}', ub.stu_bachelormajorsecond = '{stu_major_second}' WHERE ub.stu_uuid = '{stu_uuid}';"
        self.cursor.execute(sql)
        return self.conn.commit()

    # 添加学生个人信息：本科毕业去向（初始化）
    def insert_init_masterdest(self, stu_uuid):
        sql = f"INSERT INTO user_masterdest (stu_uuid, stu_desttype) VALUES ('{stu_uuid}', 0);"
        self.cursor.execute(sql)
        self.conn.commit()          

    # 修改学生个人信息：本科毕业，即研究生或工作相关
    def update_masterdest(self, stu_name, params):
        sql = f"SELECT stu_uuid FROM user_info WHERE stu_name = '{stu_name}';"
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        stu_uuid = ret['stu_uuid']

        sql = f"SELECT * FROM user_masterdest WHERE stu_uuid = '{stu_uuid}';"
        self.cursor.execute(sql)
        ret = self.cursor.fetchone()
        old_dest, old_city = ret['stu_dest'], ret['stu_city']
            
        stu_desttype = params['master_desttype']
        stu_dest = params['master_dest']
        stu_city = params['master_city']
        stu_major = params['master_major']
        stu_direction = params['master_direction']
        stu_masterorphd = params['master_orphd']
        stu_period = params['master_period']
        now_ts = now_timestamp_mysql()

        # check if dest change
        if old_dest != stu_dest or old_city != stu_city:
            try:
                new_posx, new_posy = loc2geocode(address=' '.join([stu_city, stu_dest]))
                sql = f"UPDATE user_masterdest as um SET um.stu_master_lastupd_timestamp = '{now_ts}', um.stu_desttype = '{stu_desttype}', um.stu_dest = '{stu_dest}', um.stu_city = '{stu_city}', um.stu_mastermajor = '{stu_major}', um.stu_direction = '{stu_direction}', um.stu_masterorphd = '{stu_masterorphd}', um.stu_masterperiod = '{stu_period}', um.stu_masterxpos = {new_posx}, um.stu_masterypos = {new_posy} WHERE um.stu_uuid = '{stu_uuid}';"
            except Exception as ne:
                print(f"ignore Exception {ne} in function update_masterdest") 
        else:
            sql = f"UPDATE user_masterdest as um SET um.stu_master_lastupd_timestamp = '{now_ts}', um.stu_desttype = '{stu_desttype}', um.stu_dest = '{stu_dest}', um.stu_city = '{stu_city}', um.stu_mastermajor = '{stu_major}', um.stu_direction = '{stu_direction}', um.stu_masterorphd = '{stu_masterorphd}', um.stu_masterperiod = '{stu_period}' WHERE um.stu_uuid = '{stu_uuid}';"
        self.cursor.execute(sql)
        return self.conn.commit()

    # 修改特定学生查看权限：
    def update_masterpermission(self, stu_name, stu_uuid, tp):
        sql = f"UPDATE user_masterpermission SET stu_permissiontype = {tp}, stu_permission_lastupd_timestamp = '{now_timestamp_mysql()}' WHERE stu_touuid = '{stu_uuid}';" 
        self.cursor.execute(sql)
        return self.conn.commit()
    