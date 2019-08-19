from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized


class BaiduTest(TestCase):
    """Baidu serach test case"""

    """
    A simple test
    """
    def test_case(self):
        """ baidu search key : pyse """
        self.open("https://www.baidu.com/")
        self.move_to_element("link_text=>设置")
        self.click("link_text=>搜索设置")
        self.select("#nr", '20')
        self.click("class=>prefpanelgo")
        self.sleep(2)
        self.assertAlert("已经记录下您的使用偏好")
        self.accept_alert()



    """
    used parameterized test
    """
    @parameterized.expand([
        (1, 'pyse'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self,int_str,search_key):
        ''' baidu search key : pyse '''
        # print("传入参数"+int_str)
        self.open("https://www.baidu.com")
        self.clear("id=>kw")
        self.type("id=>kw", search_key)
        self.click("css=>#su")
        self.assertTitle(search_key)


if __name__ == '__main__':
    runner = TestRunner('./', '百度测试用例', '测试环境：Firefox')
    runner.debug()