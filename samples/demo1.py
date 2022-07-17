# encoding: utf-8
# @author: newdream_daliu
# @file: demo1.py
# @time: 2022-07-17 8:44
# @desc: 封装的讲解

# name='刘广'
# age=28
# print('我叫%s，今年%d岁'%(name,age))
#
# #函数的封装
# def my_info():
#     name = '刘广'
#     age = 28
#     print('我叫%s，今年%d岁'%(name,age))
#
# #调用函数
# my_info()
# #数据分离
# def my_info(n,a):
#     name = n
#     age = a
#     print('我叫%s，今年%d岁'%(name,age))
#
# my_info('张三',18)
# my_info('李四',19)
# #有return
# def add(a,b):
#     return a+b
#
# print(add(100,200))
# print(add(200,300))


#类的封装
class People():
    def __init__(self,name,age):
        self.name=name
        self.__age=age


    def my_info(self):
        print('我叫%s，我今年%d岁'%(self.name,self.__age))

    def eat(self):
        print('我叫%s，是人就要吃饭，我要吃饭'%self.name)

    def get_age(self):
        return self.__age

    def set_age(self,age):
        self.__age=age



liuguang=People('刘广',28)
liuguang.my_info()
liuguang.eat()
# print(liuguang.age)

# zhansan=People('张三',25)
# zhansan.my_info()
# zhansan.eat()