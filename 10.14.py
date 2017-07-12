def my_avg(L):
    sum = 0
    for x in L:
        sum = sum + x*x
        avg = sum/len(L)
    return avg
print(my_avg([1,2]))