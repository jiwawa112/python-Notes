#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = 300
def test1():
    x = 200
    def test2():
        nonlocal x
        print("---1---x=%d" % x)
        x = 100
        print("---1---x=%d" % x)
    return test2

t1 = test1()
print(t1)
t1()

# 闭包中不能修改外部作用域的局部变量
# 修改全局变量 global
# 修改闭包外函数定义的变量 nonlocal
# 用途1：当闭包执行完后，仍然能够保持住当前的运行环境。
# 用途2：闭包可以根据外部作用域的局部变量来得到不同的结果