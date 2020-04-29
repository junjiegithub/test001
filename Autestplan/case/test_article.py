#导包  unnitest ApiArticle
import unittest
from Autestplan.api.api_article import ApiArticel

#新建测试类  继承
class TestArticle(unittest.TestCase):
    #新建收藏文章方法
    def test01_collection(self):
        #临时数据
        url ='http://ttapi.research.itcast.cn/app/v1_0/article/collections'
        headers ={"Content-Type":"application/json","Authorization":"Bearer token信息"}
        data ={"target":1}

        #调用收藏文章方法
        r=ApiArticel().api_post_collection(url,headers,data)

        #调用查看响应数据测试结果
        print("收藏响应数据为：",r.json())
        #断言响应状态码
        self.assertEqual(201,r.status_code)
    #新建取消收藏文章方法
    def test02 cancel(self):
        #临时数据
        url=''
        headers={}
        #调用去取消收藏方法
        ApiArticel().api_delete_article()
        #断言状态码