# urs/bin/python
# encoding:utf-8
import unittest
import pyse

from mxonline.easy.baseEle import BaseEle
from mxonline.easy.public_method import login_mothod
from mxonline.easy.sql import DB


class TeacherDetail(pyse.TestCase):
    '''
    teacher检查
    '''
    def login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")


    def test_teacher_detail(self):
        '''
        第一个，所有信息匹对
        :return:
        '''
        self.login()

        self.click(BaseEle.link_teachers)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)
        ele[0].click()
        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        # 教师排行榜
        teacher_list = "xpath=>//*[@class='fr list']//*[@class='des']/dd/a/h1"


        teacher_name = "xpath=>//*[@class='fl list']//*[@class='des']/dd/a/h1"
        work_years = "xpath=>//*[@class='fl list']//*[@class='des']/dd/ul/li[1]"
        work_company="xpath=>//*[@class='fl list']//*[@class='des']/dd/ul/li[2]"
        work_positon="xpath=>//*[@class='fl list']//*[@class='des']/dd/ul/li[3]"
        points = "xpath=>//*[@class='fl list']//*[@class='des']/dd/ul/li[4]"

        result = DB().showdata_all_teachers('id','asc',self.get_text(teacher_name)[:-4])

        print(result)

        self.assertTrue(str(self.get_text(teacher_name)).__contains__(str(result[0]['name'])),"不相等")
        self.assertTrue(str(self.get_text(work_years)).__contains__(str(result[0]['work_years'])),"不相等")
        self.assertTrue(str(self.get_text(work_company)).__contains__(str(result[0]['work_company'])),"不相等")
        self.assertTrue(str(self.get_text(work_positon)).__contains__(str(result[0]['work_positon'])),"不相等")
        self.assertTrue(str(self.get_text(points)).__contains__(str(result[0]['points'])),"不相等")

        # print(self.get_text(teacher_list))

    def test_teacher_list(self):
        '''
        页面右方的教师排名
        :return:
        '''
        self.login()

        self.click(BaseEle.link_teachers)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)
        ele[0].click()

        self.js(BaseEle.swipe_windows)

        self.sleep(1)

        # 教师排行榜
        teacher_list = "//*[@class='fr list']//*[@class='des']/dd/a/h1"
        hot_teachers = self.driver.find_elements_by_xpath(teacher_list)

        result = DB().showdata_all_teachers('click_nums','desc')


        i=0
        for hot_teacher in hot_teachers:
            print(hot_teacher.text)
            self.assertTrue(str(hot_teacher.text).__contains__(str(result[i]['name'])),"不相等")
            i=i+1




if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(TeacherDetail("test_teacher_detail"))
    suite.addTest(TeacherDetail("test_teacher_list"))
    runner = unittest.TextTestRunner()
    runner.run(suite)



