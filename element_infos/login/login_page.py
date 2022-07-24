# encoding: utf-8
# @author: newdream_daliu
# @file: login_page.py
# @time: 2022-07-10 9:53
# @desc: 登录页面
from common.base_page import BasePage
from common.element_data_utils import ElementDataUtils
from common.browser import Browser

elements=ElementDataUtils('login','login_page').get_element_info()

class LoginPage(BasePage):  #一个页面一个类
    def __init__(self,driver):
        super().__init__(driver)  #初试化父类的构造函数
        self.username_inputbox=elements['username_inputbox']
        self.password_inputbox=elements['password_inputbox']
        self.login_button=elements['login_button']


    def input_username(self,name):  #操作--方法
        self.input(self.username_inputbox,name)

    def input_password(self,password):
        self.input(self.password_inputbox,password)

    def click_login(self):
        self.click(self.login_button)

    #封装一个登录失败，弹出的提示框中点确认，并返回提示框中的内容
    def get_login_fail_alert_content(self):
         return  self.switch_to_alert()

if __name__ == '__main__':
    # current_path=os.path.dirname(__file__)
    # driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver_server=Service(driver_path)
    # driver=webdriver.Chrome(service=driver_server)
    driver=Browser().get_driver()
    login_page=LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.set_browser_max()
    # name=login_page.get_element_attribute(login_page.username_inputbox,'name')
    # class_name=login_page.get_element_attribute(login_page.username_inputbox,'class')
    # print('name : {}'.format(name))
    # print('class_name : {}'.format(class_name))
    # login_page.wait(5)

    login_button_id=login_page.get_element_attribute_by_js(login_page.login_button,'id')
    print('login_button_id : {}'.format(login_button_id))
    #
    # login_page.input_username('test01')
    # login_page.input_password('newdream123')
    # login_page.click_login()
    # login_page.wait(2)
    # login_page.screenshot_as_file()

