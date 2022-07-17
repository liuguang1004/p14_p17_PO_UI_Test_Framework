# encoding: utf-8
# @author: newdream_daliu
# @file: base_page.py
# @time: 2022-07-10 14:44
# @desc:页面基础类
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.log_utils import logger



class BasePage(object):
    def __init__(self,driver):
        # self.driver=driver
        self.driver=webdriver.Chrome()

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

    #切框架 ：思路1   通过元素识别数据字典，获取元素再切
    # def switch_to_frame_by_element(self,element_info):
    #     element=self.driver.find_element(element_info)
    #     self.driver.switch_to.frame(element)
    #
    # # 切框架 ：思路2   使用id或者name切
    # def switch_to_frame_id_or_name(self,id_or_name):
    #     self.driver.switch_to.frame(id_or_name)

    # 切框架 ：思路3   把前面二种思路整合，封装成一个统一的方法
    #  element_info={},id=frame_id,name=frame_name
    def switch_to_frame(self,**element_dict):
        if 'id' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['id'])
        elif 'name' in element_dict.keys():
            self.driver.switch_to.frame(element_dict['name'])
        elif  'element_info' in element_dict.keys():
            element=self.driver.find_element(element_dict['element_info'])
            self.driver.switch_to.frame(element)

    #执行js封装：
    #删除属性
    # time.sleep(2)
    # js = 'arguments[0].removeAttribute("name");'
    # el = driver.find_element_by_id('kw')
    # driver.execute_script(js, el)
    # time.sleep(2)

    #改变属性
    # time.sleep(2)
    # el= driver.find_element_by_id('kw')
    # driver.execute_script('arguments[0].setAttribute("name","newdream");',el)

    #滚动条
    # def scroll(driver, heigh):  # 把功能封装成函数，把数据分离出来，做成参数
    #     time.sleep(2)
    #     js = 'window.scrollBy(0,{});'.format(heigh)  # 向下滚
    #     driver.execute_script(js)
    #删除元素属性的封装
    def delete_element_attribute(self,element_info,attribute_name):
        js = 'arguments[0].removeAttribute("%s");'%attribute_name
        # js = 'arguments[0].removeAttribute("{}");'.format(attribute_name)
        el = self.find_element(element_info)
        # self.driver.execute_script(js, el)
        self.__execute_script(js.el)

    #修改元素的属性
    def update_element_delete_element_attribute(self,element_info,attribute_name,attribute_vaule):
        js='arguments[0].setAttribute("%s","%s");'%(attribute_name,attribute_vaule)
        el= self.driver.find_element(element_info)
        # self.driver.execute_script(js,el)
        self.__execute_script(js,el)
    #滚动条
    def scroll(self, heigh):  # 把功能封装成函数，把数据分离出来，做成参数
        time.sleep(2)
        js = 'window.scrollBy(0,{});'.format(heigh)  # heigh正数向下滚，负数向上滚
        # self.driver.execute_script(js)
        self.__execute_script(js)

    #继续封装selenium执行js的脚本   深入封装
    def __execute_script(self,js,element=None):
        if element:
            self.driver.execute_script(js,element)
        else:
            self.driver.execute_script(js)

