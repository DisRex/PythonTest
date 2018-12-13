# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:37:39 2018

@author: D.S.Mix
"""

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
#strTest = input()
def trim1(s):
    l=len(s)
    i=0
    if l==0:
        return ''  #如果字符串长度为0，直接返回空字符串
    while s[i]==' ': #从第一个字符开始判断
        i=i+1
        if i > l-1:  #超出界限，直接返回空字符串
            return ''
    while s[l-1]==' ' : #从最后一个字符开始判断
        l=l-1
        if l-1 <= i:   #如果位置将超过起始字符，则自动停止
            break
    print('输入：'+s)
    print('输出：'+s[i:l])
    return s[i:l]
 
# 测试第一种:
if trim1('hello  ') != 'hello':
    print('1:第一次测试失败!')
elif trim1('  hello') != 'hello':
    print('1:第二次测试失败!')
elif trim1('  hello  ') != 'hello':
    print('1:第三次测试失败!')
elif trim1('  hello  world  ') != 'hello  world':
    print('1:第四次测试失败!')
elif trim1('  h  ') != 'h':
    print('1:第五次测试失败!')
elif trim1('') != '':
    print('1:第六次测试失败!')
elif trim1('    ') != '':
    print('1:第七次测试失败!')
else:
    print('1:测试成功!')
