# -*- coding: utf-8 -*-

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]


if __name__ == '__main__':
    list = [2, 5, 4, 8, 9, 6, 12, 18]
    print(list)
    selection_sort(list)
    print(list)
