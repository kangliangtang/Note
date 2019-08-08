
import json

# dic = {"type": "String", "key": "nametest", "success":True}
# js = json.dumps(dic)
# # print(js)
# # js = {}
#
# if isinstance(json.loads(js), dict):
#     l = json.loads(js)
#     print(l)
#     print(type(l))


# d = {
# 					"mode": "raw",
# 					"raw": "{\"body\": {\n\t\t\t\t\t\"mode\": \"formdata\",\n\t\t\t\t\t\"formdata\": [\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"name\",\n\t\t\t\t\t\t\t\"value\": \"test\",\n\t\t\t\t\t\t\t\"type\": \"text\"\n\t\t\t\t\t\t},\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"case_file_path\",\n\t\t\t\t\t\t\t\"value\": \"D:\\\\Work\\\\testcases\\\\tem/15559985354784672\",\n\t\t\t\t\t\t\t\"type\": \"text\"\n\t\t\t\t\t\t},\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"\",\n\t\t\t\t\t\t\t\"value\": \"\",\n\t\t\t\t\t\t\t\"type\": \"text\",\n\t\t\t\t\t\t\t\"disabled\": true\n\t\t\t\t\t\t}\n\t\t\t\t\t]\n\t\t\t\t}}"
# 				}
#
#
# print(type(d["raw"]))
# print(json.loads(d["raw"]))

# l = []
# dic = {}
#
# d = json.dumps(l)
# print(d)
# d2 = json.dumps(dic)
# print(d2)


# l = 'ca..'
# print(l.split('.')[-1])

# js = "{\"mode\": \"formdata\"}"
# js = "{\"body\": {\n\t\t\t\t\t\"mode\": \"formdata\",\n\t\t\t\t\t\"formdata\": [\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"name\",\n\t\t\t\t\t\t\t\"value\": \"test\",\n\t\t\t\t\t\t\t\"type\": \"text\"\n\t\t\t\t\t\t},\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"case_file_path\",\n\t\t\t\t\t\t\t\"value\": \"D:\\\\Work\\\\testcases\\\\tem/15559985354784672\",\n\t\t\t\t\t\t\t\"type\": \"text\"\n\t\t\t\t\t\t},\n\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\"key\": \"\",\n\t\t\t\t\t\t\t\"value\": \"\",\n\t\t\t\t\t\t\t\"type\": \"text\",\n\t\t\t\t\t\t\t\"disabled\": true\n\t\t\t\t\t\t}\n\t\t\t\t\t]\n\t\t\t\t}}"
# dic = json.loads(js)
# print(type(dic))
# print(dic)
# js_2 = json.dumps(dic)
# print(type(js_2))
# print(js_2)
# dic = {"key":"val"}
# l = [{"key":"val"}]
# js = json.dumps(l)
# print(js)
# print(json.dumps(dic))

# import os
# print(os.listdir('./')
#
import json
# l = ['创建策略', '获取策略列表', '删除策略', '编辑更新策略', '产品列表', '产品分类', '产品推荐、上下','创建策略', '获取策略列表', '删除策略', '编辑更新策略', '产品列表', '产品分类', '产品推荐、上下','创建策略', '获取策略列表', '删除策略', '编辑更新策略', '产品列表', '产品分类', '产品推荐、上下']
# # ll = json.dumps(l)
# # print(ll)
# # print(ll[0:5])
# # n = '{}'.format(l)
# action = '创建了{}接口'.format(l)
# # action = '创建了{}...]等接口'.format(n[0:32])
# # action = '创建了{}..等接口'.format('{}'.format(l)[0:32])
# # action = '修改{}接口'
#
# # print(action)
# # action = '创建了编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略编辑更新策略接口'
# if len(action) > 64:
#     action_names = '{0}'.format(action)
#     print(action[-28:])
#     action = '{0} .... {1}'.format(action[0:28], action[-28:])
#     print(action)
#     print('---l---', len(action))

# name = 'wen.ace.png'
import pytz

name = 'wefwefadfsd'
name = '.txt'
# name = None
l = name.split('.')
# print(len(l))
# print(l[0])
# print(l[0:-1])
# print(l[-1:])

