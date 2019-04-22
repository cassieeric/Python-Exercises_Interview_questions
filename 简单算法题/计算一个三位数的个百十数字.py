# 定义一个变量为三位数
num = int(input('请输入一个三位数：'))
# a表示百位数，b表示十位数，c表示个位数
if len(str(num)) == 3:
    a = num // 100
    b = num // 10 % 10
    # c = num % 100 % 10
    c = num % 10
    print(a,b,c,end=' ')
else:
    print('不合格，请输入一个三位数！')
