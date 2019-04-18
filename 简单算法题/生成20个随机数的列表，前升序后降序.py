# -*- coding: utf-8 -*-
import random
number = [random.randint(1, 100) for i in range(20)]
print(number)
former = sorted(number[0:10])
later = sorted(number[10:20], reverse=True)
print(former)
print(later)
