#break:当某些条件成立，退出整个循环
#循环吃5个苹果，吃完第3个吃饱了，第四个和第5个不吃了（不执行）  --==4或>3

i=1
while i<=5:
    #条件：如果吃到4或>3打印吃饱了，不吃了
    if i==4:
        print('吃饱了，不吃了')
        break
    print(f'吃了第{i}个苹果')
    i+=1