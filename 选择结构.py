# -*- coding: utf-8 -*-
a = int(input('Please input a number: '))
b = int(input('Please input a number: '))
if a > b:
    a, b = b, a
print(a, b)
