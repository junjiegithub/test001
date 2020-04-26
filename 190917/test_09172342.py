#coding=utf-8

import random

number = random.randint(0,2)

while 1:
    getNum =int(input('请输入你的数字：'))

    if getNum ==number:
        print('恭喜你，你猜对，奖励你20元现金哦')
        break

    elif getNum >number:
        print('你猜的数据比结果大了，扣除10元')

    else:
        print('你猜的结果比结果小了，扣除10元')





