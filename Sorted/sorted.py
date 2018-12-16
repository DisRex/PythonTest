# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 18:01:39 2018

@author: D.S.Mix
"""

#假设我们用一组tuple表示学生名字和成绩：
#
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

#再按成绩从高到低排序：
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
#L2 = sorted(L, key=by_score,reverse=True)
print(L2)