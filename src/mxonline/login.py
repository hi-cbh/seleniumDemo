
'''
软实力测试测试脚本

'''


# urs/bin/python
# encoding:utf-8

import time
import unittest
import pyse


url = "http://localhost:8080/login/"

class LoginPage(object):
    '''登录页'''

    def __init__(self,driver):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.open(self.url)

    def type_username(self, username):
        '''输入用户名'''
        self.driver.type(r"id=>account_l",username)


    def type_password(self, password):
        '''输入密码'''
        self.driver.type(r"id=>password_l",password)

    def click_sumbit(self):
        '''点击登录'''
        self.driver.click(r"id=>jsLoginBtn")


class Login(object):
    '''登录类'''

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        '''登录方法'''
        try:
            loginpage = LoginPage(self.driver)

            self.driver.open(loginpage.login_url())
            time.sleep(3)


            # loginpage.type_username(username)
            # loginpage.type_password(password)
            # loginpage.click_sumbit()

            # time.sleep(50)
            print("等进去")
            time.sleep(5)

            self.driver.assertTrue(text, "首页")
            print('end')
            return True
        except BaseException as err:
            print(err)
            return False






class TestCase(pyse.TestCase):


    def testcase01(self):
        '''密码登录'''
        Login(self).login('fzjt','123456','发展集团')
        # Innovation(self).create_innovation()





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCase("testcase01"))
    # suite.addTest(Login("test_login2"))
    # suite.addTest(Login("test_login3"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # runner = pyse.TestRunner()
    # runner.run()