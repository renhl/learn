#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-01-19 14:22
# @Author  : renhl
# @Site    : 
# @File    : getToken.py
# @Software: PyCharm Community Edition
import requests
import json
from addict import Dict									# 导入方便字典取值的库
def login():
	data ={"areaCode":"021",							# 需要传入的body
		   "areaName":"上海",
		   "client":"20",
		   "password":"146a",
		   "tchType":"2",
		   "username":"卡莉"}
	url = ""
	r = requests.post(url,data=data)
	d = r.json()
	print(r.status_code)              					 #  打印响应状态码
	#print(d)
	# print(r.encoding)               					 # 打印响应编码格式
	token = Dict(d).result.token                         # 获取token
	#return token
	print("token："+token)
	yunxintoken = Dict(d).result.yunXinToken             # 获取云信token
	print("yinxintoken:"+yunxintoken)
if __name__ == "__main__":								# 防止其他py重复调用方法
	login()