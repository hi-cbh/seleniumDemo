# urs/bin/python
# encoding:utf-8

import unittest
from pyse import Pyse,TestCase

class Login(TestCase):
    '''登录类'''


    def test_login(self):
        '''密码登录'''
        print('start')
        self.login('test1','admin')


    def login(self, username, password):
        '''登录功能'''
        print('start')
        try:
            self.open("http://172.17.0.209:8066")

            self.sleep(3)

            self.type(r"xpath=>//*[@name='userName']",username)

            self.type(r"name=>password",password)

            self.sleep(2)

            self.click(r"id=>btnSubmit")

            print("等进去")
            self.sleep(10)

            self.click('xpath=>//*[@id="v-menu"]/div[3]/div/div[1]/div/div/div[2]')
            # text = self.get_text('xpath=>//*[@id="v-menu"]/div[2]/div/div[1]/div/div/div[1]/div/span[2]')
            self.sleep(10)
            # print(text)
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