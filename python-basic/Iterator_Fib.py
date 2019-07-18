#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 任何实现了__next__方法的对象都可以称为迭代器。
# 以斐波那契数列为例来实现一个迭代器

class Fib():
    def __init__(self,n):
        self.prev = 0
        self.current = 1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            value = self.current

            # self.cur = self.current + self.prev
            # self.prev = value
            # self.prev,self.current = value,self.prev + self.current

            self.prev,self.current = self.current,self.prev + self.current
            self.n -= 1
            return value
        else:
            raise StopIteration

fib = Fib(10)
print([i for i in fib])



