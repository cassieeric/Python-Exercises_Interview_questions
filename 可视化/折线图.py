# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import matplotlib

# 设置中文，解决中文乱码问题
font = {
    "family": "AR PL UMing CN, SimHei",
    "size": "10"
}
matplotlib.rc('font', **font)

# 描述一下今天晚上10点的一个气温分布
times = ["10点00分", "10点10分", "10点20分", "10点30分", "10点40分", "10点50分", "11点00分"]
x = range(len(times))
# x = ['10', '10.10', '10.20', '10.30', '10.40', '10.50', '11.00']
temperature = [15, 16, 17, 14, 18, 15, 17]

# 设置图片的大小，dpi是分辨率
plt.figure(figsize=(20, 10), dpi=80)

# 画图，存放在内存中，并没有显示到屏幕上
plt.plot(x, temperature, 'ro-')

plt.xticks(x, times)
plt.margins(0.08)
plt.subplots_adjust(bottom=0.15)

# 对图片进行详细的说明
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('温度分布图')

# 保存图片
plt.savefig('中文折线图.jpg')

# 把绘制好的图片显示出来
plt.show()
