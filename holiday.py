#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-01-15 14:21
# @Author  : renhl
# @Site    : 在工作日中执行某些方法
# @File    : holiday.py
# @Software: PyCharm Community Edition

#   工作日对应结果为 0, 休息日对应结果为 1, 节假日对应的结果为 2；
import datetime
import time
import json
import requests
import dingding

today = datetime.date.today()                  # 获取当前日期
#print(today)
date = str(today).replace('-','')              #将日期中的-去掉
print(date)

url = "http://api.goseek.cn/Tools/holiday?date="
r = requests.get(url+date)                     # 调用URL并填入date
a =r.json()                                    # 返回结果以json显示

print(a['data'])                              # 打印返回值中key为'data'的value

if a['data'] == 0:                            # 如果value==0，调用dingding.py中的dd()方法
    dingding.dd()
    print("完成")
else:
    print("今天休息")