# -*- coding: utf-8 -*-
# 需求分析
# 1 新建名片
# 2 显示全部名片
# 3 查询某个人的信息

# 全局变量，所以数据都放到这里
cards = []

def show_menue():
    print("#"*50)
    print("————欢迎使用名片管理系统————")
    print('1 新建名片')
    print('2 显示全部名片')
    print('3 查询某个人的信息')
    print("#"*50)
    num = input('请输入您的需求：')
    if num == '1':
        create_card()
    elif num == '2':
        show_all_cards()
    elif num == '3':
        find_card()
    else:
        print('您的输入有误，请重新输入！')

def create_card():
    name = input('请输入您的名字： ')
    age = input('请输入您的年龄： ')
    tel = input('请输入您的号码：')

    print('您的名字是：', name)
    print('您的年龄是：', age)
    print('您的号码是：', tel)

    # 使用一个字典来表示一个人的详细信息
    card = {
        '姓名': name,
        '年龄': age,
        '号码': tel
    }

    # 向cards中添加一个名片信息
    cards.append(card)
    print('添加成功，这个人的名片信息是：')
    # print(cards)
    for i in cards:
        print(i)

def show_all_cards():
    print('@'*50)
    print('全部名片信息如下：')
    for i in cards:
        print(i)
    print('@' * 50)

def find_card():
    name = input('请输入您需要查询的名字：')
    # 遍历，不然直接使用字典查询的话逻辑上行不通
    for i in cards:
        if i['姓名'] == name:
            print('这个人的信息是：')
            print(i)
            break
        else:
            print('查无此人。。。')

if __name__ == '__main__':
    while True:
        show_menue()
