# -*- coding: utf-8 -*-

def insert_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        # 如果当前值小于前一个元素,则将当前值作为一个临时变量存储,将前一个元素后移一位
        if list[i] < list[j]:
            temp = list[i]
            list[i] = list[j]

            # 继续往前寻找,如果有比临时变量大的数字,则后移一位,直到找到比临时变量小的元素或者达到列表第一个元素
            j = j - 1
            while j >= 0 and list[j] > temp:
                list[j+1] = list[j]
                j = j - 1
            # 将临时变量赋值给合适位置
            list[j+1] = temp

if __name__ == '__main__':
    list = [7, 11, 8, 12, 18, 2, 5, 9]
    print(list)
    insert_sort(list)
    print(list)

# 参考链接：https://www.cnblogs.com/AlwinXu/p/5444799.html
