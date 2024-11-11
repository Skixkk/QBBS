"""
for variable in sequeue:
    statements
"""
# for variable
for i in range(1, 11):
    print(i)
    pass

a = list()
for i in 'python':
    a.append(i + 'python')
    print(a)
    pass

print(a)
# simple symbol
a1 = [i + 'python' for i in 'python']
print(a1)
list1 = [2, 10, 34, 3, 10, 20, 10]
a1 = [i for i in range(len(list1)) if list1[i] == 10]
print(a1)
"""
while 循环语句的形式为：
while expression:
    statement
当while循环的expression为True时，执行statement代表的语句或者语句块的内容；
当expression为False时，跳出循环，执行statements下面一行的代码
"""
# while variable
a = 0
while a < 4:
    a += 1
    print(a + 26)
    pass
print(a)
"""
嵌套循环
# for 嵌套循环
for variable1 in sequence:
    for variable2 in sequence:
    statements1
statements2
# while 嵌套循环
while expression:
    while expression:
       statements1
    statements2
"""
# for 嵌套循环
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
z = []
for i in x:
    for j in y:
        z.append([i, j])
        pass
    pass
pass
print(z)
# 一行代码实现的上面for循环，建议使用上面的
z1 = [[i, j] for i in x for j in y]
print(z1)

# break、continue、pass 语句
# break
st1 = ['a', 'b', 'python', 'c', 'd']
for i in st1:
    print(i)
    if i == 'python':
        break  # 跳出for循环
    pass
pass
# 缩进格式一
for i in st1:
    print(i)
    if i == 'python':
        break
    print('hello')  # 和print(i)语句缩进格式相同，属于同级关系
    pass
pass
# continue：跳过本语句或者一个语句块代码
for i in st1:
    if i == 'python':
        continue  # 停止执行当前循环语句中的内容，并进入下一次循环
    print(i)  # 在for循环语句内部
print('hello')  # 在for循环语句内部，在for循环语句执行结束后执行

for i in st1:
    if i == 'python':
        continue
    print(i)  # 在for循环内部
    print('hello')  # 在for循环内部
    pass
pass

for i in st1:
    print(i)
    if i == 'python':
        continue  # continue下面无for循环中的语句
        pass
    print('hello')
    pass
pass

for i in st1:
    if i == 'python':
        continue
        # print(i)  # 在 for 循环的if语句内部，位于continue下方，永远不会被执行
        pass
    print('hello')
    pass
pass

# pass语句：属于空（null）操作，pass语句一般作为一种占位语句，执行时系统没有任何反应
for i in range(5):
    if i > 3:
        pass
    print([i, i + 3])
    pass
pass

for i in range(5):
    if i > 3:
        print([i, i + 3])
    pass
pass
