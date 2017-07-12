# 函数作为返回值，用于不立刻使用函数，使用时调用即可
def lazy_sum(*args):       # 定义一个函数
    def sum():
        ax = 0
        for n in args:
            ax = n + ax
        return ax
    return sum            # 返回函数sum()
L=lazy_sum(1,3,7,8,6)     # 将函数赋值
print(L())                # 调用函数作为返回值
# 每次调用lazy_sum()时，都会返回一个新的函数，即使传入相同的值
L1 = lazy_sum(1,2,3,4)
L2 = lazy_sum(1,2,3,4)
print(L1==L2)

# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())