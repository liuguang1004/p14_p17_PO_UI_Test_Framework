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

if __name__ == '__main__':
    # current_path=os.path.dirname(__file__)
    # driver_path=os.path.join(current_path,'../webdriver/chromedriver.exe')
    # driver_server=Service(driver_path)
    # driver=webdriver.Chrome(service=driver_server)
    driver=Browser().get_driver()
    login_page=LoginPage(driver)
    login_page.open_url('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    login_page.set_browser_max()
    login_page.input_username('test01')
    login_page.input_password('newdream123')
    login_page.click_login()

