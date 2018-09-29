# # -*- coding: utf-8 -*-
# import random
# a = [random.randint(1, 100) for i in range(20)]
# print(a)
# b = sorted(a[::2])
# b.sort(reverse=True)
# a[::2] = b
# print(a)

import random
a = [random.randint(1, 100) for i in range(1, 20)]
print(a)
b = a[::2]
print(b)
b = sorted(b, reverse=True)
print(b)
a[::2] = b
print(a)
