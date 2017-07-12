# python的循环有两种，一种是 for...in 循环，依次把list或tuple中的每个元素迭代出来。
#执行这段代码，会依次打印names的每一个元素
names = ['nacy','jack','zhangsan']
for name in names:
    print('你好：'+name)
#所以for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。
#计算1-10的整数之和，可用一个sum变量做累加：
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum = sum + x
    print(sum)
#计算1-100整数之和。可用 range()函数，可生成一个整数序列，通过list（）函数可以转化成list，range(5)生成序列从0开始小于5的整数
print (list(range(5)))
#range(101)就可以列出1-100间的整数,打印1-100间的整数之和
sum = 0
for x in range(101):
    sum = sum + x
    print(sum)
#第二种循环是while循环，只要条件满足就不断循环，计算100以内的所有奇数之和
sum = 0
n = 99
while n > 0:
    sum = sum +n
    n = n-2
    print(sum)