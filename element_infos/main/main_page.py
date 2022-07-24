# encoding: utf-8
# @author: newdream_daliu
# @file: main_page.py
# @time: 2022-07-10 11:01
# @desc:
from  common.base_page import BasePage
from  common.element_data_utils import ElementDataUtils

class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        #获取元素的数据
        elements=ElementDataUtils('main','main_page').get_element_info()
        self.myzone_link=elements['myzone_link']
        self.user_menu=elements['user_menu']
        self.quit_button=elements['quit_button']

    def goto_muzone(self):  #进入我的地盘
        self.click(self.myzone_link)

    def get_username(self):
        value=self.get_text(self.user_menu)
        return value

    #点击用户名菜单
    def click_username(self):
        self.click(self.user_menu)

    #点击退出按钮
    def click_quit_button(self):
        self.click(self.quit_button)


