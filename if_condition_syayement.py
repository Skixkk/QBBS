"""
if...else...
"""
a = 6
b = 4
if a > b:
    print("a is greater than b")
else:
    print("a is less than b")
    pass

if a > 5 and b > 5:
    a += 6
else:
    b += 6
    pass
print(a)
print(b)

# 多条件判断
grade = 95
if grade >= 90:
    print("Grade is greater than or equal to 90")
elif all([grade > 70, grade < 90]):
    print("Grade is greater than or equal to 70 and less than 90")
else:
    print("Grade is greater than 70 and less than 90")
    pass
# 简便表示
a = 6
b = 4
var1 = 'a' if a > b else 'b'
print(var1)

# 三元操作语句赋值,{}为空字典，返回False，执行a = '123';不为空，返回True，执行a = 4**3 # 64
a = 4**3 if {} else '123'
print(a)