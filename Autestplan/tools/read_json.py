#导包
import json


# #打开json文件并获取文件流
# with open("../data/login.json","r",encoding='utf-8') as f:
#
# #调用load方法加载文件流
#     data =json.load(f)
#     print("获取的数据为：",data)
#
# #使用函数进行封装
# def read_json():
#     # 打开json文件并获取文件流
#     with open("../data/login.json", "r", encoding='utf-8') as f:
#         # 调用load方法加载文件流
#         data = json.load(f)
#

#使用参数替换 静态文件名
#新建读取工具类
class ReadJson (object):
#使用初始化方法 获取要读取的文件名称
    def __init__(self,filename):
        self.filepath = "../data/" +filename
#读取文件方法
    def read_json(self):
        # 打开json文件并获取文件流
        with open(self.filepath, "r", encoding='utf-8') as f:
            # 调用load方法加载文件流
            return json.load(f)

if __name__ == "__main__":
    # print(ReadJson("login.json").read_json())
    #登录数据调试
    # data=ReadJson("login.json").read_json()
    # arrs=[]
    # arrs.append((data.get("url"),
    #             data.get("mobile"),
    #             data.get("code"),
    #             data.get("expect_result"),
    #             data.get("status_code")))
    # print(arrs)

        #获取用户频道列表，调试
        # data=ReadJson("channels.json").read_json()
        # arrs=[]
        # arrs.append((data.get("url"),
        #             data.get("headers"),
        #             data.get("expect_result"),
        #             data.get("status_code")))
        # print(arrs)

        #获取收藏文章 调试
    # data = ReadJson("article_add.json").read_json()
    # #新建空列表，添加读取json数据
    # arrs = []
    # arrs.append((data.get("url"),
    #              data.get("headers"),
    #              data.get("data"),
    #              data.get("expect_result"),
    #              data.get("status_code")))
    # print(arrs)

    #获取取消收藏文章 调试
    data = ReadJson("article_cancel.json").read_json()
    #新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("status_code")))
    print(arrs)




"""
    问题：
        1。未经过封装无法在别的模块调用。
        2.数据存储文件有好几个，如果写死，在读取别的文件时无法使用
        3. 预期格式为列表嵌套元组（【url,mobile,code...】,）目前返回字典
    解决：
        1。进行封装
        2。使用参数替换静态写死的文件名
        3。读取字典内容并添加到新的列表中
"""