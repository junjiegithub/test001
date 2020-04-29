
#基于代码-项目实战
#目标：1，熟悉接口自动化测试的流程   2.能够对一个项目的接口实现自动化测试

'''
1.熟悉接口自动化的测试的流程
1.需求分析
    请求（url，方法，数据）
    响应（响应数据，状态码）
2.挑选需要做自动化测试的功能
    时间，人员，接口复杂度
3.设计测试用例
    如果功能阶段设计过用例，直接拿过来使用即可
4.搭建自动化测试环境【可选】
    实现自动化使用的语言如：（python，pycharm）
5.设计自动化测试项目的架构【可选】
    （报告，参数化，用例执行框架）
6.编写代码
7.执行测试用例
    （unittest,pytest）
8.生成测试报告并分析结果
    (htmltextrunner,allure)

二。接口清单
登录接口
    1。1请求登录接口
        请求
            1。请求url：http://ttapi.research.itcast.cn/app/v1_0/authorizations
            2。请求方式：POST
            3。请求参数：Headers={"Content-Type":"application/json"}
            4。请求报文：{"mobile":"18453288056","code":"888888"}
        响应
            1。状态码：201
            2。响应数据
                {"message":"xxx"}
    1。2获取短信验证码
            提示：
                1。验证码发送在手机中，无法通过代码来获取，只能在手机中查看
                2。有效期一分钟
        1。请求url：http://ttapi.research.itcast.cn/app/v1_0/sms/codes/:mobile
            (mobile:手机号)
        2。状态码：200
        3。请求方法：GET

    提示：1。验证码发送成功后，在手机中查找
            2。每个手机号码1分钟之内只能接收一次
获取用户频道列表
收藏文章
取消文章

2。项目接口分析
分析接口文档

3。挑选需要做接口测试的功能

二，获取用户频道列表
    2。1 请求：
        1。请求url：http://ttapi.research.itcast.cn/app/v1_0/user/channels
        2。请求方法：GET
        3). 请求参数：Headers = {"Content-Type":"application/json",
					"Authorization":"Bearer token信息"}
							提示：默认token有效期为2小时。

	2。2 响应：
	    1). 响应状态码：200
		2). 响应数据：{"message":"xxx"}

三，收藏文章
    3。1请求
        1。请求url地址：http://ttapi.research.itcast.cn/app/v1_0/article/collections
        2。请求方法：post
        3。请求参数：Headers = {"Content-Type":"application/json",
					"Authorization":"Bearer token信息"}

		4。请求报文
		    {"target":文章id}

    3.2响应
        1。响应状态码：201
        2。响应数据：{"message":"xxx"}

四。取消收藏文章
    4。1请求
        1。请求url：http://ttapi.research.itcast.cn/app/v1_0/article/collections/:target
        （：target为文章id）
        2。请求参数：
                Headers = {"Content-Type":"application/x-www-form-urlencoded",
					"Authorization":"Bearer token信息"}
		3。请求方法：
		        DELETE

	4。2响应
	    1。204

'''









