# urs/bin/python
# encoding:utf-8
import unittest
import pyse
from mxonline.easy.baseEle import BaseEle



class NoLogin(pyse.TestCase):
    '''
    没有登录时的操作，如收藏、开始学习等待
    '''
    def test_no_login_click_fav(self):
        '''未登录状态，课程的点击收藏'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_course)
        ele[0].click()

        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        self.click(BaseEle.course_detail_fav)

        self.assertUrl(BaseEle.url_login)

    def test_no_login_click_study(self):
        '''未登录状态，课程的点击学习'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_course)
        ele[0].click()

        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        self.click(BaseEle.course_detail_study)

        self.assertUrl(BaseEle.url_login)

    def test_no_login_click_org_fav(self):
        '''未登录状态，组织的点击收藏'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_courses)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_course)
        ele[0].click()

        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        self.click(BaseEle.course_detail_org_fav)

        self.assertUrl(BaseEle.url_login)

    def test_no_login_teacher_fav(self):
        '''未登录状态，授课讲师的点击收藏'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_teachers)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)
        ele[0].click()

        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        self.click(BaseEle.teacher_detail_fav)

        self.assertUrl(BaseEle.url_login)

    def test_no_login_teacher_org_fav(self):
        '''未登录状态，授课组织的点击收藏'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_teachers)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_teacher)
        ele[0].click()

        self.js(BaseEle.swipe_windows)
        self.sleep(1)

        self.click(BaseEle.teacher_detail_org_fav)

        self.assertUrl(BaseEle.url_login)

    def test_no_login_org_fav(self):
        '''未登录状态，授课组织的点击收藏'''
        self.open(BaseEle.url_index)

        self.click(BaseEle.link_orgs)

        ele = self.driver.find_elements_by_xpath(BaseEle.list_orgs)
        ele[0].click()

        self.sleep(1)

        self.click(BaseEle.org_detail_fav)

        self.assertUrl(BaseEle.url_login)




if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(NoLogin("test_no_login_click_fav"))
    # suite.addTest(NoLogin("test_no_login_click_study"))
    # suite.addTest(NoLogin("test_no_login_click_org_fav"))
    # suite.addTest(NoLogin("test_no_login_teacher_fav"))
    suite.addTest(NoLogin("test_no_login_org_fav"))
    runner = unittest.TextTestRunner()
    runner.run(suite)