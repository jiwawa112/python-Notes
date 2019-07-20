#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from greenlet import greenlet
import time

# 用生成器对象进行封装
# 遇到延迟操作，自动切换任务(利用延迟的操作去执行其他事情)
# 效果看起来就是两个函数之间互相切换、交替运行
def test_1():
    while True:
        print('---A---')
        gr2.switch()
        time.sleep(0.5)

def test_2():
    while True:
        print('---B---')
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test_1)
gr2 = greenlet(test_2)

gr1.switch()