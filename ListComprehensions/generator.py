# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 16:05:48 2018

@author: D.S.Mix
"""

"""杨辉三角定义如下：

          1
         / \
        1   1
       / \ / \
      1   2   1
     / \ / \ / \
    1   3   3   1
   / \ / \ / \ / \
  1   4   6   4   1
 / \ / \ / \ / \ / \
1   5   10  10  5   1
把每一行看做一个list，试写一个generator，不断输出下一行的list："""

def triangles():
    s2 = [1]
    yield s2
   # s2 = [1,1]
   # yield s2
    while True:
        s2.append(0)
        s=[s2[n]+s2[n-1] for n in range(len(s2))]
        s2.pop(-1)
        s2 = s[:]
        yield s
    
    """while len(s2) >= 2:
        n = 1
        s=[1]
        while n < len(s2):
            s.append(s2[n]+s2[n-1])
            n= n+1
        s.append(1)
        print(s)
        s2 = s
        yield s"""


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')