"""
坐公交：如果有钱可以上车，没有钱，不能上车：  如果上车了，判断是否能坐下---是否有空座位
1
1

"""

money=int(input("请确认是否有钱坐车，有钱请输入1，没钱输入0"))


if money ==1:
    print("你好，请上车")
    seat = int(input("请确认是否有座位，有位请输入1，没钱输入0"))
    if seat ==1:
        print("有座位，请坐把")
    else:
        print("没座位，你先站一下")
else:
    print("不好意思，你没有钱，坐不了车")
