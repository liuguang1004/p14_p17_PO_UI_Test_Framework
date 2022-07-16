# encoding: utf-8
# @author: newdream_daliu
# @file: browser.py
# @time: 2022-07-13 20:34
# @desc: 浏览器封装
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from common.config_utils import local_config

current_path=os.path.dirname(__file__)
dri_path=os.path.join(current_path,'..',local_config.get_driver_path)
dri_name=local_config.get_driver_name

class Browser():
    def __init__(self,driver_path=dri_path,driver_name=dri_name):
        self.__driver_path=driver_path
        self.__driver_name=driver_name

    def get_driver(self):  # chrome  firefox   edge
        if self.__driver_name == 'chrome':
            return  self.__get_chrome_driver()
        elif self.__driver_name == 'firefox':
            return  self.__get_firefox_driver()
        elif self.__driver_name == 'edge':
            return self.__get_edge_driver()

    def __get_chrome_driver(self):
        chrome_options = Options()
        chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
        chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置默认编码为utf-8
        chrome_options.add_experimental_option('useAutomationExtension', False)  # 取消chrome受自动控制提示
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])  # 取消chrome受自动控制提示
        driver_path=os.path.join(self.__driver_path,'chromedriver.exe')
        driver_server=Service(driver_path)
        driver=webdriver.Chrome(service=driver_server,options=chrome_options)
        return driver


    def __get_firefox_driver(self):
        driver_path = os.path.join(self.__driver_path, 'geckodriver.exe')
        driver_server = Service(driver_path)
        driver = webdriver.Firefox(service=driver_server)
        return driver

    def __get_edge_driver(self):
        driver_path = os.path.join(self.__driver_path, 'msedgedriver.exe')
        driver_server = Service(driver_path)
        driver = webdriver.Edge(service=driver_server)
        return driver

if __name__ == '__main__':
    # driver=Browser().get_chrome_driver()
    # driver.get('https://www.baidu.com')
    # driver=Browser().get_edge_driver()
    # driver.get('https://www.baidu.com')

    # driver=Browser().get_firefox_driver()
    # driver.get('https://www.baidu.com')

    driver=Browser().get_driver()
    driver.get('https://www.baidu.com')