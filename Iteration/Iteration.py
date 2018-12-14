# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:38:00 2018

@author: D.S.Mix
"""

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if isinstance(L,list) ==False:
        return (None,None)
    if L==[]:
        return (None, None)
    minnum = L[0]
    maxnum = L[0]
    for l in L:
        if l < minnum:
            minnum = l
            continue
        if l > maxnum:
            maxnum = l
            continue
    print(minnum,maxnum)
    return (minnum,maxnum)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')