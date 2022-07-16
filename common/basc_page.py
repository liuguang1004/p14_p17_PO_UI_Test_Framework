# encoding: utf-8
# @author: newdream_daliu
# @file: basc_page.py
# @time: 2022-07-10 14:44
# @desc:页面基础类
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.log_utils import logger



class BascPage(object):
    def __init__(self,driver):
        self.driver=driver
        # self.driver=webdriver.Chrome()

    def open_url(self,url):
        self.driver.get(url)
        logger.info('打开url地址：{}'.format(url))

    def set_browser_max(self):
        self.driver.maximize_window()
        logger.info('浏览器最大化')

    def set_browser_min(self):
        self.driver.minimize_window()
        logger.info('浏览器最小化')

    def refresh(self):
        self.driver.refresh()
        logger.info('浏览器刷新操作')

    def get_title(self):
        value=self.driver.title
        logger.info('获取网页标题，标题是:{}'.format(value))
        return value

    def implicitly_wait(self,senconds=5):
        self.driver.implicitly_wait(senconds)

    def get_url(self):
            value = self.driver.current_url
            logger.info('获取网页url，网址是{}'.format(value))
            return value

    def close_tab(self):
            time.sleep(2)
            self.driver.close()
            logger.info('关闭当前的tab页')

    def exit_driver(self):
            time.sleep(2)
            self.driver.quit()
            logger.info('退出浏览器')

    #element_info
       # self.username_inputbox={'element_name':'用户名输入框',   #元素名称
       #                          'locator_type':'id',            #元素识别方法
       #                          'locatot_value':'account',      #元素识别的值
       #                          'timeout':5}
    def find_element(self,element_info):
        '''
        通过元素识别的信息字典，返回一个元素
        :param element_info: 元素识别信息字典
        :return: elemen
        '''
        locator_type_name=element_info['locator_type']
        locatot_value_info=element_info['locatot_value']
        locator_timeout=element_info['timeout']
        if locator_type_name=='id':
            locator_type=By.ID
        elif locator_type_name=='xpath':
            locator_type =By.XPATH
        elif locator_type_name=='name':
            locator_type=By.NAME
        elif locator_type_name=='class':
            locator_type=By.CLASS_NAME
        elif locator_type_name=='css':
            locator_type=By.CSS_SELECTOR
        elif locator_type_name == 'linktext':
            locator_type = By.LINK_TEXT
        elif locator_type_name == 'plinktext':
            locator_type = By.PARTIAL_LINK_TEXT
        # self.driver.find_element(By.XPATH,'//li[@data-id="product"]')
        #显示等待识别元素
        element = WebDriverWait(self.driver,locator_timeout).\
            until(lambda x: x.find_element(locator_type,locatot_value_info))  #最核心的代码
        return element
    #封装元素操作方法
    #元素点击
    def click(self,element_info):
        element=self.find_element(element_info)
        element.click()
        logger.info('点击[{}]'.format(element_info['element_name']))

    #元素输入操作
    def input(self,element_info,content):  #content:内容
        element=self.find_element(element_info)
        element.send_keys(content)
        logger.info('[{}] 中输入{}'.format(element_info['element_name'],content))