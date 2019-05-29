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
