# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [873, 560, 102]

plt.figure(figsize=(15, 10), dpi=80)

plt.bar(x, y)

plt.xlabel('sex')
plt.ylabel('number')
plt.title('Distribution plot')

plt.show()
