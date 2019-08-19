# urs/bin/python
# encoding:utf-8
import unittest
import pyse

from mxonline.easy.baseEle import BaseEle
from mxonline.easy.public_method import login_mothod
from mxonline.easy.sql import DB


class CourseDetail(pyse.TestCase):
    '''
    课程详情检查，
    涉及到机构的，延迟
    '''

    def login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")


    def test_course_detail(self):
        '''
        最新，第一个，所有信息匹对
        :return:
        '''
        self.login()

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")
        ele[0].click()
        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        print("test start")
        print("title ",self.get_text("xpath=>//*[@class='des']/h1"))
        print("title2 ",self.get_text("xpath=>//*[@class='des']/span[@class='key']"))
        print("难度 ",self.get_text("xpath=>//*[@class='des']/div/span/i"))
        print("学习人数 ",self.get_text("xpath=>//*[@class='des']/div/span[2]"))
        print("时长 ",self.get_text("xpath=>//ul[@class='parameter']/li[1]/span[2]"))
        print("章节数 ",self.get_text("xpath=>//ul[@class='parameter']/li[2]/span[2]"))
        print("课程类别 ",self.get_text("xpath=>//ul[@class='parameter']/li[3]/span[2]"))
        print("学习用户 ",self.get_display("xpath=>//ul[@class='parameter']/li[4]/span[2]"))
        print("detail ",self.get_text("xpath=>//*[@class='left layout']/div[2]/p"))
        print("test end")


        # 读取数据库结果
        result = DB().show_data_all_course("add_time")
        print("test start")
        self.assertEqual(self.get_text("xpath=>//*[@class='des']/h1"),result[0]['name'],"不相等")
        self.assertEqual(self.get_text("xpath=>//*[@class='des']/span[@class='key']"),result[0]['desc'])
        self.assertEqual(self.get_text("xpath=>//*[@class='left layout']/div[2]/p"),result[0]['detail'])
        self.assertEqual(self.get_text("xpath=>//ul[@class='parameter']/li[1]/span[2]"),str(result[0]['learn_times']))
        self.assertEqual(self.get_text("xpath=>//ul[@class='parameter']/li[3]/span[2]"),result[0]['category'])

        # 学习人数
        students = self.get_text("xpath=>//*[@class='des']/div/span[2]").__str__()
        students = students.split("：")[1]
        self.assertEqual(students,str(result[0]['students']))

        # 章节数
        lession_num = self.get_text("xpath=>//ul[@class='parameter']/li[2]/span[2]")
        lessions = DB().show_lession_num(int(result[0]["id"]))
        self.assertEqual(int(lession_num),lessions[0]['lession_num'])

        # 等级
        degree = self.choices(result[0]["degree"])
        self.assertEqual(self.get_text("xpath=>//*[@class='des']/div/span/i"),degree)
        print("test end")


    def test_course_orginfo(self):
        '''课程机构信息'''
        '''暂时不写'''
        self.login()

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")
        ele[0].click()
        self.js("window.scrollTo(100,250);")
        self.sleep(1)


        org_name = str(self.get_text("xpath=>//*[@class='center']"))
        courses = str(self.get_text("xpath=>//*[@class='clear']/ul/li[1]/span")).split("：")[1].strip(' ')
        teachers = str(self.get_text("xpath=>//*[@class='clear']/ul/li[2]/span")).split("：")[1].strip(' ')
        address = str(self.get_text("xpath=>//*[@class='clear']/ul/li[3]")).split("：")[1].strip(' ')

        print(org_name)
        print(courses)
        print(teachers)
        print(address)

        # 读取数据库信息
        result = DB().show_data_all_course("add_time")

        print(result[0])

        course_org_id = result[0]["course_org_id"]




    def test_course_fav(self):
        '''课程收藏，页面及数量的变化'''

        self.login()

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")
        ele[0].click()
        self.js("window.scrollTo(100,250);")
        self.sleep(1)

        # 点击前状态获取
        # 1、获取文字
        fav_text = self.get_text("id=>jsLeftBtn")

        # 2、读取数据库信息
        result = DB().show_data_all_course("add_time")
        # print(result[0])

        # 3、读取状态
        fav_status = DB().show_course_user_fav(user_name="admin123",fav_id=result[0]['id'],fav_type=1)
        # 4、读取收藏数量
        before_fav_nums = int(result[0]['fav_nums'])
        print("fav_status: %s, before_fav_nums: %d" %(fav_status, before_fav_nums))
        # 收藏状态 与数据库对比

        self.assertEqual(fav_status, fav_text, "点击前，收藏状态与数据库不一致！")

        # 点击后状态
        self.click("id=>jsLeftBtn")
        self.F5()
        # 点击前状态获取
        # 1、获取文字
        fav_text = self.get_text("id=>jsLeftBtn")

        # 2、读取数据库信息
        result = DB().show_data_all_course("add_time")
        # print(result[0])

        # 3、读取状态
        fav_status = DB().show_course_user_fav(user_name="admin123",fav_id=result[0]['id'],fav_type=1)

        after_fav_nums = int(result[0]['fav_nums'])
        print("fav_status: %s, before_fav_nums: %d" %(fav_status, after_fav_nums))
        # 收藏状态 与数据库对比
        self.assertEqual(fav_status, fav_text, "点击后，收藏状态与数据库不一致！")

        # 最后一次 收藏/已收藏按钮的文字，收藏量增加或减少
        if str(fav_text).__eq__("收藏"):
            print("收藏")
            if before_fav_nums >=1 :
                self.assertEqual(before_fav_nums, after_fav_nums+1, "点击后，收藏数量错误！")
            else:
                self.assertEqual(0, after_fav_nums, "点击后，收藏数量错误！")
        else:
            print("已收藏")
            self.assertEqual(before_fav_nums, after_fav_nums-1, "点击后，收藏数量错误！")


    def test_course_org_fav(self):
        '''课程组织，页面及数量的变化'''
        '''暂时不完成'''
        self.login()

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")
        ele[0].click()
        self.js("window.scrollTo(100,250);")
        self.sleep(1)

        fav_text = self.get_text("id=>jsRightBtn")

        # 收藏状态 与数据库对比
        # 2、读取数据库信息
        result = DB().show_data_all_course("add_time")
        # print(result[0])

        # 3、读取状态
        fav_status = DB().show_course_user_fav(user_name="admin123",fav_id=result[0]['id'],fav_type=1)
        # 4、读取收藏数量
        before_fav_nums = int(result[0]['fav_nums'])
        print("fav_status: %s, before_fav_nums: %d" %(fav_status, before_fav_nums))
        # 收藏状态 与数据库对比

        self.assertEqual(fav_status, fav_text, "点击前，收藏状态与数据库不一致！")



        # 收藏数量与数据库对比




    def test_course_students(self):
        '''课程学习人数变化，页面及数量的变化'''

        self.login()

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")
        ele[0].click()
        self.js("window.scrollTo(100,250);")
        self.sleep(1)

        fav = self.get_text("xpath=>//*[@class='buy btn']")

        # 学习人数
        students = self.get_text("xpath=>//*[@class='des']/div/span[2]").__str__()
        students = students.split("：")[1]



    def choices(self,name):
        choices=(('cj','初级'),('zj','中间'),('gj','高级'))
        choices = dict(choices)
        for k,v in choices.items():
            if k.__eq__(name):
                return v


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(CourseDetail("test_course_detail"))
    # suite.addTest(CourseDetail("test_course_orginfo"))
    suite.addTest(CourseDetail("login"))
    # suite.addTest(CourseDetail("test_course_fav"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
