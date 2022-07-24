# encoding: utf-8
# @author: newdream_daliu
# @file: quit_case.py
# @time: 2022-07-24 10:56
# @desc:
import unittest

from common.browser import Browser
from common.base_page import BasePage
from common.config_utils import local_config

from actions.login_action import LoginAction
from actions.quit_action import QuitAction
from common.selenium_base_case import SeleniumBaseCase

class QuitCase(SeleniumBaseCase):
    # def setUp(self) -> None:
    #     self.driver=Browser().get_driver()
    #     self.base_page=BasePage(self.driver)
    #     self.base_page.set_browser_max()
    #     self.base_page.implicitly_wait()
    #     self.base_page.open_url(local_config.get_url)
    #
    # def tearDown(self) -> None:
    #     self.base_page.exit_driver()

    def test_quit(self):
        """正常退出操作测试"""
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.default_login()

        quit_action=QuitAction(main_page.driver)
        login_page=quit_action.quit() #退出后返回主业务
        #断言
        actual=login_page.get_title()
        self.assertEqual(actual.__contains__('用户登录'),True,'quit_case 用例不通过')

if __name__ == '__main__':
    unittest.main()