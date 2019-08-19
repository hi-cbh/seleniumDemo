
# urs/bin/python
# encoding:utf-8
import unittest
import pyse

from mxonline.easy.public_method import login_mothod
from mxonline.easy.sql import DB

'''全局搜索'''

class Search(pyse.TestCase):


    def login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")

    # 添加依赖
    def search(self,name, search_keywords ):
        '''搜索公开课程'''
        '''name: course、org、teacher'''
        self.click("id=>jsSelectOption")
        self.sleep(1)
        self.click("xpath=>//li[@data-value='%s']" %name)
        self.sleep(1)
        self.type("id=>search_keywords",search_keywords)
        self.sleep(1)
        self.click("id=>jsSearchBtn")


    def test_search_course(self):
        self.login()

        self.search('course', "python")
        self.sleep(2)

        ls = self.get_text("xpath=>//*[@id='content']/div[@class='group_list']/div[@class='box']/div[1]/a/h2")
        self.sleep(2)

        result = DB().show_data_course("python")

        self.assertEqual(ls,result[0]['name'],"搜索结果不匹配")



    def test_search_org(self):
        self.login()

        self.search('org', "python")
        self.sleep(2)
        num = self.get_text("xpath=>//span[@class='key']")
        first_org = self.get_text("xpath=>//*[@class='clearfix']/a/h1")
        result = DB().show_data_org("python")

        self.assertEqual(num, str(len(result)), "数量不一致")
        self.assertEqual(first_org, result[0]['name'], "搜索出的第一个机构名称不一致")



    def test_search_teacher(self):
        self.login()

        self.search('teacher', u"大")
        self.sleep(2)
        num = self.get_text("xpath=>//span[@class='key']")

        first_org = self.get_text("xpath=>//*[@class='left']//*[contains(@href,'/org/teacher/detail/')]/h1")
        result = DB().show_data_teacher("大")

        self.assertEqual(num, str(len(result)), "数量不一致")
        self.assertTrue(first_org.__contains__(result[0]['name']),  "搜索出的第一个机构名称不一致")



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Search("test_search_course"))
    suite.addTest(Search("test_search_org"))
    suite.addTest(Search("test_search_teacher"))
    runner = unittest.TextTestRunner()
    runner.run(suite)