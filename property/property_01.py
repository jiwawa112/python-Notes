#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self,value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

goods = Goods()
print(goods.price)
goods.price = 200
del goods.price