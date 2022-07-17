# encoding: utf-8
# @author: newdream_daliu
# @file: element_data_utils.py
# @time: 2022-07-10 17:12
# @desc:

import  os
import xlrd
from common.config_utils import local_config

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_info_datas2.xlsx')

class ElementDataUtils():
    def __init__(self,module_name,page_name,element_path=excel_path): #module_name 模块名称 page_name：页面名称
        self.workbook=xlrd.open_workbook(element_path)
        self.sheet =self.workbook.sheet_by_name(module_name)
        self.page_name=page_name
        self.row_count=self.sheet.nrows

    #{{}，{}，{}，{}}
    def get_element_info(self):
        # { 'username_inputbox'：{'element_name':'用户名输入框', 'locator_type':'id','locatot_value':'account', 'timeout':5}}
        element_infos={}
        for i in range(1,self.row_count):
            #通过第三列判定页面名称
            if self.sheet.cell_value(i,2)==self.page_name: #判定页面
                element_info={}
                element_info['element_name']=self.sheet.cell_value(i,1)
                element_info['locator_type']=self.sheet.cell_value(i,3)
                element_info['locatot_value'] = self.sheet.cell_value(i, 4)
                timeout_value= self.sheet.cell_value(i, 5)
                # 方法1：
                # if timeout_value=='':
                #     timeout_value=local_config.time_out   #如果没有设置就取config.ini里面的默认
                # else:
                #     timeout_value=float(timeout_value)  #如果设置就把字符串转float

                # 方法1.5：
                # if timeout_value: #如果存在，就取自己
                #     timeout_value=float(timeout_value)    #如果没有设置就取config.ini里面的默认
                # else:
                #     timeout_value=local_config.time_out   #如果没有设置就取config.ini里面的默认
                # # 方法2：
                timeout_value = timeout_value if isinstance(timeout_value,float) else local_config.time_out


                element_info['timeout']=timeout_value
                element_infos[self.sheet.cell_value(i,0)]=element_info
        return  element_infos

if __name__ == '__main__':
    elements=ElementDataUtils('login','login_page').get_element_info()
    print(elements)
    elements = ElementDataUtils('login', 'add_user').get_element_info()
    print(elements)
    elements = ElementDataUtils('main','main_page').get_element_info()
    print(elements)


