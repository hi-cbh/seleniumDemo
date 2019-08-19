
# urs/bin/python
# encoding:utf-8
import unittest
import pyse

from mxonline.easy.sql import DB
from mxonline.easy.public_method import login_mothod
from mxonline.easy.baseEle import BaseEle

class Course(pyse.TestCase):
    '''
    :keyword
    '''

    def login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")


    def test_sort_addtime(self):
        '''默认排序'''
        self.login()
        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result= DB().show_data_all_course("add_time")
        i=0
        for txt in l:
            name = str(result[i]['name'])
            self.assertEqual(name, str(txt),name+" : "+txt + "不一致")
            i+=1

    def test_sort_students(self):
        '''学习人数'''
        self.login()
        self.click(BaseEle.link_courses)
        self.click("link_text=>参与人数")

        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result= DB().show_data_all_course("students")
        i=0
        for txt in l:
            name = str(result[i]['name'])
            self.assertEqual(name, str(txt),name+" : "+txt + "不一致")
            i+=1

    def test_sort_click_nums(self):
        '''热门排序'''
        self.login()
        self.click(BaseEle.link_courses)
        self.click("link_text=>最热门")
        ele = self.driver.find_elements_by_xpath("//*[@class='left layout']//*[contains(@class,'box')]/div[*]/a/h2")

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result= DB().show_data_all_course("click_nums")
        i=0
        for txt in l:
            name = str(result[i]['name'])
            self.assertEqual(name, str(txt),name+" : "+txt + "不一致")
            i+=1




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Course("test_sort_addtime"))
    suite.addTest(Course("test_sort_students"))
    suite.addTest(Course("test_sort_click_nums"))
    runner = unittest.TextTestRunner()
    runner.run(suite)




