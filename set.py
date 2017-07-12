#set和dict类似，也是一组key的集合，但不储存value。由于key不能重复，所以，在set中，没有重复的key
#要创建一个set，需要提供一个list作为输入集合：
s = set([1,2,3])
print(s)
s.add(4)
print(s)
#可通过add(key)的方法添加元素到set中，可以重复添加，但是无效果
s.add(2)
print(s)
#通过remove的方法可以删除元素：
s.remove(4)
print(s)
#set可以看做数学上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
s1 = set([8,9,0,7])
s2 = set([8,9,1,2])
print(s1 & s2)
print(s1 | s2)
