from pymysql import connect
from pymysql.cursors import DictCursor # 为了返回字典形式
from settings import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

# 类和对象
# 对象是类的实例
# 类是抽象的
# 对象是具像的

class Book(object):
    def __init__(self):  # 创建对象同时要执行的代码
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor=self.conn.cursor(DictCursor)  # 这个可以让他返回字典的形式

    def __del__(self):  # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()

    def get_stu_infos_limit(self):
        sql = 'SELECT * FROM user_info WHERE stu_permission = 3;'
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print(temp)
            data.append(temp)
        return data

    def get_cates_newst_books_30(self, book_cate):
        sql = "select id, book_name,book_id,book_last_update_time, \
        book_newest_name,book_newest_url from book_infos \
        where book_cate='{}' order by book_last_update_time desc limit 30;".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print(temp)
            data.append(temp)
        return data

    def get_cates_most_books_30(self, book_cate):
        sql = "select id,book_id,book_name,book_author,book_newest_url from book_infos where book_cate='{}' order by book_newest_url desc limit 35;".format(book_cate)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print(temp)
            data.append(temp)
        return data

    def get_book_infos_by_book_id(self,book_id):
        sql = "select * from book_infos where book_id ='{}'".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

    def get_book_all_caps_by_book_id(self,book_id):
        sql = "select id,book_id,sort_id,detail_title from book_details where book_id='{}' order by sort_id".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

    def get_book_newest_20_caps_by_book_id(self,book_id):
        sql = "select id,book_id,sort_id,detail_title from book_details where book_id='{}' order by sort_id desc limit 20".format(book_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

    def get_book_detail_by_book_id_sort_id(self, book_id, sort_id):
        sql = "select * from book_details where book_id='{}' and sort_id='{}';".format(book_id, sort_id)
        self.cursor.execute(sql)
        data = []
        for temp in self.cursor.fetchall():
            # print("get_book_infos_by_book_id = ", temp)
            data.append(temp)
        return data

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

    # 查询当前用户名密码是否正确
    def get_user_password(self, username):
        sql = "select stu_idcid from user_info where stu_name = '{}';".format(username)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    # 查询当前学生可查看的详细信息
    def get_stu_admittedinfos(self, stu_name):
        sql = "SELECT stu_uuid FROM user_info WHERE stu_name = '{}';".format(stu_name)
        self.cursor.execute(sql)
        stu_uuid = self.cursor.fetchone()['stu_uuid']
        sql = "SELECT tab1.stu_touuid, tab2.stu_desttype, tab2.stu_city, tab2.stu_dest, tab2.stu_mastermajor, " \
              "tab2.stu_masterorphd, tab2.stu_masterperiod, tab2.stu_masterfurtherinfo FROM (SELECT ump.stu_touuid FROM " \
              "user_masterpermission as ump WHERE ump.stu_fmuuid = '{}' and ump.stu_permissiontype = 1) as tab1 INNER " \
              "JOIN user_masterdest as tab2 ON tab1.stu_touuid = tab2.stu_uuid;".format(stu_uuid)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询当前学生不可查看的详细信息
    def get_stu_forbiddeninfos(self, stu_name):
        sql = "SELECT stu_uuid FROM user_info WHERE stu_name = '{}';".format(stu_name)
        self.cursor.execute(sql)
        stu_uuid = self.cursor.fetchone()['stu_uuid']
        sql = "SELECT tab1.stu_touuid, tab2.stu_desttype, tab2.stu_city, tab2.stu_dest, tab2.stu_mastermajor, " \
              "tab2.stu_masterorphd, tab2.stu_masterperiod, tab2.stu_masterfurtherinfo FROM (SELECT ump.stu_touuid FROM " \
              "user_masterpermission as ump WHERE ump.stu_fmuuid = '{}' and ump.stu_permissiontype = 0) as tab1 INNER " \
              "JOIN user_masterdest as tab2 ON tab1.stu_touuid = tab2.stu_uuid;".format(stu_uuid)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 查询学生姓名和uuid对应的json
    def get_uuid2stuname(self):
        sql = "SELECT stu_uuid, stu_name FROM user_info;"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    # 修改学生个人信息：本科相关
    def update_bachelordest(self, stu_name, params):
        sql = "SELECT stu_uuid FROM user_info WHERE stu_name = '{}';".format(stu_name)
        self.cursor.execute(sql)
        stu_uuid = self.cursor.fetchone()['stu_uuid']
        stu_school = params['bachelor_school']
        stu_city = params['bachelor_city']
        stu_major = params['bachelor_major']
        stu_major_trans = params['bachelor_major_trans']
        stu_major_second = params['bachelor_major_second']
        sql = "UPDATE stu_info.user_bachelordest as ub SET ub.stu_bachelorschool = '{}', ub.stu_bachelorcity = '{}', ub.stu_bachelormajor = '{}', ub.stu_bachelormajorsecond = '{}' WHERE ub.stu_uuid = '{}';"\
            .format(stu_school, stu_city, stu_major, stu_major_second, stu_uuid)
        sql = self.cursor.execute(sql)
        return self.conn.commit()

    # 修改学生个人信息：本科毕业，即研究生或工作相关
    def update_masterdest(self, stu_name, params):
        sql = "SELECT stu_uuid FROM user_info WHERE stu_name = '{}';".format(stu_name)
        self.cursor.execute(sql)
        stu_uuid = self.cursor.fetchone()['stu_uuid']
        stu_desttype = params['master_desttype']
        stu_dest = params['master_dest']
        stu_city = params['master_city']
        stu_major = params['master_major']
        stu_direction = params['master_direction']
        stu_masterorphd = params['master_orphd']
        stu_period = params['master_period']
        sql = "UPDATE stu_info.user_masterdest as um SET um.stu_desttype = '{}', um.stu_dest = '{}', um.stu_city = '{" \
              "}', um.stu_mastermajor = '{}', um.stu_direction = '{}', um.stu_masterorphd = '{}', um.stu_masterperiod " \
              "= '{}' WHERE um.stu_uuid = '{}';"\
            .format(stu_desttype, stu_dest, stu_city, stu_major, stu_direction, stu_masterorphd, stu_period, stu_uuid)
        sql = self.cursor.execute(sql)
        return self.conn.commit()
