# urs/bin/python
# encoding:utf-8

import time
import unittest
from pyse import Pyse

class Login(unittest.TestCase):
    '''登录类'''


    def test_login(self):
        '''密码登录'''
        print('start')
        driver = Pyse("chrome")
        try:
            driver.open("http://172.17.0.200:8066/Directors/pages/login.html?_U155834476961480222")

            time.sleep(3)

            driver.type(r"xpath=>//*[@name='userName']","test1")

            driver.type(r"name=>password","admin")

            time.sleep(2)

            driver.click(r"id=>btnSubmit")

            # time.sleep(50)
            print("等进去")
            time.sleep(30)
            print("ddddddddddd")
            print('end')
        except BaseException as err:
            print(err)




    # def test_logout(self):
    #     '''注销账号'''
    #     # self.login()
    #
    #     text = self.get_text("css=>#header > div.login > span > a:nth-child(2)")
    #
    #     if text == "注销":
    #         self.click("css=>#header > div.login > span > a:nth-child(2)")





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login"))
    # suite.addTest(Login("test_login2"))
    # suite.addTest(Login("test_login3"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # runner = pyse.TestRunner()
    # runner.run()