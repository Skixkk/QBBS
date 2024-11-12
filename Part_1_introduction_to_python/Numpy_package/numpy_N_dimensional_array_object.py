import numpy as np

'''
array1 = np.array(range(6))
array1.shape = 2,3 # 分成两个数组，每个数值含3个element
print(array1)
'''

array1 = np.array(range(6))
# print(array1)

shape = array1.shape
shape1 = shape
# print(shape1)

array1.shape = 2, 3  # 2行3列
# print(array1)

array2 = array1.reshape(3, 2)
# print(array2)
# print(array2.shape)
# print(array1.shape)

array1[1,2] = 88 # 将array1中的2行3列数改为88
# print(array1)
# print(array2) # array1 & array2 共同一个array1的数据

array3 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(array3)
print(array3.shape)

