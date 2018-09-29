# -*- coding: utf-8 -*-
# sum = 0
# for i in range(1, 101):
#     if i % 2 != 0:
#         sum += i
# print(sum)

# sum = 0
# i = 1
# while i < 100:
#     if i % 2 != 0:
#         sum += i
#     i += 1
# print(sum)

a = [i for i in range(1, 101)]
print(sum(a[::2]))
