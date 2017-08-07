# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print("%s:%s" % (self.name, self.score))
#
# bart = Student('zhangsan', 98)
#
# print(bart.print_score())
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

print('bart.name =', bart.name)
print('bart.score =', bart.score)
bart.print_score()
lisa.print_score()

print('grade of Bart:', bart.get_grade())
print('grade of Lisa:', lisa.get_grade())

class Animal(object):
    def run(self):
        print("Animal is running")
class Dog(Animal):
# 当子类和父类都存在相同的run()方法时，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
    def run(self):
        print("dog is running")
    def eat(self):
        print("dog eating")
class Cat(Animal):
    pass
dog = Dog()
cat = Cat()

dog.run()
dog.eat()
cat.run()
print(isinstance(dog,Dog))   # 判断变量dog是否为Dog类型
print(isinstance(dog,Animal)) # 因Dog()从Animal()继承下来。

def run_twice(Animal):  # 多态 编写一个函数，这个函数接受一个Animal类型的变量
    Animal.run()
    Animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())

print(type(dog))      # 变量的类型

# 实例属性和类属性
class Student(object):
    name = "xxx"         # 定义类属性
rex = Student()          # 创建实例rex
print(rex.name)          # 打印name属性，因为实例中没有name属性，会继续查找class的name属性
print(Student.name)      # 打印类的name属性
rex.name = "123"         # 给实例绑定name属性
print(rex.name)          # 实例的属性优先级高于类的属性
print(Student.name)      # 打印类的name属性

del rex.name             # 删除实例的属性
print(rex.name)          # 再次调用实例属性时，未找到就会显示类的属性