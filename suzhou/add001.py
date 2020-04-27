#coding=utf-8
import requests
import flask

#1，从flask中导入Flash类和request对象
from flask import Flask,request

#2，从当前模块实例化出一个Flask实例
app =Flask(__name__)

#3,编写一个接口处理方法
#4.挂载路由（制定接口的url路径），声明接口接受的方法
@app.route("/add/",methods=["GET","POST"])
def add():
    #3.1从请求中获取参数
    #request.valuses {"a":"1","b":"2"}
    a=request.values.get("a")
    b=request.values.get("b")
    #3.2 业务操作
    sum = int(a)+int(b)
    #3.3组装响应并返回
    return str(sum)

#5.运行接口
if __name__ =='__main__':
    app.run() #默认5000端口，可以指定端口app.run（port=50001）

