#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# closing类。该类会自动调用传入对象的close方法

import contextlib

# closing类。该类会自动调用传入对象的close方法

class MyOpen2(object):
    def __init__(self,file_name):
        """初始化方法"""
        self.file_handler = open(file_name,'r')

    def close(self):
        """关闭文件，会被自动调用"""
        print("call close in MyOpen2")
        if self.file_handler:
            self.file_handler.close()
        return

with contextlib.closing(MyOpen2("python_base.py")) as file_in:
    pass


# 这里会自动调用MyOpen2的close方法。我们查看contextlib.closing方法，内部实现为：
# class closing(object):
#   """Context to automatically close something at the end of a block."""
#     def __init__(self, thing):
#         self.thing = thing
#     def __enter__(self):
#         return self.thing
#     def __exit__(self, *exc_info):
#         self.thing.close()
# closing类的__exit__方法自动调用传入的thing的close方法。
