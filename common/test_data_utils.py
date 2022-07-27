# encoding: utf-8
# @author: newdream_daliu
# @file: test_data_utils.py
# @time: 2022-07-27 20:54
# @desc: 读取测试用例数据
import os
from common.excel_utils import ExcelUtils
from common.config_utils import local_config

# sheet_infos = ExcelUtils(test_data_path, 'login_suite').get_sheet_data_by_list()
# print(sheet_infos)

class TestDataUtils():
    def __init__(self,test_suite_name,test_class_name):
        current_path = os.path.dirname(__file__)
        test_data_path = os.path.join(current_path, '..', local_config.testdata_path)
        self.test_class_name=test_class_name
        self.excel_data = ExcelUtils(test_data_path, test_suite_name).get_sheet_data_by_list()
        self.excel_row=len(self.excel_data)


    # { 'test_login_success':{'test_name':'验证是否能成功登录','isnot':'是','expected_result':'test01',
    #  'test_parameter':{'username':'test01','password':'newdream123'}}}
    def convert_exceldata_to_testdata(self):
        """把excel中的数据转成用例的字典数据{{{}}}"""
        test_data_infos={}
        for i in range(1,self.excel_row):  #self.excel_row)=3  1,2    数组下标： 0,1,2
            test_data_info={}
            if self.excel_data[i][2].__eq__(self.test_class_name):
                test_data_info['test_name']=self.excel_data[i][1]
                test_data_info['isnot'] = self.excel_data[i][3]
                test_data_info['expected_result'] = self.excel_data[i][4]
                test_parameter={}
                for j in range(5,len(self.excel_data[i])):
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
                        parameter_info=self.excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]]=parameter_info[1]
                test_data_info['test_parameter']=test_parameter
            test_data_infos[self.excel_data[i][0]]=test_data_info
        return  test_data_infos

if __name__ == '__main__':
    infos=TestDataUtils('login_suite','LoginCase').convert_exceldata_to_testdata()
    for key in infos.keys():
        print(key,infos[key])



