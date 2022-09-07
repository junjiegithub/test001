

""""
格式化输出
"""
age=18
name="TOM"
weight=75.5
stu_id=1
"""
我的年龄是X岁，
我的的名字是x
我的体重是X公斤、
我的学号是x
我的学好是001
我的名字是x，今年x岁了
我的名字是x，明年x岁了
我的名字是x，今年x岁了，体重x公斤，学号是x
"""

print("我的年龄是%d岁"%age)
print('我的名字是%s'%name)
print('我的体重是%0.2f'%weight)
print('我的学号是%s'%stu_id)
print('我的学号是%03d'%stu_id)
print('我的名字是%s,今年%d岁'%(name,age))
print('我的名字是%s,明年%d岁'%(name,age+1))
print('我的名字是%s,今年%d岁,体重%0.2f公斤，学号是%06d'%(name,age,weight,stu_id))
print('我的名字是%s，我的年龄是岁%s，我的体重是%s公斤'%(name,age,weight))

#f{}表达式
print(f"我的名字是{name}，我的年龄是{age}岁")
