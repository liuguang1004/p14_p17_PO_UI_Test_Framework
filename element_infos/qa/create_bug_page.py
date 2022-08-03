from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils

class CreateBugPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        elements = ElementDataUtils('qa', 'create_bug_page').get_element_info()
        self.qa_click = elements['qa_click']
        self.bug_click = elements['bug_click']
        self.create_bug_button = elements['create_bug_button']
        self.bug_project_select = elements['bug_project_select']
        self.bug_project_choose = elements['bug_project_choose']
        self.bug_module_select = elements['bug_module_select']
        self.bug_module_choose = elements['bug_module_choose']
        self.bug_version_select = elements['bug_version_select']
        self.bug_version_choose = elements['bug_version_choose']
        self.bug_datetime_select = elements['bug_datetime_select']
        self.bug_datetime_choose = elements['bug_datetime_choose']
        self.bug_system_select = elements['bug_system_select']
        self.bug_system_choose = elements['bug_system_choose']
        self.bug_browser_select = elements['bug_browser_select']
        self.bug_browser_choose = elements['bug_browser_choose']
        self.bug_title_input = elements['bug_title_input']
        self.bug_steps_frame = elements['bug_steps_frame']
        self.bug_steps_input = elements['bug_steps_input']
        self.bug_save_button = elements['bug_save_button']

    def click_qa(self):
        self.click(self.qa_click)

    def click_bug(self):
        self.click(self.bug_click)

    def click_create_bug(self):
        self.click(self.create_bug_button)

    def click_bug_project_select(self):
        self.click(self.bug_project_select)

    def click_bug_project_choose(self):
        self.click(self.bug_project_choose)

    def click_bug_module_select(self):
        self.click(self.bug_module_select)

    def click_bug_module_choose(self):
        self.click(self.bug_module_choose)

    def double_click_bug_version_select(self):
        self.wait(2)
        self.double_click(self.bug_version_select)

    def click_bug_version_choose(self):
        self.click(self.bug_version_choose)

    def click_bug_datetime_select(self):
        self.click(self.bug_datetime_select)

    def click_bug_datetime_choose(self):
        self.click(self.bug_datetime_choose)

    def click_bug_system_select(self):
        self.click(self.bug_system_select)

    def click_bug_system_choose(self):
        self.click(self.bug_system_choose)

    def click_bug_browser_select(self):
        self.click(self.bug_browser_select)

    def click_bug_browser_choose(self):
        self.click(self.bug_browser_choose)

    def input_bug_title(self, content):
        self.input(self.bug_title_input, content)

    def click_bug_steps_frame(self):
        self.switch_to_frame(element_info=self.bug_steps_frame)

    def input_bug_steps(self, content):
        self.clear(self.bug_steps_input)
        self.input(self.bug_steps_input, content)
        # self.switch_to_default_frame()

    def click_bug_save_button(self):
        self.click(self.bug_save_button)
