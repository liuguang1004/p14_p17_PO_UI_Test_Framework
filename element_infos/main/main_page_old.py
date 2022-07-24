# encoding: utf-8
# @author: newdream_daliu
# @file: main_page.py
# @time: 2022-07-10 11:01
# @desc:
import time
from selenium.webdriver.common.by import By
from element_infos.login.login_page import LoginPage
from common.log_utils import logger
from common.base_page import BasePage

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(self,driver)

        login_page=LoginPage()
        login_page.input_username('test01')
        login_page.input_password('newdream123')
        time.sleep(2)
        login_page.click_login()
        #难点；页面的衔接,把前一个页面的驱动，传给后一个页面
        self.driver=login_page.driver
        time.sleep(2)
        self.companyname_showbox=self.driver.find_element(By.XPATH,'//h1[@id="companyname"]')
        self.my_zone_menu=self.driver.find_element(By.XPATH,'//li[@data-id="my"]')
        self.my_product_menu = self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        self.my_project_menu = self.driver.find_element(By.XPATH,'//li[@data-id="project"]')
        self.username_showbox = self.driver.find_element(By.CLASS_NAME,'user-name')

    def get_companyname(self):  #或者公司名称
        companyname=self.companyname_showbox.get_attribute('title')
        return companyname

    def goto_myzone(self): #打开我的地盘
        self.my_zone_menu.click()

    def goto_product(self):
        self.my_product_menu.click()

    def get_username(self): #获取用户名
        username=self.username_showbox.text
        logger.info('获取用户名成功，用户名为：{}'.format(username))
        return username

if __name__ == '__main__':
    main_page=MainPage()
    main_page.goto_product()
    main_page.goto_myzone()
    username=main_page.get_username()
    # print(username)