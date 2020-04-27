#导入包
from flask import Flask,request,jsonify
#实例化一个
app =Flask(__name__)
#编写一个接口处理方法
@app.route("/api/sub",methods=["POST"])

def sub():
    if not request.json:#如果请求数据类型非json
        return jsonify({"code":"100001","msg":"请求类型错误","data":None})

    if not "a" in request.json or not "b" in request.json:#如果参数中没有a或b
        return jsonify({"code":"100002","msg":"参数缺失","data":None})

    a=request.json.get("a")
    b= request.json.get("b")
    result =str(float(a)-float(b))#使用float支持浮点数相减
    #使用jsonify将字典数据转换为json类型的相应数据
    return jsonify({"code":"100000","msg1":"成功","data":result})

if __name__ == '__main__':
    app.run()