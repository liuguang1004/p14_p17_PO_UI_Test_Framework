# encoding: utf-8
# @author: newdream_daliu
# @file: login_page.py
# @time: 2022-07-10 9:53
# @desc: 登录页面
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from common.log_utils import logger
from common.basc_page import BascPage

class LoginPage(BascPage):  #一个页面一个类
    def __init__(self,driver):
        super().__init__(driver)
        # #元素识别数据分离
        self.username_inputbox={'element_name':'用户名输入框',   #元素名称
                                'locator_type':'id',            #元素识别方法
                                'locatot_value':'account',      #元素识别的值
                                'timeout':5}                    # 识别元素时，显示等待的时间

        self.password_inputbox={'element_name':'密码输入框',
                                 'locator_type':'name',
                                 'locatot_value':'password',
                                'timeout':5}

        self.login_button={'element_name':'登录按钮',
                                 'locator_type':'xpath',
                                 'locatot_value':'//button[@id="submit"]',
                                'timeout':5}

        self.keepLogin_checkbox={'element_name':'记住密码复选框',
                                 'locator_type':'xpath',
                                 'locatot_value':'//input[@name="keepLogin[]"]',
                                'timeout':5}


    def input_username(self,name):  #操作--方法
        self.input(self.username_inputbox,name)

    def input_password(self,password):
        # self.password_inputbox.send_keys(password)
        # logger.info('密码输入：{}'.format(password))
        self.input(self.password_inputbox,password)

    def click_login(self):
        # self.login_button.click()
        # logger.info('点击登录操作')
        self.click(self.login_button)

if __name__ == '__main__':
    current_path=os.path.dirname(__file__)
    driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
    driver_server = Service(driver_path)
    driver=webdriver.Chrome(service=driver_server)
    login_page=LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()
