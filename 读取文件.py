#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-28 17:18
# @Author  : renhl
# @Site    : 
# @File    : 读取文件.py
# @Software: PyCharm Community Edition
import time

opens = open("C://Users//PC//Desktop//1.txt",'r')    # 通过open方法，以读“r”的方式打开
print("文件名：",opens.name)
strs = opens.readlines()

try:
    for l in strs:
        print(l)
        time.sleep(1)
finally:
    opens.close()
    print("...")
