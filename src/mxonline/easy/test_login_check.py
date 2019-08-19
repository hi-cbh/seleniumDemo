# urs/bin/python
# encoding:utf-8
import unittest
import pyse

from mxonline.easy.public_method import login_mothod


class Login(pyse.TestCase):


    def test_userAndpwd_check1(self):
        '''账号、密码为空'''
        login_mothod(self,"","")
        print("账号、密码为空: "+self.get_text("id=>jsLoginTips"))

    def test_userAndpwd_check2(self):
        '''密码为空'''
        login_mothod(self,"admin123","")
        print("账号、密码为空: "+self.get_text("id=>jsLoginTips"))

    def test_userAndpwd_check3(self):
        '''密码不为空'''
        login_mothod(self,"","12345678")
        print("密码不为空: "+self.get_text("id=>jsLoginTips"))

    def test_userAndpwd_check4(self):
        '''账号或密码错误'''
        login_mothod(self,"admin12387","12345678786")
        print("账号或密码错误: "+self.get_text("id=>jsLoginTips"))


    def test_userAndpwd_check5(self):
        '''账号或密码输入过长'''
        login_mothod(self,"admin123jiifjijfi23jiji32ji2j3r23","12345678920348230948230480239480234")
        print("账号或密码输入过长: "+self.get_text("id=>jsLoginTips"))


    def test_login(self):
        ''' baidu search key : pyse '''
        login_mothod(self,"admin123","12345678")
        self.assertTitle("慕课网在线")
        print("登录成功！")
        self.move_to_element("class=>personal")
        self.sleep(1)
        self.click("link_text=>退出")

        # self.click("link_text=>进入个人中心")

if __name__ == '__main__':
    for i in range(1,2):
        suite = unittest.TestSuite()
        runner = pyse.TestRunner("./")
        runner.run()

