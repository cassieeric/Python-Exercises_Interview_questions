# -*- coding: utf-8 -*-

# 自定义输入数值
# number = int(input('Please input your number(3 numbers): '))
# geweishu = number % 10
# # print(geweishu)
# shiweishu = number // 10 % 10
# # print(shiweishu)
# baiweishu = number // 100
# # print(baiweishu)
# a = geweishu ** 3 + shiweishu ** 3 + baiweishu ** 3
# if a == number:
#     print(number)
# else:
#     print('This number is not correct!')

计算1000以内的水仙数
for i in range(100, 1000):
    geweishu = i % 10
    shiweishu = i // 10 % 10
    baiweishu = i // 100
    a = geweishu ** 3 + shiweishu ** 3 + baiweishu ** 3
    if a == i:
        print(i)
    else:
        # continue
        print('This number is not correct!')