# if len(l) == 1:
#     name = ''.join(l[0])
#     suffix = ''
# if len(l) > 1:
#     name = ''.join(l[0:-1])
#     suffix = l[-1]
#
# print('name:', name)
# print('suffix:', suffix)


# file_obj_name = 'plan'
# print('--wwww--', file_obj_name)
# file_obj_name = file_obj_name.split('.')
# print(file_obj_name)
# file_name = file_obj_name[0]
# suffix = file_obj_name[-1]
# if len(file_obj_name) > 2:
#     file_name = ''.join(file_name[0:-1])
#     suffix = file_name[-1]
# print('---', file_name)
# print('--222---', suffix)


# 发起任务
# http://10.0.99.136/API/project/23/envinfo

# 立即执行
# http://10.0.99.136/API/project/flow/task


# file_obj_name = file_obj.name.split('.')
# file_obj_obj_name = 'bug.txt'
# file_obj_name = file_obj_name.split('.')
# file_name = file_obj_name[0]
# suffix = ''
# if len(file_obj_name) > 1:
#     file_name = ''.join(file_obj_name[0:-1])
#     suffix = file_obj_name[-1]


# n = '创建1创建2;创建3创建4;;创建5创建6;'
# # n = '修改了<公文管理>项目信息'
# l = list(n.split(';'))
# print(l)
# if not all(l):
#     print('----')
#     l = [i for i in l if i]
#     print(l)


# data = {"nodes": [{"interfaces": [{"name": "1", "id": 12}, {"name": "\u767e\u5ea6", "id": 13}, {"name": "\u65b0\u589euser", "id": 14}, {"name": "deleteinterface", "id": 15}, {"name": "\u6d4b\u8bd5\u9000\u51fa", "id": 56}, {"name": "\u8bbe\u7f6e\u7528\u6237\u90ae\u7bb1", "id": 57}, {"name": "demo\u63a5\u53e3", "id": 63}, {"name": "\u53bb", "id": 65}, {"name": "\u65b0\u589euser", "id": 66}, {"name": "deleteinterface", "id": 67}, {"name": "\u521b\u5efa\u9879\u76ee", "id": 70}, {"name": "\u67e5\u770b\u9879\u76ee", "id": 71}], "zindex": 9, "id": "node1", "width": 100, "height": 200, "status": "", "name": "\u8282\u70b9\u4e00", "y": 200, "index": 0, "shape": "customNode", "x": 100}]}
# print(len('{}'.format(data)))
#
#
# if len('{0}'.format(data)) > 512:
#     try:
#         nodes = data["nodes"]
#         interfaces = ['...']
#         nodes[0]["interfaces"] = interfaces
#     except Exception:
#         data = {}
#     # else:
#     #     data = {"nodes": nodes}
# print('----nodes---', nodes)
# print('----data---', data)


# name = 'test.exe'
# file_obj_name = name.split('.')
# file_name = file_obj_name[0]
# suffix = ''
# if len(file_obj_name) > 1:
#     file_name = '.'.join(file_obj_name[0:-1])
#     suffix = file_obj_name[-1]
# print(suffix)

# def fn():
#     try:
#         id = 'ss'
#         s = id - 1
#     except Exception:
#         pass
#     else:
#
#         return s
#
# s = fn()
# print(s)


# import time
# import datetime
# import re
# #
# # utc 时间戳
# utc = time.mktime(time.gmtime())
# print(utc)


# def get_timestamp(days=None):
#     """获取时间戳"""
#     now_time = datetime.datetime.utcnow()                  # 伦敦时间
#     if days:
#         days = re.match(r'(\+|\-)?(\d+)$', days)
#         if days is None:
#             # 时间偏移参数输入有误
#             timestamp = None
#             return timestamp
#         add_or_cut = days.group(1)
#         num = days.group(2)
#         if add_or_cut == '-':
#             now_time = now_time - datetime.timedelta(days=int(num))
#         else:
#             now_time = now_time + datetime.timedelta(days=int(num))
#     array = time.strptime(now_time.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
#     # 格林时间戳，非本地时间
#     timestamp = time.mktime(array)
#     return timestamp


