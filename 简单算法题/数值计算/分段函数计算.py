# -*- coding: utf-8 -*-
x = int(input('Please input your number: '))

if x < 0 or x >= 20:
    y = 0
elif 0 <= x < 5:
    y = x
elif 5 <= x < 10:
    y = 3 * x - 5
# elif 10 <= x < 20:
else:
    y = 0.5 * x - 2
print(y)
