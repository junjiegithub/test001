"""
    目标：完成登录业务层实现
"""

#导包  unnittest ApiLogin
import unittest
from Autestplan.api.api_login import ApiLogin
from parameterized import parameterized
from Autestplan.tools.read_json import ReadJson
#读取数据函数
def get_data():
    datas = ReadJson("login_more.json").read_json()
    arrs = []
    # 使用遍历获取所有的values
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("mobile"),
                     data.get("code"),
                     data.get("expect_result"),
                     data.get("status_code")))


    return arrs


#新建测试类
class TestLogin(unittest.TestCase):
#新建测试方法
    @parameterized.expand(get_data())
    def test_login(self,url,mobile,code,expend_result,status_code):

    #暂时存放数据   url mobile code
        # url='http://ttapi.research.itcast.cn/app/v1_0/authorizations'
        # mobile ='18453288056'
        # code='882477'

    #调用登录方法
        s = ApiLogin.api_post_login(url,mobile,code)
    #断言  响应断言 及状态码
        # self.assertEqual("OK",s.json()['message'])
        self.assertEqual(expend_result,s.json()['message'])

    #断言响应状态码
        self.assertEqual(status_code,s.status_code)


if __name__ == '__main__':
    unittest.main()
