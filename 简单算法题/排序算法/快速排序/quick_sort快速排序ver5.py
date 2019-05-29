#快排的主函数，传入参数为一个列表，左右两端的下标
def QuickSort(list,low,high):
    if high > low:
        #传入参数，通过Partitions函数，获取k下标值
        k = Partitions(list,low,high)
        #递归排序列表k下标左侧的列表
        QuickSort(list,low,k-1)
        # 递归排序列表k下标右侧的列表
        QuickSort(list,k+1,high)

def Partitions(list,leftindex,rightindex):
    i = leftindex
    j = rightindex
    temp = list[leftindex]
    while i < j:
        while list[i] <= temp:
            i += 1
        while list[j] > temp:
            j = j - 1
        if i < j:
            list[i], list[j] = list[j], list[i]

            # 另外一种写法
            # a = list[i]
            # list[i] = list[j]
            # list[j] = a

    list[leftindex] = list[j]
    list[j] = temp
    return j

list_demo = [6,1,2,7,9,3,4,5,10,8]
print(list_demo)
QuickSort(list_demo,0,9)
print(list_demo)

# 参考博客:https://www.cnblogs.com/kunpengv5/p/7833361.html
