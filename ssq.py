#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018-01-02 18:20
# @Author  : renhl
# @Site    : 
# @File    : ssq.py
# @Software: PyCharm Community Edition
import random

h = random.sample(range(1,34),6)  # 随机生成1-33的list，取出6个元素
h.sort()                          # 将list排序
l = random.sample(range(1,17),1)

h1 = str(h)[1:len(str(h))-1]     # 将list中的元素依次放入h1中
l1 = str(l)[1:len(str(l))-1]

print("红球：",h1,"蓝球:",l1)