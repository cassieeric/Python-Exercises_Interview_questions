# -*- coding: utf-8 -*-

# 计算100以内最大的素数
for n in range(100, 1, -1):
    # print(n, end=' ')
    for i in range(2, n):
        # print(i, end=' ')
        if n % i == 0:
            break
    else:
        print(n)
        break  # 注释的话则输出100以内所有的素数

