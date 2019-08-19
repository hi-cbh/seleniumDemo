#-*- coding:utf-8 -*-
import time
# from selenium import webdriver
from pyse import Pyse, TestCase, TestRunner
from PIL import Image,ImageEnhance
import pytesseract

def get_auth_code(driver,codeEelement):
    '''获取验证码'''
    driver.save_screenshot('login/login.png')  #截取登录页面
    imgSize = codeEelement.size   #获取验证码图片的大小
    imgLocation = imgElement.location #获取验证码元素坐标
    rangle = (int(imgLocation['x']),int(imgLocation['y']),int(imgLocation['x'] + imgSize['width']),int(imgLocation['y']+imgSize['height']))  #计算验证码整体坐标
    login = Image.open("login/login.png")
    frame4=login.crop(rangle)   #截取验证码图片
    frame4.save('login/authcode.png')
    authcodeImg = Image.open('login/authcode.png')
    authCodeText = pytesseract.image_to_string(authcodeImg).strip()
    return authCodeText






if __name__ == '__main__':

    driver = Pyse("chrome")
    try:
        driver.get('http://172.17.0.200/login')
        # driver.maximize_window()
        time.sleep(2)
        imgElement = driver.find_element_by_id('codeImg')
        authCodeText = get_auth_code(driver,imgElement)
        time.sleep(2)
        print("code: "+authCodeText)
    except BaseException as e:
        print(e)

    finally:

        driver.quit()