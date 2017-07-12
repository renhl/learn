from operator import itemgetter
# 通过sorted()函数进行list排序
print(sorted([1,3,-5,7]))
# 传入key函数，进行list绝对值排序
print(sorted([2,-4,5,-19],key = abs))
# 字符串进行排序，根据ASCII大小排序，'Z'<'a'
print(sorted(['acd','Ayt','Zoo','srr']))
# 忽略大小写进行排序
print(sorted(['acd','Ayt','Zoo','srr'],key = str.lower))
# 通过传入第三个函数反向排序
print(sorted(['acd','Ayt','Zoo','srr'],key = str.lower,reverse=True))

# 用一组tuple表示学生名字和成绩：
students = [('Bob', 75), ('Adam', 66), ('Bart', 66), ('Lisa', 88)]
# 按名字排序
print(sorted(students, key=itemgetter(0)))
# 按成绩排序，两种方法
# print(sorted(students, key=lambda t: t[1]))
print(sorted(students,key=itemgetter(1)))
# 先按名字排，再按成绩排序
print(sorted(students,key=itemgetter(0,1)))
# 按照成绩反向排序
print(sorted(students, key=itemgetter(1), reverse=True))

# 对字典排序
d = {'date1':3,'date4':2,'date2':5,'date3':4}
print(sorted(d.items(),key=itemgetter(1)))  # 按value进行排序
print(sorted(d.items(),key=itemgetter(0)))  # 按key进行排序