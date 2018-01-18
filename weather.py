#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-01-17 14:14
# @Author  : renhl
# @Site    : 
# @File    : weather.py
# @Software: PyCharm Community Edition

import requests
import json
from addict import Dict                       # 导入解析json的开源库
def weather():
    r=requests.get("https://free-api.heweather.com/s6/weather/forecast?location=北京&key=4e6ea60db7634f3ba31616c733500301")
   # print(r.text)                            # 打印接口返回内容
    a=r.json()
    # dictionary=Dict(a)
    f = Dict(a).HeWeather6[0].daily_forecast[0].date
    print("当前日期为："+f)
    b=Dict(a).HeWeather6[0].basic.location
    print("地区："+b)
    # c=Dict(a).HeWeather6[0].update.utc
    # print(c)
    d=Dict(a).HeWeather6[0].daily_forecast[0].tmp_min
    print("最低气温："+d)
weather()