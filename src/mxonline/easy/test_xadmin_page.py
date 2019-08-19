# urs/bin/python
# encoding:utf-8
import unittest
import pyse
from mxonline.easy.baseEle import BaseEle

class xadminPage(pyse.TestCase):
    '''
    xadmin测试用例
    '''
    def test_xadmin_login(self):
        '''
        xadmin登录
        :return:
        '''
        self.open(BaseEle.url_xadmin)
        self.sleep(1)
        self.type(BaseEle.xadmin_username, "admin123")
        self.sleep(1)
        self.type(BaseEle.xadmin_password, "12345678")
        self.sleep(1)
        self.click(BaseEle.xadmin_btn)
        self.sleep(1)
        self.assertTitle("主页面 | 慕课网后管理系统")




if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(xadminPage("test_xadmin_login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)