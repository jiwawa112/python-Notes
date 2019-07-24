#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 修改、查看私有属性、名字重整

class Test(object):
    def __init__(self,name):
        self.__name = name

a = Test('laowang')
# print(a._name)
print(a.__dict__)   #{'_Test__name': 'laowang'}

print(a._Test__name)