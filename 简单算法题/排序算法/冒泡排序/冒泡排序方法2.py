# -*- coding: utf-8 -*-

def bubble_sort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

if __name__ == '__main__':
    list = [7, 11, 8, 12, 18, 2, 5, 9]
    print(list)
    bubble_sort(list)
    print(list)

'''
第一次内层循环的结果就是找到最大的值

第二次内层循环的结果就是找到次大的值,本次将忽略最后一个元素的比较

第二次内层循环的结果就是找到第三大的值，本次讲忽略倒数第二个元素和最后一个元素的比较

参考链接：https://www.cnblogs.com/xiaxiaoxu/p/9529028.html
'''
