# urs/bin/python
# encoding:utf-8
import pymysql.cursors
import os
import configparser as cparser

base_dir = str(os.path.dirname(__file__))
file_path = base_dir + "/user_db.ini"

cf = cparser.ConfigParser()
print(file_path)
cf.read(file_path)
host = cf.get("mysqlconf", "host")
port = cf.get("mysqlconf", "port")
db   = cf.get("mysqlconf", "db_name")
user = cf.get("mysqlconf", "user")
password = cf.get("mysqlconf", "password")


class DB:

    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                              port=int(port),
                                              user=user,
                                              password=password,
                                              db=db,
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self, table_name):
        real_sql = "delete from " + table_name + ";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
            cursor.execute(real_sql)
        self.connection.commit()

    # insert sql statement
    def insert(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'"+str(table_data[key])+"'"
        key   = ','.join(table_data.keys())
        value = ','.join(table_data.values())
        real_sql = "INSERT INTO " + table_name + " (" + key + ") VALUES (" + value + ")"
        print(real_sql)

        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)

        self.connection.commit()


    # 修改
    def update(self, table_name, table_data):
        try:
            key   = "=%r,".join(table_data.keys())
            key = key + "=%r"
            # print(tuple(table_data.values()))
            real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values())
            print(real_sql)

            with self.connection.cursor() as cursor:
                cursor.execute(real_sql)

            self.connection.commit()
        except BaseException as e:
            print("本地数据库连接失败")
            print(e)
        finally:
            self.close()

    # 修改
    def update_hour(self, table_name, table_data, hour):
        try:
            key   = "=%r,".join(table_data.keys())
            key = key + "=%r"
            # print(tuple(table_data.values()))
            real_sql = "UPDATE " + table_name + " SET " + key %tuple(table_data.values()) + " WHERE hour = %d ;"  %int(hour)
            print(real_sql)

            with self.connection.cursor() as cursor:
                cursor.execute(real_sql)

            self.connection.commit()
        except BaseException as e:
            print("本地数据库连接失败")
            print(e)
        finally:
            self.close()


    # close database
    def close(self):
        try:
            self.connection.close()
        except BaseException:
            print("数据库连接失败")

    # init data
    def init_data(self, datas):
        for table, data in datas.items():
            self.clear(table)
            for d in data:
                self.insert(table, d)
        self.close()

    def show_data(self,table_name):
        sql = "SELECT * FROM %s" %table_name
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results)
        return results

    def show_data_org(self,search):
        '''
        查找组织
        :param search:
        :return:
        '''
        sql = "select * from organization_courseorg where organization_courseorg.desc LIKE '%%%%%s%%%%'" %search
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results.__len__())
        return results


    def show_data_course(self,search):
        '''
        查找课程
        :param search:
        :return:
        '''
        sql = "select * from courses_course " \
              "where courses_course.name like '%%%%%s%%%%' " \
              "or courses_course.desc like  '%%%%%s%%%%' " \
              "or courses_course.detail like '%%%%%s%%%%'" \
              "ORDER BY courses_course.learn_times DESC" \
              %(search,search,search)
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results.__len__())
        return results


    def show_data_teacher(self,search):
        '''
        查找讲师
        :param search:
        :return:
        '''
        sql = "select * from organization_teacher " \
              "where organization_teacher.name like '%%%%%s%%%%' " \
              "or organization_teacher.work_company like  '%%%%%s%%%%'" \
              %(search,search)
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results.__len__())
        return results

    def show_data_all_course(self, column):
        """
        排序方式
        add_time、click_nums、students
        :return:
        """
        '''
        查找课程
        :param search:
        :return:
        '''
        sql = "select * from courses_course " \
              "ORDER BY courses_course.%s DESC" %column
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        # print(results)
        return results

    def show_lession_num(self, id):
        '''章节数量'''
        sql = "select count(*) as lession_num from courses_course, courses_lession " \
              " where courses_course.id = courses_lession.course_id and courses_course.id = %d "\
              "group by courses_course.id" %id
        print(sql)
        results = []
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        if results.__len__().__eq__(0):
            results = 0

        return results

    def show_course_user_fav(self,user_name, fav_id, fav_type):
        '''用户收藏状态'''
        sql = "select count(*) as num from operation_userfavorite, users_userprofile "\
              "where fav_id=%d and fav_type = %d and username='%s' " \
              "and operation_userfavorite.user_id = users_userprofile.id"\
              %(fav_id, fav_type,user_name)

        # print(sql)

        results = []

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        results = dict(results[0])
        print(results)
        if results['num'] == 0:
            return "收藏"
        else:
            return "已收藏"

    def show_courseorg(self, fav_id, fav_type,org_name):
        '''用户收藏状态'''
        sql = "select count(*) as num from operation_userfavorite, users_userprofile " \
              "where fav_id=%d and fav_type = %d and username='%s' " \
              "and operation_userfavorite.user_id = users_userprofile.id" \
              %(fav_id, fav_type,org_name)

        # print(sql)

        results = []

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        results = dict(results[0])
        print(results)
        if results['num'] == 0:
            return "收藏"
        else:
            return "已收藏"


    def showdata_all_teachers(self, col, by_name,name=""):
        '''

        :param col:  行
        :param by_name:  排序名
        :return:
        '''
        if name.__eq__(""):
            sql = "select * from organization_teacher ORDER BY %s %s" %(col, by_name)
        else:
            sql = "select * from organization_teacher where name='%s' ORDER BY %s %s" %(name, col, by_name)
            # print(sql)

        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results.__len__())
        return results

    def show_all_orgs(self,col, sort):
        '''
        查找组织
        :param search:
        :return:
        '''
        sql = "select * from organization_courseorg order by %s %s" %(col, sort)
        # print(sql)
        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            results = cursor.fetchall()

        print(results.__len__())
        return results





"""

全局机构
select * from organization_courseorg
where name LIKE '%python%' or `desc` like '%python%';

全局课程
select * from courses_course
where `name` like '%python%' or `desc` like  '%python%' or `detail` like '%python%'
ORDER BY courses_course.`learn_times` DESC

教师
select * from organization_teacher
where `name` like '%大%' or work_company like '%大%'

"""


if __name__ == '__main__':

    result = DB().show_all_orgs('add_time','asc')
    result = DB().show_all_orgs('click_nums','desc')
    result = DB().show_all_orgs('students','desc')
    print(result)