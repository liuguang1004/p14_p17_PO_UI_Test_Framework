# encoding: utf-8
# @author: newdream_daliu
# @file: demo3.py
# @time: 2022-07-17 10:58
# @desc:
# element_info={},id=frame_id,name=frame_name

def switch_to_frame(**element_dict):
    if 'id' in element_dict.keys():
       print(element_dict['id'])
    elif 'name' in element_dict.keys():
        print(element_dict['name'])

switch_to_frame(id='123456')

switch_to_frame(name='newdream')

#假设我们描述一个人，一个人很多特性，可以多，个位未知


def my_info(**info_dict):
    for key in info_dict.keys():
        print('特征: {}，值:{}'.format(key,info_dict[key]))

my_info(name='刘广')
my_info(age=28)
my_info(存款=999999)

my_info(name='刘广',age=28,存款=999999)



