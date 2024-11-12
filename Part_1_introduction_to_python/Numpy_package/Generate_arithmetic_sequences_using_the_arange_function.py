import numpy as np

# array4 = np.arange(13,1,-1) # 起始，结束，步长
# # array（） 在创建数组序列时，不包含结束值
# print(array4)
#
# array4.shape = 2,2,3
# print(array4)
#
# array5 = array4.reshape(3,2,2)
# print(array5)

# Linspace（） 在创建数组序列时，不包含结束值
# array6_1 = np.linspace(0,1,5) # 起始，结束，原始个数
# print(array6_1)
# array_mul = np.multiply(array6_1,array6_1)
# print(array_mul)
# array_m = np.multiply(array6_1,100)
# print(array_m)

# array6_2 = np.linspace(1,12,12)
# print(array6_2)
# print(array6_2.dtype) # 默认数据类型为float浮点数

# # 通过设定dtype输出int
# array6_3 = np.linspace(1,12,12,dtype=int)
# print(array6_3)
# print(array6_3[0]) # print第一个数
# print(array6_3[-1]) # print倒数第一个数
# print(array6_3. dtype) # int整数类型

# a = np.zeros((4,5))
# print(a)
# print(a.dtype)

# b = np.zeros((2,5,4),dtype=np.int16) # create 2 shape
# print(b)
# print(b.dtype)

# c = np.empty((3,2))
# print(c)
# print(c.dtype)
# c.dtype = np.int16
# print(c)
# print(c.dtype)

# # index value of shape
# a1 = np.arange(0,30,1,dtype=int)
# print(a1)
#
# a2 = np.array(range(30),dtype=int)
# print(a2)

# a3 = np.linspace(1, 26, 6, dtype=int)
# print(a3)
# print(a3.shape)
# # 索引shape 中的第4个element
# print(a3[3])
# # array[start:end],第2个不被索引，索引数3 to 4
# print(a3[1:3])
# # 从0开始索引到第4个element，第4个element不被索引（从左往右索引）
# print(a3[:3])
# # 从最后一个开始索引到倒数第4个element，倒数第4个element不被索引（从右往左）
# print(a3[-3:])
# # 索引从右往左数倒数第4个element
# print(a3[-3])
# # 从第三个element[2],到倒数第二个element
# print(a3[2:-1])

# # 数组常用运算unfunc function shape
# # 加
# add = np.add(2,3)
# print(add)
# # 减
# substract = np.subtract(2,3)
# print(substract)
# # 乘
# multiply = np.multiply(2,3)
# print(multiply)
# # 除法
# divide = np.divide(2,3)
# print(divide)
# # mod = a % b，求余数，被整除法，output为0
# mod = np.mod(3,3)
# print(mod)
# # remainder = a % b,求余数，被整除，output为0
# remainder = np.remainder(9,3)
# print(remainder)
# # 2^3  power = a ** b
# power = np.power(2,3)
# print(power)
# # a^2
# square = np.square(4)
# print(square)
