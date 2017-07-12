h = input('请输入身高：')
w = input('请输入体重：')
height = float(h)
weight = float(w)
BMI = weight/(height*height)
if BMI > 32:
    print('严重肥胖')
elif BMI >= 28:
    print('肥胖')
elif BMI >= 25:
    print('过重')
elif BMI >= 18.5:
    print('正常')
elif BMI < 18.5:
    print('过轻')