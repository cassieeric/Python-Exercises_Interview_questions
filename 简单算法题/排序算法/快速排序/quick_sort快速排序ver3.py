# -*- coding: utf- 8 -*-

def find_middle_value(list, leftindex, rightindex):
    i = leftindex
    j = rightindex
    temp = list[i]
    if leftindex < rightindex:
        while i < j:
            while i < j and temp <= list[j]:
                j = j - 1
            list[i] = list[j]
            while i < j and temp >= list[i]:
                i = i + 1
            list[j] = list[i]

        list[j] = temp
        return i



def quicksort(list, leftindex, rightindex):
    if leftindex < rightindex:
        temp = find_middle_value(list, leftindex, rightindex)
        quicksort(list, leftindex, temp-1)
        quicksort(list, temp+1, rightindex)

if __name__ == '__main__':
    list1 = [2, 8, 7, 1, 3, 5, 6, 4]
    print(list1)
    quicksort(list1, 0, len(list1)-1)
    print(list1)
