# -*- coding: utf-8 -*-
a = ['a', 'b', 'apple', 'z', 'example', 'dcpeng']

for i in range(len(a)):
    print(a[i])

print('*************')

for i, v in enumerate(a):
    print(i, v)

print('*************')

i = 0
while i < len(a):
    print(a[i])
    i += 1
