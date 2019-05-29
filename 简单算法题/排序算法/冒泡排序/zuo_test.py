# -*- coding: utf-8 -*-
a = [7, 11, 8, 12, 18]
for i in range(0, len(a)):
    for j in range(0, i):
        if a[i] < a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
