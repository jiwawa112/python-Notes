#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from collections import Iterator
from collections import Iterable

# 自己定义一个可迭代对象
class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self,name):
        self.names.append(name)
        self.current_num = 0

    def __iter__(self):
        """如果想要一个对象成为一个 可以迭代的对象，要使用for 必须实现__iter__方法"""
        return self      #返回一个迭代器

    def __next__(self):
        if self.current_num < len(self.names):      #判断for循环的下标越界问题
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration

classmate = Classmate()
classmate.add('老王')
classmate.add('张三')
classmate.add('王二')

print("判断classmate是否是可以迭代的对象: ", isinstance(classmate,Iterable))
classmate_iterator = iter(classmate)
print("判断classmate是否是迭代器: ", isinstance(classmate_iterator,Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)

# 执行for name in classmate的过程:
# 1.首先判断classmate是否是可以迭代的  （判断标准：类中有无__iter__()方法）  若有，则classmate的__iter__()方法返回一个迭代器对象
# 2.若类中还有__next__()方法，则classmate是一个迭代器 (迭代器 = __iter__()方法 + __next__()方法)
# 3.循环过程中使用classmate的__iter__()方法,返回的迭代器对象中的__next__()方法，一个一个返回迭代器的值

#【注】：迭代器一定可以迭代，可迭代的不一定是迭代器