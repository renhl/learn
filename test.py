# 迭代dict
d={'a':1,'b':2,'c':3}
# 默认迭代的是key
for k in d:
    print(k)
# 迭代value
for v in d.values():
    print(v)
# 同时迭代key和value
for k,v in d.items():
    print(k,v)
# 判断一个对象是否可迭代，通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('abc',Iterable)) #str是否可迭代
print(isinstance([1,2,3],Iterable)) #list是否可迭代
print(isinstance(123,Iterable))     #整数是否可迭代
# 生成器
L = (x*x for x in range(10))
for n in L:
    print(n)