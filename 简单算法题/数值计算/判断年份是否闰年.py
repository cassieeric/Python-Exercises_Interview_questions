# -*- coding: utf-8 -*-
year = int(input('Please input your year: '))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print('该年是闰年！')
else:
    print('该年不是闰年！')
