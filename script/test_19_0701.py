
num = float(input("输入一个数字: "))
if num > 0:
   print("大于0")
elif num == 0:
   print('{"msg":"账户被禁, 可联系在线客服 处理","code":1,"obj":null,"datas":null,"attributes":null,"ext1":"/user/home"}')
else:
   print("负数")