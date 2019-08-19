import unittest
import pyse

from mxonline.easy.baseEle import BaseEle
from mxonline.easy.public_method import login_mothod
from mxonline.easy.sql import DB


class TeacherList(pyse.TestCase):
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
        self.click(BaseEle.link_teachers)
        self.click("link_text=>全部")

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result = DB().showdata_all_teachers("id",'asc')
        i=0
        for txt in l:
            name = str(result[i]['name'])
            print(name)
            self.assertTrue(str(txt).__contains__(name),name+" : "+txt + "不一致")
            i+=1


    def test_sort_clicknums(self):
        '''默认人气'''
        self.login()
        self.click(BaseEle.link_teachers)

        self.driver.find_element_by_partial_link_text("人气").click()

        self.F5()

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)

        l = []

        num = len(ele)

        for i in range(0,num):
            print(i)
            l.append(ele[i].text)
        print("-------")
        print(l)
        self.sleep(3)
        print("-------")

        result = DB().showdata_all_teachers("click_nums",'desc')
        i=0
        for txt in l:
            name = str(result[i]['name'])
            self.assertTrue(str(txt).__contains__(name),name+" : "+txt + "不一致")
            i+=1



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TeacherList("test_sort_addtime"))
    suite.addTest(TeacherList("test_sort_clicknums"))
    runner = unittest.TextTestRunner()
    runner.run(suite)