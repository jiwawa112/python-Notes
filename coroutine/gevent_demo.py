#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import gevent
# 遇到延迟操作，自动切换任务(利用延迟的操作去执行其他事情)

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(0.5)
        gevent.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(0.5)
        gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        #time.sleep(0.5)
        gevent.sleep(0.5)

print("---1---")
g1 = gevent.spawn(f1,5)
print("---2---")
g2 = gevent.spawn(f2,5)
print("---3---")
g3 = gevent.spawn(f3,5)
print("---4---")

g1.join()
g2.join()
g3.join()