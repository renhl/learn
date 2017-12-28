class A:
    def add(self,a,b):
        return a+b
class B(A):
    def sub(self,a,b):
        return a-b
try:
    count = B()
    print(count.add(4,5))
    print(count.sub(4,5))
except NameError as msg:
    print(msg)
