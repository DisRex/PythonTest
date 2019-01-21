# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 09:46:06 2019

@author: D.S.Mix
"""

#test = '用户输入的字符串'
#if re.match(r'正则表达式', test):
#    print('ok')
#else:
#    print('failed')

import re
def is_valid_email(addr):
    re_email = re.compile(r'^[a-zA-Z]+[.]?[a-zA-Z]+@[a-zA-Z]+\.com*$')# re.compile(r'^\w+.?\w+\@\w+.com$')
    if re_email.match(addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')