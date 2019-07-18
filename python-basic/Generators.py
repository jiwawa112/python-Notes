#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成器函数：也是用def定义的，利用关键字yield一次性返回一个结果，阻塞，重新开始
生成器表达式：返回一个对象，这个对象只有在需要的时候才产生结果
——生成器函数
为什么叫生成器函数？因为它随着时间的推移生成了一个数值队列。一般的函数在执行完毕之后会返回一个值然后退出，但是生成器函数会自动挂起，然后重新拾起急需执行，他会利用yield关键字关起函数，给调用者返回一个值，同时保留了当前的足够多的状态，可以使函数继续执行，生成器和迭代协议是密切相关的，迭代器都有一个__next__()__成员方法，这个方法要么返回迭代的下一项，要买引起异常结束迭代。
"""
from collections import Iterator

# 函数有了yield之后，函数就变成了生成器
# return在生成器中代表生成器的中止，直接报错
# next的作用是唤醒并继续执行
# send的作用是唤醒并继续执行，发送一个信息到生成器内部

def create_counter(n):
    '''生成器'''
    print("create_counter")
    while True:
        yield n
        print("increment n")
        n += 1

gen1 = create_counter(2)
print(gen1)
print(next(gen1))
print(next(gen1))

# 生成器表达式
# 生成器表达式来源于迭代和列表解析的组合，生成器和列表解析类似，但是它使用尖括号而不是方括号# 列表解析生成列表
lis = [ x ** 3 for x in range(5)]

# 生成器表达式
gen2 = (x ** 3 for x in range(5))

# 两者之间转换
list(x ** 3 for x in range(5))

# 一个实现了iter方法的对象时可迭代的，一个实现next方法的对象是迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 可以使用isinstance()判断一个对象是否是Iterator对象：
print(isinstance((x for x in range(10)), Iterator))
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))

#生成器都是Iterator对象，但list、dict、str虽然是Iterable（可迭代对象），却不是Iterator（迭代器）
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))