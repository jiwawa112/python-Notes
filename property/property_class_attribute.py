#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建property属性的方式-创建值为property对象的类属性
class Foo:
    def get_bar(self):
        return "laowang"

    BAR = property(get_bar)


obj = Foo()
reslut = obj.BAR  # 自动调用get_bar方法,并获取方法的返回值
print(reslut)