# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 14:37:39 2018

@author: D.S.Mix
"""

#������Ƭ������ʵ��һ��trim()������ȥ���ַ�����β�Ŀո�
#strTest = input()
def trim1(s):
    l=len(s)
    i=0
    if l==0:
        return ''  #����ַ�������Ϊ0��ֱ�ӷ��ؿ��ַ���
    while s[i]==' ': #�ӵ�һ���ַ���ʼ�ж�
        i=i+1
        if i > l-1:  #�������ޣ�ֱ�ӷ��ؿ��ַ���
            return ''
    while s[l-1]==' ' : #�����һ���ַ���ʼ�ж�
        l=l-1
        if l-1 <= i:   #���λ�ý�������ʼ�ַ������Զ�ֹͣ
            break
    print('���룺'+s)
    print('�����'+s[i:l])
    return s[i:l]
 
# ���Ե�һ��:
if trim1('hello  ') != 'hello':
    print('1:��һ�β���ʧ��!')
elif trim1('  hello') != 'hello':
    print('1:�ڶ��β���ʧ��!')
elif trim1('  hello  ') != 'hello':
    print('1:�����β���ʧ��!')
elif trim1('  hello  world  ') != 'hello  world':
    print('1:���Ĵβ���ʧ��!')
elif trim1('  h  ') != 'h':
    print('1:����β���ʧ��!')
elif trim1('') != '':
    print('1:�����β���ʧ��!')
elif trim1('    ') != '':
    print('1:���ߴβ���ʧ��!')
else:
    print('1:���Գɹ�!')
