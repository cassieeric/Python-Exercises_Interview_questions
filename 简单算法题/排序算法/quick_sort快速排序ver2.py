# -*- coding: utf- 8 -*-

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
