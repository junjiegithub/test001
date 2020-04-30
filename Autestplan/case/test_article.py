#导包  unnitest ApiArticle
import unittest
from Autestplan.api.api_article import ApiArticel
from parameterized import parameterized

#收藏文章获取数据
from Autestplan.tools.read_json import ReadJson
def get_data_add():
        #获取收藏文章 调试
    data = ReadJson("article_add.json").read_json()
    #新建空列表，添加读取json数据
    arrs = []
    arrs.append((data.get("url"),
                 data.get("headers"),
                 data.get("data"),
                 data.get("expect_result"),
                 data.get("status_code")))
    return arrs

#获取取消收藏测试数据
def get_get_data_cancel():
        data = ReadJson("article_cancel.json").read_json()
        # 新建空列表，添加读取json数据
        arrs = []
        arrs.append((data.get("url"),
                     data.get("headers"),
                     data.get("status_code")))
        return arrs


#新建测试类  继承
class TestArticle(unittest.TestCase):
    #新建收藏文章方法
    @parameterized.expand(get_data_add())
    def test01_collection(self,url,headers,data,expect_result,status_code):
        #临时数据
        # url ='http://ttapi.research.itcast.cn/app/v1_0/article/collections'
        # headers ={"Content-Type":"application/json","Authorization":"Bearer token信息"}
        # data ={"target":1}

        #调用收藏文章方法
        r=ApiArticel().api_post_collection(url,headers,data)

        #调用查看响应数据测试结果
        print("收藏响应数据为：",r.json())
        #断言响应状态码
        self.assertEqual(201,r.status_code)
        #使用动态数据获取状态码
        self.assertEqual(status_code,r.status_code)

        #断言响应信息
        self.assertEqual("OK",r.json()["message"])
        #使用动态数据获取响应信息
        self.assertEqual(expect_result,r.json()["message"])
    #新建取消收藏文章方法
    @parameterized.expand(get_get_data_cancel())
    def test02_cancel(self,url,headers,status_code):
        #临时数据
        # url='http://ttapi.research.itcast.cn/app/v1_0/article/collections/1'
        # headers={"Content-Type":"application/x-www-form-urlencoded",
		# 			"Authorization":"Bearer token信息"}
        #调用去取消收藏方法
        r= ApiArticel().api_delete_article(url,headers)

        #获取响应状态码
        print(r.status_code)
        #断言状态码
        # self.assertEqual(204,r.status_code)
        #使用动态获取 状态码
        self.assertEqual(status_code,r.status_code)

if __name__ == '__main__':
    unittest.main()