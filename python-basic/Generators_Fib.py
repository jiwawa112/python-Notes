#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用生成器完成斐波那契数列
# 生成器是一种特殊的迭代器
def create_num(n):
    a,b = 0,1
    current_num = 0
    while current_num < n:
        yield a     #如果一个函数中有yield语句，那么这个函数就不在是函数，而是一个生成器模板
        a,b = b,a+b
        current_num += 1

# 如果在调用create_num的时候，发现这个函数中有yield，那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(10)

for num in obj:
    print(num)

