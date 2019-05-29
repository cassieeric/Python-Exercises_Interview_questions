# -*- coding: utf-8 -*-

def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(0, i):
            if list[i] > list[j]:
                temp = list[i]
                list[i] = list[j]
                list[j] = temp
    print(list)

if __name__ == '__main__':
    list1 = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
    bubble_sort(list1)
