# -*- coding: utf-8 -*-
namelist = ['name1','name2','name3','name4','name5','name6','name7','name8','name9']
print(namelist)
print(len(namelist))   #list长度
print(namelist[0])   #list中第一个值
print(namelist[-1])  #list中最后一个值
namelist.append('name10') #增加name10
print(namelist)
namelist.insert(3,'name2.5') #在第三个位置插入name2.5，第一个位置为0
print(namelist)
namelist.pop(3) #删除位置3的值
print(namelist)

print(namelist[0:4])   #切片取0-4的值
print(namelist[:8:2])  #前8个 每2个取一个