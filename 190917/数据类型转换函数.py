
#1.float()--将数据类型转换成浮点型
num=1
str1='10'

print(float(num))
print(float(str1))

#2.str()--将数据类型转换成字符串类型
print(str(num))

#3.tuple()--将一个序列转换成元组
list1=[10,20,30]
print(tuple(list1))
#4.list()--将一个序列转换成列表
t1=(100,200,300)
print(list(t1))

#5,eval()--计算在字符串里的有效python表达式，并返回一个对象
str2='1'
str3='1.1'
str4='(100,200,300)'
str5='[100,200,300]'

print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))

