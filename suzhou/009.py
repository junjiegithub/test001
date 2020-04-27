# from flask import Flask, request, jsonify
#
# app = Flask(__name__)
#
#
# @app.route("/api/sub/", methods=["POST"])
# def sub():
#     if not request.json:  # 如果请求数据类型非json
#         return jsonify({"code": "100001", "msg": "请求类型错误", "data": None})
#
#     if not "a" in request.json or not "b" in request.json:  # 如果参数中没有a或者没有b
#         return jsonify({"code": "100002", "msg": "参数缺失", "data": None})
#
#     a = request.json.get("a")
#     b = request.json.get("b")
#     result = str(float(a) - float(b))  # 使用float支持浮点数相减
#     return jsonify({"code": "100000", "msg": "成功", "data": result})  # 使用jsonify将字典数据转换为json类型的相应数据
#
#
# if __name__ == '__main__':
#     app.run()

# 1. 导入包
import requests

base_url = "http://127.0.0.1:5000"

#
# # 2. 组装请求
# def test_add_normal():
#     # url  字符串格式
#     url = base_url + "/add/"
#
#     # data {} 字典格式
#     data = {"a": "1", "b": "2"}
#     # 3. 发送请求,获取响应对象
#     response = requests.post(url=url, data=data)
#     # 4. 解析响应
#     # 5. 断言结果
#     assert response.text == '3'


# 1. 导入包
import requests
import json

base_url = "http://127.0.0.1:5000"

def test_sub_normal():
    url = base_url + "/api/sub/"
    headers = {"Content-Type": "application/json"} # 1. 必须通过headers指定请求内容类型为json
    data = {"a": "4", "b": "2"}
    data = json.dumps(data) # 2. 序列化成字符串
    response = requests.post(url=url, headers=headers, data=data)
    # 3. 响应解析 # 响应格式为: {"code":"100000", "msg": "成功", "data": "2"}
    resp_code = response.json().get("code")
    resp_msg = response.json().get("msg")
    resp_data = response.json().get("data")
    # 断言
    assert response.status_code == 200
    assert resp_code == "100000"
    assert resp_msg == "成功"
    assert resp_data == "2"