# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# BTCUSDT = pd.read_csv('E:\\My_File_Code_and_Note\\1\\Quantitative_Investment_Using_Python_by_LiruiCai'
#                       '\\Part_1_introduction_to_python\\pandas_package\\BINANCE_BTCUSDT_4h_2024_2_12_by_2024_11_1.csv')
# # print(BTCUSDT.head())
# index =pd.to_datetime(BTCUSDT.index)
# # print(index)
# close = BTCUSDT['close']
# # print(close)
#
# draw = plt.plot(close)
# plt.show()

# draw2 = plt.plot([1, 1, 0, 0, -1, 0, 1, 1, -1])
# # 取消默认axes.unicode_minus值unicode的minus类型，去掉负数字体不兼容问题,rcParams:参数字
# plt.rcParams['axes.unicode_minus'] = False
# # font.sans-serif：无衬线字体属性，为字典的一个key
# plt.rcParams['font.sans-serif'] = ['Arial']
# plt.rcParams['font.sans-serif'] = ['SimHei']
# x轴边界
# plt.xlim(0, 6)
# # y轴边界
# plt.ylim(-1.5, 1.5)
# # 坐标标签
# # s1 = pd.Series([1, 2, 3], index=pd.date_range('20240101', periods=3))
# plt.xticks(range(9), ['2024-02-21', '2024-02-22', '2024-02-23', '2024-02-24', '2024-02-25', '2024-02-26',
#                       '2024-02-27', '2024-02-28', '2024-02-29'], rotation=45)
# plt.xticks(range(9), ['2024-02-21', '2024-02-22', '2024-02-23', '2024-02-24', '2024-02-25', '2024-02-26',
#                       '2024-02-27', '2024-02-28', '2024-02-29'])
# plt.yticks(np.arange(-1, 1.5, step=0.1))
# plt.title('BTCUSDT.P Trading History', loc='center', fontweight='bold', fontsize='large')
# plt.xlabel('Date', fontweight='bold', fontsize='large')
# plt.ylabel('Price', fontweight='bold', fontsize='large')
# plt.grid(True, axis='y') # axis='y' axis='x' axis='bath'
"""
图例设置需要
# plt.plot(close['2024'], label='close', color='blue')
# plt.plot(open['2024'], label='open', color='red')
最适宜位置：'best'
右上角：'upper right'
左上角：'upper left'
左下角：'lower left'
右下角：'lower right'
右侧：'right'
左侧中间：'center left'
右侧中间：'center right'
下方中间：'lower center'
中间：'center'
"""
# plt.legend('best', labelspacing=0.5, fontsize='large')
"""
实线:'solid'
虚线:'dashed'
线点:'dashdot'
点线:'dotted'
不画线:'None'
# plt.polt(close['2024'], c='r', label='close', color='blue' ,linestyle='solid', alpha=0.5)
# plt.polt(open['2024'], c='b', label='open', color='red', linestyle='dashed', alpha=0.5)
# plt.legend()
# plt.xlabel('Date', fontweight='bold', fontsize='large')
# plt.ylabel('Price', fontweight='bold', fontsize='large')
plt.title('BTCUSDT')
plt.grid(True, axis='y')
"""
"""
red:'r'
black:'k'
blue:'b'
cyan:'c'
yellow:'y'
white:'w'
green:'g'
# plt.polt(close['2024'], c='r', label='close', alpha=0.5)
# plt.polt(open['2024'], c='b', ls='--', label='open', alpha=0.5)
# plt.legend(loc='best')
# plt.xlabel('Date', fontweight='bold', fontsize='large')
# plt.ylabel('Price', fontweight='bold', fontsize='large')
# plt.title('BTCUSDT')
# plt.grid(True, axis='both')
"""
"""
点：'point'   '·'
圆圈：'circle' 'o'
向下三角：'triangle_down'    'v'    
向上三角：'triangle_up'   '^'
向左三角：'triangle_left'    '<'
向右三角：'triangle_right'   '>'
正方形：'square'    's'
五边形：'pentagon'  'p'
六边形：'hexagonl'  'h'
加号：'plus'   '+'
叉号：'x'  'x'
钻石：'diamond'    'D'
星号：'star'   '*'
竖线：'vline'  '|'
# plt.polt(close['2024'], marker='o', label='close')
# plt.polt(open['2024'], marker='*',  label='open')

# plt.polt(close['2024'], '--rD', label='close')
# plt.polt(open['2024'], '--b>',  label='open')
"""
"""
线条宽度
# plt.polt(close['2024'], '--rD', label='close', linewidth=2)
# plt.polt(open['2024'], '--b>',  label='open', lw=2)
# plt.legend(loc='best')
# plt.xlabel('Date', fontweight='bold', fontsize='large')
# plt.ylabel('Price', fontweight='bold', fontsize='large')
# plt.title('BTCUSDT')
# plt.grid(True, axis='both')
"""
# plt.show()
