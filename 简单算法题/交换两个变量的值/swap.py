-*- coding: utf-8 -*-
# 方法一：传统的交换方法，也是最常用的
def swap(list, i, j):
  if i <j:
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    
# 方法二：高级交换方法，在Python中可以用
def swap(list, i, j):
  if i <j:
    list[i], list[j] = list[j], list[i]
   
'''
  总结：
    1、第一种交换变量值的方法较为常用，一般引入第三变量。
    2、第二种交换方法属于Python中的高级用法，下次见到的时候就知道，原来是在做交换。
    3、第二种交换方法不可以拆分为两行代码，否则会报错。
    如拆分为：
      list[i] = list[j]
      list[j] = list[i]
      会出现报错，列表索引溢出
'''
    
    
   
