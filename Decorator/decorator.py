# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 22:45:41 2018

@author: D.S.Mix
"""

#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

import time, functools
def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        print('begin call')
        result = fn(*args, **kw)
        end = time.time()
        print('end call')
        print('%s executed in %s ms' % (fn.__name__, (end-start)/1000)) 
        return result       
    return wrapper


# 测试
@log('')
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log('slow:')
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')