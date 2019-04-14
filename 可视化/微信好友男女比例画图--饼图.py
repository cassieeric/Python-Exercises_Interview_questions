import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import itchat

itchat.login()
# 爬取自己好友的信息，返回一个json文件
friends = itchat.get_friends(update=True)[0:]

# 初始化计数器
Male = Female = Unknown = 0
# friends[0]是自己的信息，所以要从friends[1]开始
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        Male += 1
    elif sex == 2:
        Female += 1
    else:
        Unknown += 1
# 计算朋友总数
total = str(len(friends[1:]))
# print (total)
count = 'There are '+total+' people in the WeChat circle' # fontproperties
labels = ['Unknown', 'Male', 'Female']
# colors = ['red', 'yellowgreen', 'lightskyblue']
X = [Unknown, Male, Female]
fig = plt.figure()
# 画饼图（数据，数据对应的标签，百分数保留两位小数点）
# plt.pie(X, labels=labels, autopct='%1.2f%%')
plt.title("WeChat's circle gender ratio")
plt.xlabel(count)

# plt.show()
#
# plt.savefig("PieChart.jpg")

# 直方图
x = [1, 2, 3]
y = X

plt.figure(figsize=(15, 10), dpi=80)

plt.title('sex ratio analysis')


plt.bar(x, y, width=0.5, align='center', facecolor='yellowgreen', edgecolor='white')

plt.xlabel('sex')
plt.ylabel('number')

for a, b in zip(labels, y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va='bottom', fontsize=12)


plt.title('Sex distribution plot')

plt.show()
