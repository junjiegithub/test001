# #coding =utf-8
# import json
# json_str ="""
#
# {"avatar_large": "https://cdn.v2ex.com/navatar/8613/985e/90_large.png?m=1585387365", "name": "python", "avatar_normal": "https://cdn.v2ex.com/navatar/8613/985e/90_normal.png?m=1585387365", "title": "Python", "url": "https://www.v2ex.com/go/python", "topics": 13020, "footer": "", "header": "这里讨论各种 Python 语言编程话题，也包括 Django，Tornado 等框架的讨论。这里是一个能够帮助你解决实际问题的地方。", "title_alternative": "Python", "avatar_mini": "https://cdn.v2ex.com/navatar/8613/985e/90_mini.png?m=1585387365", "stars": 8950, "aliases": [], "root": false, "id": 90, "parent_node_name": "programming"}
#
# """
#
# res =json.loads(json_str)
#
# print(res)
# print(res['id'])
# print(res['name'])
# print(res['url'])

#
# import unittest
#
# class StringTestCase(unittest.TestCase):
#     def setUp(self) :
#         self.test_string ="This is a string"
#
#     def testUpper(self):
#         self.assertEqual("THIS IS A STRING",self.test_string.upper())
#
# if __name__ == '__main__':
#     unittest.main()

# import requests
# import unittest
#
# class V2exAPITestCase(unittest.TestCase):
#     def test_node_api(self):
#         url="https://www.v2ex.com/api/nodes/show.json"
#         querystring={"name":"python"}
#         response =requests.request("GET",url,params=querystring).json()
#         self.assertEqual(response['name'],'python')
#         self.assertEqual(response['id'],90)
#         print(response['id'])
#         print(response)
#
# if __name__ == '__main__':
#     unittest.main()


#
# from flask import Flask, jsonify, g
# import copy
# app = Flask(__name__)
#
# @app.before_request
# def set_up_data():
#     g.data = [
#         {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
#         {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
#         {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
#         {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
#         {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
#     ]
#
#     g.task_does_not_exist = {"msg": "task does not exist"}
#
# @app.route('/api/tasks')
# def get_all_tasks():
#     return jsonify(g.data)
#
# @app.route('/api/tasks/<int:task_id>')
# def get_task(task_id):
#     if task_id > 0 and task_id <= len(g.data):
#         return jsonify(g.data[task_id])
#     else:
#         return jsonify(g.task_does_not_exist)
#
# @app.route('/api/tasks/<int:task_id>', methods=['PUT'])
# def complete_task(task_id):
#     if task_id > 0 and task_id <= len(g.data):
#         tmp = copy.deepcopy(g.data[task_id])
#         tmp['done'] = True
#         return jsonify(tmp)
#     else:
#         return jsonify(g.task_does_not_exist)

#coding =utf-8
# import json
# import requests
# url = 'http://47.75.7.156:7300/api/u/login'
# data ={
#     "name":"easymock01",
#     "password":"123456",
# }
# result=requests.post(url,data).json()
# print(result)

#coding =utf-8
import requests
import json
import unittest

def send_post(url=None,data=None):
    result =requests.post(url=url,data=data).json()
    res =json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2)
    print(res)

if __name__ == "__main__":
    url='http://47.75.7.156:7300/api/u/login'
    data={
        'name':"easymock01",
        'password':"123456",
        }
    post =send_post(url=url,data=data)
