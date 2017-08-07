class Stu(object):
    __slots__ = ('name','score')    # 用tuple定义允许绑定的属性名称

class SubStu(Stu):              # 定义一个子类
    pass

s = Stu()                       # 创建一个实例
s.name = 'linda'                # 绑定属性name
s.score = 98                    # 绑定属性score
# s.age  = 23
try:                            # 捕获AttributeError异常并抛出
    s.age = 23
except AttributeError as e:
    print('AttributeError',e)

g = SubStu()                 # 创建子类的实例
g.age = 25                   # 动态创建属性age， __slots__ 限制属性对子类不起作用
print('年龄',g.age)