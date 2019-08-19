'''

授课机构
1、列表
2、组合筛选
3、我要学习
4、机构排名
'''

import unittest
import pyse

from mxonline.easy.baseEle import BaseEle
from mxonline.easy.public_method import login_mothod
from mxonline.easy.sql import DB


class OrgList(pyse.TestCase):
    '''
    课程详情检查，
    涉及到机构的，延迟
    '''
    def login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")


    def test_sort_addtime(self):
        '''默认排序'''

        self.login()
        self.click(BaseEle.link_orgs)
        self.click("link_text=>全部")

        ele = self.driver.find_elements_by_xpath(BaseEle.list_orgs)

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result = DB().show_all_orgs('add_time','asc')
        i=0
        for txt in l:
            name = str(result[i]['name'])
            print(name)
            self.assertTrue(str(txt).__contains__(name),name+" : "+txt + "不一致")
            i+=1

    def test_sort_students(self):
        '''默认排序'''

        self.login()
        self.click(BaseEle.link_orgs)
        self.driver.find_element_by_partial_link_text("学习人数").click()
        self.sleep(1)
        self.F5()
        self.sleep(2)
        ele = self.driver.find_elements_by_xpath(BaseEle.list_orgs)

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result = DB().show_all_orgs('students','desc')
        i=0
        for txt in l:
            name = str(result[i]['name'])
            print(name)
            self.assertTrue(str(txt).__contains__(name),name+" : "+txt + "不一致")
            i+=1

    def test_sort_click_nums(self):
        '''默认排序'''

        self.login()
        self.click(BaseEle.link_orgs)
        self.driver.find_element_by_partial_link_text("课程数").click()

        ele = self.driver.find_elements_by_xpath(BaseEle.list_orgs)

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result = DB().show_all_orgs('course_num','desc')
        i=0
        for txt in l:
            name = str(result[i]['name'])
            print(name)
            self.assertTrue(str(txt).__contains__(name),name+" : "+txt + "不一致")
            i+=1





if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(OrgList("test_sort_addtime"))
    suite.addTest(OrgList("test_sort_students"))
    suite.addTest(OrgList("test_sort_click_nums"))
    runner = unittest.TextTestRunner()
    runner.run(suite)