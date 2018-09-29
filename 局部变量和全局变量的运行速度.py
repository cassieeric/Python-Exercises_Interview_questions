# -*- coding: utf-8 -*-
import time
import math
from math import sin as sin

start_time1 = time.time()
for i in range(10000000):
    math.sin(i)
end_time1 = time.time()
time_consuming1 = end_time1 - start_time1
print('Time consuming: ', time_consuming1)


start_time2 = time.time()
for i in range(10000000):
    sin(i)
end_time2 = time.time()
time_consuming2 = end_time2 - start_time2
print('Time consuming: ', time_consuming2)


loc_sin = math.sin
start_time3 = time.time()
for i in range(10000000):
    loc_sin(i)
end_time3 = time.time()
time_consuming3 = end_time3 - start_time3
print('Time consuming: ', time_consuming3)
