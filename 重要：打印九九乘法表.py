# -*- coding: utf-8 -*-
for i in range(1, 10):
    # print('\t')
    for j in range(1, i+1):
    # for j in range(1, 10):
        print('%s*%s=' % (i, j), i * j, end='\t')
    print('\n')  # 这个地方务必要加上
        # print('%s*%s=' % (i, j), i * j, end='\t')
        # print('\t')
