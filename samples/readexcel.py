# encoding: utf-8
# @author: newdream_daliu
# @file: readexcel.py
# @time: 2022-07-10 16:49
# @desc: 读取元素识别信息数据
# {{},{},{},{}}
import  os
import xlrd

current_path=os.path.dirname(__file__)
excel_path=os.path.join(current_path,'../element_info_datas/element_info_datas.xlsx')

workbook=xlrd.open_workbook(excel_path)
sheet =workbook.sheet_by_name('login_page')
row_count=sheet.nrows
# { 'username_inputbox'：{'element_name':'用户名输入框', 'locator_type':'id','locatot_value':'account', 'timeout':5}}
element_infos={}
for i in range(1,row_count):
    element_info={}
    element_info['element_name']=sheet.cell_value(i,1)
    element_info['locator_type']=sheet.cell_value(i,2)
    element_info['locatot_value'] = sheet.cell_value(i, 3)
    element_info['timeout'] = sheet.cell_value(i, 4)

    element_infos[sheet.cell_value(i,0)]=element_info

print(element_infos)