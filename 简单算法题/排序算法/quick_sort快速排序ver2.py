# -*- coding: utf- 8 -*-

'''
说起快排的Python实现，首先谈一下，快速排序的思路：

1、取一个参考值放到列表中间，初次排序后，让左侧的值都比他小，右侧的值，都比他大。

2、分别对左侧和右侧的部分递归第1步的操作

实现思路：

两个指针left，right分别指向列表的第一个元素和最后一个元素，然后取一个参考值，默认为第一个列表的第一个元素list[0]，称为K
然后left指向的值先和参考值K进行比较，若list[left]小于或等于K值，left就一直向右移动，left+1，直到移动到大于K值的地方，停住
right指向的值和参考值K进行比较，若list[right]大于K值，right就一直向左移动，right-1，直到移动到小于K值的地方，停住
此时，left和right若还没有相遇，即left还小于right，则二者指向的值互换
若已经相遇则说明，第一次排序已经完成，将list[right]与list[0]的值进行互换，进行之后的递归。

'''

#快排的主函数，传入参数为一个列表，左右两端的下标
def QuickSort(list,low,high):
    if high > low:
        #传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list,low,high)
        #递归排序列表k下标左侧的列表
        QuickSort(list,low,k-1)
        # 递归排序列表k下标右侧的列表
        QuickSort(list,k+1,high)

def Partitions(list,low,high):
    left = low
    right = high
    #将最左侧的值赋值给参考值k
    k = list[low]
    #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
    while left < right :
        #当left对应的值小于k参考值，就一直向右移动
        while list[left] <= k:
            left += 1
        # 当right对应的值大于k参考值，就一直向左移动
        while list[right] > k:
            right = right - 1
        #若移动完，二者仍未相遇则交换下标对应的值
        if left < right:
            list[left],list[right] = list[right],list[left]
    #若移动完，已经相遇，则交换right对应的值和参考值
    list[low] = list[right]
    list[right] = k
    #返回k值
    return right

list_demo = [6, 1, 2, 7, 9, 3, 4, 5, 10, 8]
print(list_demo)
QuickSort(list_demo,0,9)
print(list_demo)

# 参考链接：https://www.cnblogs.com/kunpengv5/p/7833361.html
