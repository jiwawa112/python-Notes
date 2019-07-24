#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类属性方式创建property属性具有三种访问方式，可以根据它们几个属性的访问特定，分别将三个方法定义为对同一个属性：获取、修改、删除
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        new_price = self.original_price * self.discount
        return  new_price

    def set_price(self,value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price,set_price,del_price,'价格属性描述...')

obj = Goods()
obj.PRICE