# s = get_timestamp(days=None)
# print('--s', s)
# utc = time.mktime(time.gmtime())
# print(utc)



# a = b = None
# if not all([a,b]):
#     print('====')

# import random
#
# s = random.randint(int(0),10)
# print(s)
# params = dict()
# # test_content = ['case_body_data': {"type": "String", "value": "sss", "key": "ss"}, {"editRow": ["key", "value", "type"], "value": "${{code}}", "type": "String", "key": "aa"}]
# test_content = [{"extract":[],"interface_id":914,"case_name":"测试接口22","case_params":[],"case_body_data":[{"type":"String","value":"sss","key":"ss"},{"key":"a","value":"${{code}}","type":"String","editRow":["key","value","type"]}],"case_header_info":[],"case_validate":[],"status":"enable","name":"测试接口22","id":914,"case_body_type":"x-formdata","nodeId":"94631a9d"}]
# test_content = test_content[0]
# for i in test_content.get('case_body_data', []):
#     params[i['key']] = i.get('value', '')
#     value = i.get('value', '')
#     print('===value==', value)
#
#
# print('--params--', params)
#
#
# def replace_common_parameter(param):
#     """公共参数替换
#     :param param 需要替换的参数；格式${{name}}
#     :return tb_common_parameter表中的value值； 不存在时返回原值
#     """
#     import re
#     try:
#         new_param = param.replace(' ', '').replace('\n', '').replace('\t', '')
#         re_match = re.match(r'\${{(.+)}}$', new_param)
#         if re_match is not None:
#             return param
#         match_param = re_match.group(1)
#         # 查库-公共参数表，存在则替换
#         from system.models import CommonParameterModel
#         common_parameter_obj = CommonParameterModel.objects.get(name=match_param)
#         param = common_parameter_obj.value
#         return param
#     except Exception as e:
#         print('公共参数获取失败: %s' % e)
#         return param
#
#
# if __name__ == '__main__':
#     ret = replace_common_parameter('${{''}}')
#     print('---ret---', ret)
#
#
#
#
#     import requests
#     requests.post()


js_data = {
	"info": {
		"_postman_id": "83251be2-5922-4359-a144-34c6259af0f4",
		"name": " 门户",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "测试退出22",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "crctoken",
						"value": "2123132132132131",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": ""
				},
				"url": {
					"raw": "http://10.0.99.102:8050/crcloud-account/loginout",
					"protocol": "http",
					"host": [
						"10",
						"0",
						"99",
						"102"
					],
					"port": "8050",
					"path": [
						"crcloud-account",
						"loginout"
					]
				}
			},
			"response": []
		},
		{
			"name": "设置用户邮箱22",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "crctoken",
						"value": "2132132132132132131",
						"type": "text"
					},
					{
						"key": "Content-Type",
						"name": "Content-Type",
						"value": "application/json",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\r\n  \"email\": \"3333@qq.cpm\",\r\n  \"emailCode\": \"323\"\r\n}"
				},
				"url": {
					"raw": "http://10.0.99.102:8050/crcloud-account/setUserEmail",
					"protocol": "http",
					"host": [
						"10",
						"0",
						"99",
						"102"
					],
					"port": "8050",
					"path": [
						"crcloud-account",
						"setUserEmail"
					]
				}
			},
			"response": []
		}
	]
}


# ret = json.dumps(js_data)
# print(ret.encode())
# print(type(ret.encode()))

from httprunner.api import HttpRunner
from httprunner import built_in


# 读取文件内容
# filePath = "D:\\upload\\postman_collection.json"
filePath = "./postman_collection.json"
# "file1": "${get_file($filePath)}"
def get_file(filePath):
    return open(filePath, "rb")

ret = get_file(filePath=filePath)

obj = HttpRunner()
# obj.run(path_or_tests='./demo_file.json', mapping={"file1": ret})
obj.run(path_or_tests='./demo_file.json')
ret = obj.summary
print('---报告结果---', ret)



# import requests
# requests.post()