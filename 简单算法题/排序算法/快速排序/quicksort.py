# -*- coding: utf-8 -*-

def quick_sort(list, leftindex, rightindex):
    if leftindex < rightindex:
        k = partitions(list, leftindex, rightindex)
        quick_sort(list, leftindex, k-1)
        quick_sort(list, k+1, rightindex)

def partitions(list, leftindex, rightindex):
    i = leftindex
    j = rightindex
    temp = list[i]
    while i < j:
        while i < j and temp <= list[j]:
            j -= 1
        list[i] = list[j]
        while i < j and temp >= list[i]:
            i += 1
        list[j] = list[i]
    list[i] = list[j]
    list[j] = temp
    return j


if __name__ == '__main__':
    list1 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    print(list1)
    quick_sort(list1, 0, len(list1)-1)
    print(list1)

'''
    总结：
        1、快速排序的关键点在分解函数这块，很容易让人混淆。
        2、记得partitions函数里边用的是三个while，如果使用if语句，则会出现排序不完整的情况。
        3、在判断temp与list值对比的时候，记得先从右往左进行(while i < j and temp <= list[j]:)，
        如果将(while i < j and temp >= list[i]:)放在前面的话，则排序会不完整，无法达到预期的效果。
'''
