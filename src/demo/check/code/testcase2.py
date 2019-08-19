# urs/bin/python
# encoding:utf-8

import time

import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class WebReceive(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def login(self):
        try:

            cookies={"JSESSIONID":"D8EE1183E0F21C12066DD0BBE7946A6D", "_guozi_sso":"eyJhbGciOiJIUzI1NiJ9.eyJzeXN0ZW1BdXRocyI6IlwiZ3VvemlfY3JlZGl0LGd1b3ppX2RpcmVjdG9yYXRlLGd1b3ppX2hoLGd1b3ppX2pzaCxndW96aV9sYyxndW96aV9sZWdhbCxndW96aV9zdXBlcnZpc29yXCIiLCJpc3MiOiJ0ZXN0MSIsImp0aSI6IjUwNyIsImlhdCI6MTU1NzI4NjQ2NH0.F8TDbUshZGTDGPfRvvrFNP_LuPU1yXGZfHht8d-thvg"}


            # self.browser.get("http://172.17.0.200:8055/dist/index.html#/home")
            # time.sleep(2)
            self.browser.add_cookie(cookie_dict=cookies)
            time.sleep(2)
            self.browser.get("http://172.17.0.200:8055/dist/index.html#/home")

            # elements = self.browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div/dl[2]/dt")
            # ActionChains(self.browser).move_to_element(elements).perform()
            time.sleep(4)

        except BaseException as e:
            print('运行出错！！！')
            print(e)


    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(WebReceive("login"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
