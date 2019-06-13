# -*- coding: utf-8 -*-
# 书上的代码
# import math
# number = int(input('Please input a number: '))
# m = int(math.sqrt(number) + 1)
# for i in range(2, m):
#     if number % i == 0:
#         print('No')
#         break
# else:
#     print('yes')


# 自己想的代码
# number = int(input('Please input a number: '))
# for i in range(2, number+1):
#     if number % i == 0:
#         print('No')
#         break
#     else:
#         print('yes')
#         break


# 加根号来取
# import math
# number = int(input('Please input a number: '))
# a = int(math.sqrt(number)+1)
# for i in range(2, a):
#     if number % i == 0:
#         print('No')
#         break
#     else:
#         print('Yes')
#         break

# 二分法
# number = int(input('Please input a number: '))
# a = int(number/2 + 1)
# for i in range(2, a+1):
#     if number % i == 0:
#         print('No')
#         break
#     else:
#         print('Yes')
#         break

# number = int(input('Please input your number: '))
# for i in range(2, number):
#     if number % i == 0:
#         print('No')
#         break
# else:
#     print('Yes')

import math
number = int(input('Please input your number: '))
a = int(math.sqrt(number))
for i in range(2, a+1):
    if number % i == 0:
        print('No')
        break
else:
    print('Yes')
