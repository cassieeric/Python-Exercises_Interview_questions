# -*- coding: utf-8 -*-
import random

number = [random.randint(0, 100) for i in range(10)]
# number = [random.randint(1000) for i in range(100)]

print(number)

for item in number:
    print(number.count(item), end=' ')
