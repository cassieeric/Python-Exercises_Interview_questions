# -*- coding: utf-8 -*-
# a = [1, 2, 3, 4, 5, 6]
# b = 2
# c = 5
# d = a[b: c+1]
# print(d)

a = list(input('Please input a list: '))
b = int(input('Please input a number: '))
c = int(input('Please input a number: '))
print(a)

if b < len(a) and c < len(a):
    if b < c:
        print(a[b: c+1])
    else:
        print('error!! b must be small to c')
else:
    print('The number is out of list! Please input your number again.')

