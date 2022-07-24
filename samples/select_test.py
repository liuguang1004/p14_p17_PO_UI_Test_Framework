# encoding: utf-8
# @author: newdream_daliu
# @file: select_test.py
# @time: 2022-07-23 21:32
# @desc:
from common.browser import Browser
from common.base_page import BasePage

url='file:///E:/%E6%96%B0%E6%A2%A6%E6%83%B3%E6%95%99%E8%82%B2/1.%20%E6%96%B0%E6%A2%A6%E6%83%B3%E6%95%99%E5%AD%A6PPT/(5)python%E7%B3%BB%E5%88%97/python_selenium/selenium%E6%BC%94%E7%A4%BA%E4%BE%8B%E5%AD%90/select.html'
select_inputbox={'element_name':'审核结果下拉框',   #元素名称
                                'locator_type':'id',            #元素识别方法
                                'locatot_value':'status',      #元素识别的值
                                'timeout':5}

driver=Browser().get_driver()
base_page=BasePage(driver)
base_page.open_url(url)
base_page.wait(2)
# base_page.select_input(select_inputbox,index=2)  #初审通过
# base_page.wait(2)
# base_page.select_input(select_inputbox,value='2') #复审通过
# base_page.wait(2)
# base_page.select_input(select_inputbox,text='审核不通过') #复审通过

base_page.select_input_2(select_inputbox,index=2)
base_page.wait(2)
base_page.select_input_2(select_inputbox,value='2') #复审通过
base_page.wait(2)
base_page.select_input_2(select_inputbox,text='审核不通过') #复审通过
base_page.wait(2)
base_page.select_input_2(select_inputbox) #没有传入数据，去默认值