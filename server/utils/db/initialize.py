from utils.utils import now_timestamp_mysql
from utils.db.connector import DataConnector
from utils.utils import geocode2loc, loc2geocode

class Initializer(DataConnector):
    def __init__(self):
        super().__init__()

    # 更新所有时间戳
    def flush_lastupdate_timestamp(self):
        sql = "SELECT * FROM user_info WHERE stu_permission = 3;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for each in data:
            dt = now_timestamp_mysql()
            sql = f"UPDATE user_bachelordest SET stu_bachelor_lastupd_timestamp = '{dt}' WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            sql = f"UPDATE user_masterdest SET stu_master_lastupd_timestamp = '{dt}' WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            self.conn.commit()
        return 0

    # 更新所有经纬度信息
    def flush_pos(self):
        self._flush_bachelor_pos()
        self._flush_master_pos()

    # 更新所有本科经纬度信息
    def _flush_bachelor_pos(self):
        sql = "SELECT * FROM user_info WHERE stu_permission = 3;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for each in data:
            # update bachelor
            sql = f"SELECT * FROM user_bachelordest WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            ret = self.cursor.fetchone()
            if ret['stu_bachelorxpos'] is not None and ret['stu_bachelorypos'] is not None:
                continue
            bach_city, bach_school = ret['stu_bachelorcity'] if ret['stu_bachelorcity'] is not None else "", ret['stu_bachelorschool'] if  ret['stu_bachelorschool'] is not None else ""
            if bach_school == "": continue
            posx, posy = loc2geocode(address=bach_city + bach_school)
            if posx is None or posy is None: continue
            add_comp, add_detail = geocode2loc(posx, posy)
            print(bach_city + bach_school, add_detail)
            sql = f"UPDATE user_bachelordest SET stu_bachelorxpos = {posx}, stu_bachelorypos = {posy} WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            self.conn.commit()
        return 0

    # 更新所有未来经纬度信息
    def _flush_master_pos(self):
        sql = "SELECT * FROM user_info WHERE stu_permission = 3;"
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        for each in data:
            # update master
            sql = f"SELECT * FROM user_masterdest WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            ret = self.cursor.fetchone()
            if ret['stu_masterxpos'] is not None and ret['stu_masterypos'] is not None:
                continue
            mast_city, mast_school = ret['stu_city'] if ret['stu_city'] is not None else "", ret['stu_dest'] if  ret['stu_dest'] is not None else ""
            if mast_school == "": continue
            posx, posy = loc2geocode(address=mast_city + mast_school)
            if posx is None or posy is None: continue
            add_comp, add_detail = geocode2loc(posx, posy)
            print(mast_city + mast_school, add_detail)
            sql = f"UPDATE user_masterdest SET stu_masterxpos = {posx}, stu_masterypos = {posy} WHERE stu_uuid = '{each['stu_uuid']}';"
            self.cursor.execute(sql)
            self.conn.commit()

if __name__ == '__main__':
    initializer = Initializer()
    initializer.flush_pos()