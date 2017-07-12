# 直接传入匿名函数：
print(list(map(lambda x: x * x, [1, 2, 3, 4])))

# 把匿名函数赋值给一个变量，再利用变量来调用该函数：
f = lambda x: x * x
print(f(10))


# 把匿名函数作为返回值返回
def build(x,y):
    return lambda: x * x, y * y