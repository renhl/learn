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


#　　　多重继承


#生父
class Father():

    def func(self):
        print('生父打儿子')

#隔壁老王
class LaoWang():

    def func(self):
        print('老王打儿子')
    def func1(self):
        print('跟你妈说明天下午我会来')
#继父
class StepFather():

    def func(self):
        print('继父打儿子')
    def func1(self):
        print('我还会打你妈')

#神秘人
class Mysterious(Father,StepFather,LaoWang):         # 父类存在相同函数，按（）内顺序继承
    pass

##让我们看看到底谁打了儿子
s=Mysterious()
s.func()
s.func1()