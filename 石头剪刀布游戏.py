# -*- coding: utf-8 -*-
import random

while True:
    # 1 石头，2 剪刀，3 布
    computer = random.randint(1, 3)
    people = int(input('请输入数字1(石头)或2(剪刀)或3(布):'))

    if people > 3 or people < 1:
        people = int(input('对不起，您输错了，请重新输入正确的数字：'))

    if (computer == 1 and people == 3) or (computer == 2 and people == 1) or (computer == 3 and people == 2):
        print('小伙子，您赢了，真厉害~~')

    elif computer == people:
        print('平局，再来一次！')

    else:
        print('对不起，您输了，再来一局')
