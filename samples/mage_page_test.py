# encoding: utf-8
# @author: newdream_daliu
# @file: mage_page_test.py
# @time: 2022-07-24 10:26
# @desc: 测试一下mage_page里面的或者登录后用户名的方法，看能不能返回登录的用户名
from common.browser import Browser
from common.config_utils import local_config
from actions.login_action import LoginAction

driver=Browser().get_driver()
driver.get(local_config.get_url)
login_action=LoginAction(driver)
main_page=login_action.default_login()
username=main_page.get_username()
print(username)