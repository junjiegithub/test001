"""
for 临时变量 in 序列
    重复执行的代码
    。。。。。。
1.准备一个数据序列
2.for
"""
str1='itheima'
# for i in str1:
#     print(i)

for i in str1:
    if i=='e':
        print('遇到e不打印')
        break
    print(i)