# urs/bin/python
# encoding:utf-8

import time
from pyse import Pyse




class WebReceive(object):

    def __init__(self, username, pwd, receiver):
        self.username = username
        self.pwd = pwd
        self.receiver = receiver

    def sendEmail(self, subject="cctv"):
        start = time.time()
        driver = Pyse("chrome")
        try:

            # driver.implicitly_wait() # 添加了隐式等待，去除time.sleep显示等待
            # driver.max_window()
            driver.open("http://mail.10086.cn/")

            time.sleep(3)
            driver.element_wait(r"name=>UserName", 10)
            driver.element_wait(r"id=>loginBtn", 10)

            driver.clear("name=>UserName")
            driver.type("name=>UserName", self.username)

            driver.type("id=>txtPass", self.pwd)
            driver.click("id=>loginBtn")

            time.sleep(1)
            driver.click("name=>mailbox_1")

            # 收件箱
            driver.element_wait(r"xpath=>//*[@id='divTab']/ul/li[1]/span", 10)
            driver.element_wait(r"xpath=>//*[@id='sub']", 10)



            time.sleep(3)
            print("点击写信页: %r" %driver.get_display(r"xpath=>//a[@id='btn_compose']"))
            driver.click(r"xpath=>//a[@id='btn_compose']")

            time.sleep(3)
            print('切换frame: %r' %driver.get_display(r"xpath=>//*[@id='compose_preload' and @class='main-iframe']"))
            driver.switch_to_frame(r"xpath=>//*[@id='compose_preload' and @class='main-iframe']")

            time.sleep(2)
            print('输入收件人: %r' %driver.get_display(r"xpath=>//*[@id='toContainer']/div/div[2]/div[2]/input"))
            driver.type(r"xpath=>//*[@id='toContainer']/div/div[2]/div[2]/input", self.receiver)

            time.sleep(3)
            print('输入主题: %r' %driver.get_display(r"xpath=>//input[@id='txtSubject']"))
            # driver.click(r"xpath=>//input[@id='txtSubject']")
            driver.type(r"xpath=>//input[@id='txtSubject']", subject)


            print('点击发送')
            driver.click("id=>topSend")

            #             print('等待完成')
            #             driver.element_wait(r"xpath=>//*[@id='snedStatus']", 10)
            start = time.time()
            time.sleep(1)

        except BaseException as e:
            print('运行出错！！！')

            # driver.get_windows_img(r"D:\%s.jpg " %(start))
            print(e)
        finally:
            driver.quit()
            return start

if __name__ == '__main__':


    for i in range(1):
        t1 = time.time()
        r = WebReceive('13697485262', 'hy12345678','13580491603@139.com')
        start = r.sendEmail()
        time.sleep(1)
        print(start)
        t2 = time.time()
        valueTime = str(round((t2 - t1), 2))
        print('时间差: %r' %valueTime)