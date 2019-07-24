#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建property属性的方式-装饰器
class Goods:
    """python3中默认继承object类"""

    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self,value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.delter')

# ####### 调用 #######
obj = Goods()
obj.price           #自动执行 @property修饰的price方法，并获取方法的返回值
obj.price = 123     #自动执行 @price.setter修饰的price方法，并将123赋值给方法的参数
del obj.price       #自动执行 @price.delter修饰的price方法

# 经典类中的属性只有一种访问方式，其对应被@property修饰的方法
# 新式类中的属性有三种访问方法，并分别对应了三个被@property、@方法名.setter、@方法名.deleter修饰的方法
