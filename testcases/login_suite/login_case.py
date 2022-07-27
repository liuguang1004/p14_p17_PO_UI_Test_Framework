# encoding: utf-8
# @author: newdream_daliu
# @file: login_case.py
# @time: 2022-07-17 17:11
# @desc: 编写登录的测试用例
import unittest
from  common.browser import Browser
from  common.base_page import  BasePage
from  actions.login_action import LoginAction
from common.config_utils import local_config
from common.selenium_base_case import SeleniumBaseCase
from common.test_data_utils import TestDataUtils

class LoginCase(SeleniumBaseCase):
    # def setUp(self) -> None:
    #     self.driver=Browser().get_driver()
    #     self.base_page=BasePage(self.driver)
    #     self.base_page.set_browser_max()
    #     self.base_page.implicitly_wait()
    #     self.base_page.open_url(local_config.get_url)
    #
    # def tearDown(self) -> None:
    #     self.base_page.exit_driver()
    def setUp(self) -> None:
        super().setUp()
        print('LoginCase 测试类的初始化！')
        self.test_class_data=TestDataUtils('login_suite','LoginCase').convert_exceldata_to_testdata()

    def test_login_success(self):
        '''登录成功用例'''
        test_function_data=self.test_class_data['test_login_success']
        self._testMethodDoc=test_function_data['test_name']
        login_action=LoginAction(self.base_page.driver)
        main_page=login_action.login_success(test_function_data['test_parameter'].get('username'),
                                             test_function_data['test_parameter'].get('password'))
        #断言 留着下次讲,
        actual=main_page.get_username()
        self.assertEqual(actual,test_function_data['expected_result'],'test人员1登录失败')  #actual=test01

    def test_login_fail_case(self):
        test_function_data = self.test_class_data['test_login_fail_case']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        actual=login_action.login_fail(test_function_data['test_parameter'].get('username'),
                                             test_function_data['test_parameter'].get('password'))
        self.assertEqual(actual,'登录失败，请检查您的用户名或密码是否填写正确。')

if __name__ == '__main__':
    unittest.main()

