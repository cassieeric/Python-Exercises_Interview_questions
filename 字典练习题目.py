# -*- coding: utf-8 -*-
d = {'1': 'python', '2': 'java', '3': 'c++', '4': 'php'}
a = int(input('Please input your number(1, 2, 3, 4): '))

if a == 1:
    print(d['1'])
elif a == 2:
    print(d['2'])
elif a == 3:
    print(d['3'])
elif a == 4:
    print(d['4'])
else:
    print('您输入的键不存在！')