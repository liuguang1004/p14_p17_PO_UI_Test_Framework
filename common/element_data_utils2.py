# encoding: utf-8
# @author: newdream_daliu
# @file: element_data_utils.py
# @time: 2022-07-10 17:12
# @desc: 第二种封装读取excel中的 元素识别信息类的封装

import  os
import xlrd

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_info_datas2.xlsx')

class ElementDataUtils():
    def __init__(self,module_name,element_path=excel_path): #module_name 模块名称 page_name：页面名称
        self.workbook=xlrd.open_workbook(element_path)
        self.sheet =self.workbook.sheet_by_name(module_name)
        # self.page_name=page_name
        self.row_count=self.sheet.nrows

    #{{}，{}，{}，{}}
    def get_element_info(self,page_name):
        # { 'username_inputbox'：{'element_name':'用户名输入框', 'locator_type':'id','locatot_value':'account', 'timeout':5}}
        element_infos={}
        for i in range(1,self.row_count):
            #通过第三列判定页面名称
            if self.sheet.cell_value(i,2)==page_name: #判定页面
                element_info={}
                element_info['element_name']=self.sheet.cell_value(i,1)
                element_info['locator_type']=self.sheet.cell_value(i,3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                element_info['timeout'] = self.sheet.cell_value(i, 5)

                element_infos[self.sheet.cell_value(i,0)]=element_info
        return  element_infos

if __name__ == '__main__':
    # elements=ElementDataUtils('login','login_page').get_element_info()
    # print(elements)
    # elements = ElementDataUtils('login', 'add_user').get_element_info()
    # print(elements)
    # elements = ElementDataUtils('main','main_page').get_element_info()
    # print(elements)
    elements=ElementDataUtils('login').get_element_info('login_page')
    print(elements)


