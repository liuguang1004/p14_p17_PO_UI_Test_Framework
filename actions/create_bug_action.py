from element_infos.qa.create_bug_page import CreateBugPage
from element_infos.main.main_page import MainPage


class CreateBugAction:
    def __init__(self, driver):
        self.create_bug_page = CreateBugPage(driver)
        # self.main_page = MainPage(driver)

    # 提交bug用例
    def create_bug(self, bug_title, bug_content):
        '''
        提交一个bug
        :param bug_title:  bug的标题
        :param bug_content: bug 的步骤
        :return:
        '''
        self.create_bug_page.click_qa()
        self.create_bug_page.click_bug()
        self.create_bug_page.click_create_bug()

        # 选择所属模块
        self.create_bug_page.click_bug_module_select()
        self.create_bug_page.click_bug_module_choose()

        # 选择所属项目
        self.create_bug_page.click_bug_project_select()
        self.create_bug_page.click_bug_project_choose()

        # 选择影响版本
        self.create_bug_page.double_click_bug_version_select()
        self.create_bug_page.click_bug_version_choose()
        # 选择截止日期
        self.create_bug_page.click_bug_datetime_select()
        self.create_bug_page.click_bug_datetime_choose()
        # 选择操作系统
        self.create_bug_page.click_bug_system_select()
        self.create_bug_page.click_bug_system_choose()
        # 选择浏览器
        self.create_bug_page.click_bug_browser_select()
        self.create_bug_page.click_bug_browser_choose()
        # 输入bug标题
        self.create_bug_page.input_bug_title(bug_title)
        # 进入重现步骤frame框
        self.create_bug_page.click_bug_steps_frame()
        # 输入重现步骤
        self.create_bug_page.input_bug_steps(bug_content)
        # 点击保存
        #先回到默认框架
        self.create_bug_page.switch_to_default_frame()
        self.create_bug_page.scroll(1000)

        self.create_bug_page.click_bug_save_button()
        return MainPage(self.create_bug_page.driver)
