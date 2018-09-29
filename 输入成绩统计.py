# -*- coding: utf-8 -*-

# 自己写的代码
# sum = 0
#
# while True:
#     question = input('Do you want to input your score one more time?: ')
#     if question == 'yes':
#         score = int(input('Please input your score: '))
#         sum += score
#         print('The current total scores are: ', sum)
#     else:
#         break


# 书上的参考代码
endFlag = 'yes'
s = 0

while endFlag.lower() == 'yes':
    score = int(input('Please input your score: '))
    if 0 <= score <= 100:
        s += score
    else:
        print('The number is incorrect!')
    endFlag = input('Do you want to input your score one more time?(yes or no?): ')

print('The sum of the scores is: ', s)


