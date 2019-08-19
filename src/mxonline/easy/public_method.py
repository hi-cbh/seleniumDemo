# urs/bin/python
# encoding:utf-8

from mxonline.easy.baseEle import BaseEle

def login_mothod(self,username, password):
    self.open(BaseEle.url_login)
    self.type(BaseEle.input_username, username)
    self.sleep(1)
    self.type(BaseEle.input_password, password)
    self.sleep(1)
    self.click(BaseEle.btn_login)
    self.sleep(1)