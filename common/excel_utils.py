# encoding: utf-8
# @author: newdream_daliu
# @file: excel_utils.py
# @time: 2022-07-24 15:29
# @desc: 读取excel底层封装
import os
import xlrd
from common.config_utils import local_config

class ExcelUtils():
    def __init__(self,excel_path,sheet_name=None):
        self.excel_path=excel_path
        self.sheet_name=sheet_name
        self.sheet_data=self.__get_sheet_data()

    def __get_sheet_data(self):
        """
        通过sheet_name获取一个sheet，如果没有指明就返回第一个sheet
        :return:
        """
        workbook = xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet = workbook.sheet_by_name(self.sheet_name)
        else:
            sheet= workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        """获取总的行数"""
        row_count=self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        """获取总的列表"""
        col_count=self.sheet_data.ncols
        return col_count

    def get_sheet_data_by_list(self):
        """
        读取excel中数据
        :return:  列表 [[],[],[]]
        """
        all_excel_data=[]  #总的数据
        for rownum in range(self.get_row_count):
            row_excel_data=[]  #一行的数据
            for colnum in range(self.get_col_count):
                cell_value =self.sheet_data.cell_value(rownum,colnum)
                row_excel_data.append(cell_value)
            all_excel_data.append(row_excel_data)
        return all_excel_data
if __name__ == '__main__':
    # data1=ExcelUtils('F:/p14_p17_PO_UI_Test_Framework/'
    #                  'element_info_datas/element_info_datas2.xlsx')
    # print(data1.get_sheet_data_by_list())
    # data2= ExcelUtils('F:/p14_p17_PO_UI_Test_Framework'
    #                   '/element_info_datas/element_info_datas2.xlsx','main')
    # print(data2.get_sheet_data_by_list())
    current_path=os.path.dirname(__file__)
    test_data_path=os.path.join(current_path,'..',local_config.testdata_path)
    sheet_infos=ExcelUtils(test_data_path,'login_suite').get_sheet_data_by_list()
    print(sheet_infos)