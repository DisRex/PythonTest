# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 21:41:39 2018

@author: D.S.Mix
"""

#利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    def counter():
        i=0
        while True:
            i = i+1
            yield i
    result = counter()
    def r():
        return next(result)
    return r

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')

#第二种
def f():
    s=[0]
    def counter(): 
         s[0]=s[0]+1
         return s[0]
    return counter

# 测试:
counterA = f()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = f()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')