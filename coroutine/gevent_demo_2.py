#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gevent import monkey
import gevent
import random
import time

monkey.patch_all()

def coroutine_work(coroutine_name):
    for i in range(10):
        print(coroutine_name,i)
        time.sleep(random.random())

gevent.joinall([
    gevent.spawn(coroutine_work,'work1'),
    gevent.spawn(coroutine_work,'work2')
])

