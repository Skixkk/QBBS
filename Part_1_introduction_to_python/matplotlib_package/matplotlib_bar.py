import pandas as pd
import matplotlib.pyplot as plt

BTCUSDT = pd.read_csv('E:\\My_File_Code_and_Note\\1\\Quantitative_Investment_Using_Python_by_LiruiCai'
                      '\\Part_1_introduction_to_python\\pandas_package\\BINANCE_BTCUSDT_4h_2024_2_12_by_2024_11_1.csv')
# print(BTCUSDT.head())
close = close = BTCUSDT['close']
a = [0, 0, 0, 0]
for i in close:
    if (i > 2) & (i <= 3):
        a[0] += 1
    elif (i > 3) & (i <= 4):
        a[1] += 1
    elif (i > 4) & (i <= 5):
        a[2] += 1
    else:
        a[3] += 1
print(a)

plt.bar([2, 3, 4, 5], a)

plt.show()
"""
matplotlib.pyplot.bar(left, height=a, width=0.8, bottom=None, hold=None, **kwargs)
left, height,每根bar的X轴位置&竖直高度
width=0.8,调整bar的宽度
bottom=None, 设定bar底部Y轴坐标,设定Bar在Y轴的位置，即Bar_Drawing 不一定要紧贴X轴，可以设置为凌空位置bottom=2.0
hold=None,
matplotlib.pyplot.bar(left=[2, 3, 4, 5], height=a, width=1.0, bottom=2.0, color='blue', edgecolor='k', **kwargs)
plt.bar(left, height, width=0.8, bottom=None, **kwargs)
"""
"""
# 水平柱状图
matplotlib.pyplot.barh([2, 3, 4, 5], a, width=1.0, bottom=2.0, color='red', edgecolor='k',)
# 直方图
plt.hist(x, bins=10, range=None, normed=False, weight=None, cumulative=False, bottom=None, histtype='bar', orientation='vertical', **kwargs)
# cumulative=True ,累积直方图
# histtype='bar'/'barstacked'/'step'/'stepfilled'# 直方图、堆栈图、无填充线图、有填充线图 

plt.hist([2, 3, 4, 5], bins='auto') # bins=12
plt.hist([2, 3, 4, 5], range=(2.3, 5.5), orientation='horizontal', c='r', recoloured='blue') # bins=12
# 累积直方图
plt.hist([2, 3, 4, 5], range=(2.3, 5.5), orientation='horizontal', c='r', edgecoloered='blue') #
"""
"""
# 饼图
plt.pie(a, labels=('(2, 3]', '(3, 4]', '(4, 5]', '(5, 6]'), colors=('b', 'g', 'r', 'k'), shadow=Ture)
plt.title('BTCUSDT')
"""
"""
# 箱形图
data = np.random.randn(100)
#　plt.boxplot(x, notch=None, labels=None, sym='')
plt.boxplot(data, labels=('open', 'close', 'high', 'low'), sym='')
plt.title('BTCUSDT')
"""
"""
# 面向对象绘图
#　Figure对象是一个空白区域，一个Figure是一个绘图纸
#　创建一个Figure对象
fig = plt.figure()

Axes：每个figure对象可以包含一个或几个Axes对象，每个Axes对象即一个绘图区域，拥有自己独立的坐标系统
ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.1, 0.1, 0.3, 0.3])
ax1.plot(data, color='b')
ax2.plot(open[:10], color='g')
# ax1 setting
ax1.set_title('BTCUSDT')
ax1.set_xlabel('Time')
ax1.set_xticklabels(open.index[:10], rotation=25)
ax1.set_ylabel('Price')
ax1.set_yticklabels(close.index[:10], rotation=25)
ax.set_ylim([0, 100]) # (2.4, 2.65)
# ax2 setting
ax2.set_title('BTCUSDT')
ax2.set_xlabel('Time')
ax2.set_xticklabels(close.index[:10], rotation=25)
ax2.set_ylabel('Price')
ax2.set_yticklabels(close.index[:10], rotation=25)
ax2.set_ylim([0, 100]) # (2.4, 2.65)
"""
"""
# 多图绘制
# 如果一个Figure对象中包含多个Axes对象，每个Axes对象位置除了通过区域坐标和长度来设定以外，更为常用的是通过子图subplot（）函数来设定
1|2
---
3|4
ax1 = plt.subplot(221) # 子图排列为2*2形式，“1”表示第一个子图
ax2 = plt.subplot(222) # 最后一个“2”表示第二个子图
ax3 = plt.subplot(223)
ax4 = plt.subplot(224)
"""
open24 = BTCUSDT['open']
close24 = close['2024/05-2024/06']
volume24 = BTCUSDT['volume']
ax1 = plt.subplot(211)
ax1.plot(close24, color='k')
ax1.set_title('BTCUSDT')
ax1.set_xlabel('Time')
ax1.set_xticklabels(close24.index[:10], rotation=25)
ax1.set_ylabel('Price')
ax1.set_yticklabels(close24.index[:10], rotation=25)

volume = BTCUSDT['volume']
open15 = BTCUSDT['open']
ax2 = plt.subplot(212)
left1 = volume24.index[close24 >= open24]
high1 = volume24[left1]
ax2.bar(left1, high1, width=0.8, color='r')
left2 = volume24.index[close24 < open24]
high2 = volume24[left2]
ax2.bar(left2, high2, width=0.8, color='g')
ax2.set_title('BTCUSDT Volume')
ax2.set_xlabel('Time')
ax2.set_xticklabels(close24.index[:10], rotation=25)
ax2.set_ylabel('volume')
ax2.set_yticklabels(close24.index[:10], rotation=25)
           
# 一图多线
# 导入data information
high24 = BTCUSDT['high']
low24 = BTCUSDT['low']

# create Axes object
fig = plt.figure()
ax3 = fig.add_axes([0.1, 0.1, 0.8, 0.8])

# 在一个Axes上绘制4条曲线
ax3.plot(close24, lable='close', color='k')
ax3.plot(high24, '--*', lable='high', color='r')
ax3.plot(low24, '-+', lable='low', color='g')
ax3.plot(open24, '-.>', lable='open', color='g')

# 设置表头
ax3.set_title('BTCUSDT price')
ax3.set_ylabel('price')
ax3.set_yticklabels(close24.index[:10], rotation=25)
ax3.set.xlabel('Time')
ax3.set_xticklabels(close24.index[:10], rotation=25)
ax3.legend(loc='best')
plt.show()
