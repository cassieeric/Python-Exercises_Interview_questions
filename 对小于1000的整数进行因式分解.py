# -*- coding: utf-8 -*-
# 网上源码
# x = input('Please input an interger less than 1000: ')
# x = eval(x)
# t = x
# i = 2
# result = []
# while True:
#     if t == 1:
#         break
#     if t % i == 0:
#         result.append(i)
#         t = t / i
#     else:
#         i += 1
# print(x, '=', '*'.join(map(str, result)))


x = int(input('Please input an interger less than 1000: '))
temp = x
result = []
i = 2
while True:
    if x == 1:
        break
    if x % i == 0:
        result.append(i)
        x = x / i
    else:
        i += 1
print(temp, '=', '*'.join(map(str, result)))
