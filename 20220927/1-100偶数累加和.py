"""
1.准备累加的数字 开始1 结束100 增量1
2.准备保存结果的变量result
3.循环加法运算--如果是偶数才加法运算--和2取余数为0
4.输出结果
5。验证结果

"""

# i=1
# result=0
# while i<=100:
#     #条件语句 --if
#     if i%2 ==0:
#         #加法运算
#         result+=i
#     i+=1
#
# #输出结果
# print(result)

i=2
result=0

while i<=100:
    result+=i
    i+=2

print(result)