# -*- coding: utf-8 -*-
# 方法一
# sum = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         sum += i
# print(sum)

# 方法二
# sum = 0
# i = 1
# while i < 100:
#     if i % 2 != 0:
#         sum += i
#     i += 1
# print(sum)

# 方法三
a = [i for i in range(1, 101)]
print(sum(a[::2]))
