# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 16:44:14 2018

@author: D.S.Mix
"""

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解。
import math

def quadratic(a,b,c):
    if a==0:
        return (-c/b)
    elif pow(b,2)-4*a*c >= 0:
        result1=(-b+math.sqrt(pow(b,2)-4*a*c))/(2*a)
        result2=(-b-math.sqrt(pow(b,2)-4*a*c))/(2*a)
        return (result1,result2)
    else:
        return('no result')




# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')