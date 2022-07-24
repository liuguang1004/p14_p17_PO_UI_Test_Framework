# encoding: utf-8
# @author: newdream_daliu
# @file: quit_action.py
# @time: 2022-07-24 10:50
# @desc: 退出操作
from element_infos.main.main_page import MainPage
from element_infos.login.login_page import LoginPage

class QuitAction():
    def __init__(self,driver):
        self.main_page=MainPage(driver)

    def quit(self):
        self.main_page.click_username()
        self.main_page.click_quit_button()
        return LoginPage(self.main_page.driver)  #退出操作后，返回一个主页面