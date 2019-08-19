import unittest
import  time
import pytesseract
from pyse import Pyse, TestCase, TestRunner
from parameterized import parameterized
from PIL import Image,ImageEnhance

class BaiduTest(unittest.TestCase):
    """Baidu serach test case"""
    #
    # @classmethod
    # def setUpClass(cls):
    #     """ Setting browser driver, Using chrome by default."""
        # cls.driver = Pyse("chrome")
        # cls.timeout = 15  # You can customize timeout time

    # """
    # A simple test
    # """
    # def test_case(self):
    #     """ baidu search key : pyse """
    #     self.open("https://www.baidu.com/")
    #     self.move_to_element("link_text=>设置")
    #     self.click("link_text=>搜索设置")
    #     self.select("#nr", '20')
    #     self.click("class=>prefpanelgo")
    #     self.sleep(2)
    #     self.assertAlert("已经记录下您的使用偏好")
    #     self.accept_alert()

    # def test_case2(self):
    #     path="/Users/apple/PythonSelenium2/src/datas/"
    #     self.open("http://172.17.0.200/login")
    #     self.sleep(1)
    #     # self.max_window()
    #     imgElement = self.get_element("id=>codeImg")
    #     self.get
    #     self.get_screenshot(path+"login.png")
    #     self.sleep(2)
    #     imgSize = imgElement.size
    #     imgLocation = imgElement.location #获取验证码元素坐标
    #     rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    #     login = Image.open(path+"login.png")
    #     frame4=login.crop(rangle)   #截取验证码图片
    #     frame4.save(path+'authcode.png')
    #     authcodeImg = Image.open(path+'authcode.png')
    #     authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    #     print(authCodeText)


    def test_case3(self):
        path="/Users/apple/PythonSelenium2/src/datas/"
        tmp_imagee = self.getImage("org_image0003.png")

        time.sleep(2)
        tmp_imagee2 = self.getRBGA(tmp_imagee)

        fimage = Image.open(path+tmp_imagee2)
        authCodeText = pytesseract.image_to_string(fimage,lang="eng").strip()
        # time.sleep(2)
        print("-------")
        print("code: "+ authCodeText)
        print("-------")



    def getImage(self, imagefile):
        tmp_image_file = "tmp_image_file.png"
        path="/Users/apple/PythonSelenium2/src/datas/"

        authcodeImg = Image.open(path+imagefile)
        sharp_img = ImageEnhance.Contrast(authcodeImg).enhance(2.5)
        sharp_img.save(path+'tmp_image_file.png')
        return tmp_image_file



    def getRBGA(self, imagefile):
        path="/Users/apple/PythonSelenium2/src/datas/"
        tmp_image_file="tmp_image_RBGA.png"
        from PIL import Image
        import numpy as np
        import cv2
        img2 = Image.open(path+imagefile)
        img2 = img2.convert('RGBA')
        pixdata = img2.load()
        for y in range(img2.size[1]):
            for x in range(img2.size[0]):
                if (pixdata[x,y][0]==0 and pixdata[x,y][1]<255 and pixdata[x,y][2]<255):
                    pixdata[x, y] = (0, 0, 0,255)
                else:
                    pixdata[x, y] = (255, 255, 255,0)


        # img2.show()
        img2.save(path+tmp_image_file)
        return tmp_image_file


    # """
    # used parameterized test
    # """
    # @parameterized.expand([
    #     (1, 'pyse'),
    #     (2, 'selenium'),
    #     (3, 'unittest'),
    # ])
    # def test_baidu(self,name,search_key):
    #     ''' baidu search key : pyse '''
    #     self.open("https://www.baidu.com")
    #     self.clear("id=>kw")
    #     self.type("id=>kw", search_key)
    #     self.click("css=>#su")
    #     self.assertTitle(search_key)


if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(BaiduTest("test_case3"))
    # suite.addTest(BaiduTest("test_case4"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
