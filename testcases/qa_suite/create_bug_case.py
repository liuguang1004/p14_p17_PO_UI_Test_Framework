import unittest
from common.selenium_base_case import SeleniumBaseCase
from actions.login_action import LoginAction
from actions.create_bug_action import CreateBugAction
from common.test_data_utils import TestDataUtils

class CreateBugCase(SeleniumBaseCase):
    test_calss_data = TestDataUtils('qa_suite', 'CreateBugCase').convert_exceldata_to_testdata()

    def test_create_bug(self):
        test_function_data = self.test_calss_data['test_create_bug']
        self._testMethodDoc = test_function_data['test_name']
        login_action = LoginAction(self.base_page.driver)
        main_page=login_action.default_login()

        createBugAction=CreateBugAction(main_page.driver)
        main_page = createBugAction.create_bug(test_function_data['test_parameter'].get('bug_title'), test_function_data['test_parameter'].get('bug_content'))
        main_page.wait(3)   # 等待回到主页面
        actual_result = main_page.get_title()
        self.assertEqual(actual_result.__contains__(test_function_data['expected_result']), True, '提示：提交bug用例不通过')


if __name__ == '__main__':
    unittest.main()
