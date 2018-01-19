#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-01-19 18:09
# @Author  : renhl
# @Site    : 
# @File    : getCookie.py
# @Software: PyCharm Community Edition
import requests
import json
from addict import Dict									# 导入方便字典取值的库

payload = {"username":"tikuadmin","password":"123456","areaCode":"010"}
url = "http://xxx/ceshi_tiku/login"
r = requests.post(url,data=payload)
# print(r.text)
print(r.request.headers['Cookie'])						# 获取请求中headers中的cookie，注意request此处没有s
print(r.headers)										# 获取响应中的headers,若cookie在响应中，通过此方法获取
