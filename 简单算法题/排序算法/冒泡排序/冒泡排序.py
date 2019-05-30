# -*- coding: utf-8 -*-

def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(0, i):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

if __name__ == '__main__':
    list1 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    bubble_sort(list1)
    print(list1)

    
'''
    总结：
        1、关键的地方是在两个for循环，而且第二个循环是在第一个之上的，存在关联。
        2、if list[i] > list[j]:这个判断，如果是大于号，代表的是降序排序。
        3、if list[i] < list[j]:这个判断，如果是小于号，代表的是升序排序。
        4、之后就是更换两个值，使用中间值temp。
'''
