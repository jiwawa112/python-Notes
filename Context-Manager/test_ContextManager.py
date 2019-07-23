#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import contextmanager

#该装饰器将一个函数中yield语句之前的代码当做__enter__方法执行，yield语句之后的代码当做__exit__方法执行。同时yield返回值赋值给as后的变量。
@contextmanager
def my_open(path,mode):
    # __enter__方法
    f = open(path,mode)
    yield  f
    # __exit__方法
    f.close()

with my_open('out.txt','w') as f:
    f.write("hello,This is a simple context manager")
