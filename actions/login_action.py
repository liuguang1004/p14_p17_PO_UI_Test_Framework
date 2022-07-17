# encoding: utf-8
# @author: newdream_daliu
# @file: login_action.py
# @time: 2022-07-17 16:44
# @desc: 功能层里面的登录，把登录页面的一组控制操作封装成一个业务
from element_infos.login.login_page import LoginPage
from element_infos.main.main_page import MainPage
from common.config_utils import local_config

class LoginAction():
    def __init__(self,driver):
        self.login_page=LoginPage(driver)

    #登录操作
    def login_action(self,username,password):
        self.login_page.input_username(username)
        self.login_page.input_password(password)
        self.login_page.click_login()

    #登录成功操作
    def login_success(self,username,password):
        self.login_action(username,password)
        # return MainPage(self.login_page.driver)

    #登录失败
    def login_fail(self,username,password):
         self.login_action(username,password)
         return self.login_page.get_login_fail_alert_content()

    #默认登录
    def default_login(self):
        self.login_success(local_config.user_name,local_config.pass_word)

    #自己扩展：
    def login_by_cookie(self):
        pass