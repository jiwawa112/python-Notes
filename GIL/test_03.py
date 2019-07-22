#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import multiprocessing

def deadloop():
    while True:
        pass

# 子进程死循环
p1 = multiprocessing.Process(target=deadloop)
p1.start()

# 主进程死循环
# deadLoop()
while True:
    pass

