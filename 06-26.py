# import math
#
# def quadratic_equation(a, b, c):
#     t = math.sqrt(b*b-4*a*c)
#     return (-b + t) / (2 * a), (-b - t) / (2 * a)
# print(quadratic_equation(2, -3, 1))
# print(quadratic_equation(1, -6, 5))
def power(x,n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(2,3))


