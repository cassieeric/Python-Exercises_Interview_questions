# -*- coding: utf-8 -*-

def insert_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        if list[i] < list[j]:
            list[i], list[j] = list[j], list[i]
            j = j - 1
            while j >= 0 and list[j] > temp:
                list[j+1] = list[j]
                j = j - 1
            list[j+1] = temp

if __name__ == "__main__":
    list = [7, 11, 8, 12, 18, 2, 5, 9, 20, 6, 32, 13]
    print(list)
    insert_sort(list)
    print(list)
