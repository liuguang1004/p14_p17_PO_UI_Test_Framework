# encoding: utf-8
# @author: newdream_daliu
# @file: demo2.py
# @time: 2022-07-17 9:47
# @desc: 大型项目中，动态元素识别的处理  -- 通过业务数据来识别

from common.element_data_utils import ElementDataUtils

#演示1
# elements=ElementDataUtils('login','bug_page').get_element_info()
# print(elements)

str='bug标题：%s'
title='修改商品数量时单价自动变为0'
print('bug标题%s'%title)
print(str%title)  #使用title替换str里面的%s

#最后的处理
elements=ElementDataUtils('login','bug_page').get_element_info()
print(elements)
#业务数据
title1='修改商品数量时单价自动变为0'
title2='20220626自动化测试008'

bug_link=elements['bug_link']
print(bug_link)
#方式1：
element_name=bug_link['element_name']%title1
locatot_value=bug_link['locatot_value']%title1
print(element_name)
print(locatot_value)
#方法2：
element_name=bug_link.get('element_name')%title2
locatot_value=bug_link.get('locatot_value')%title2
print(element_name)
print(locatot_value)

#先动态获取业务数据，再传入

