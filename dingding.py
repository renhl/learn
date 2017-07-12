import os
import time
from selenium import webdriver
# 点home键KEYCODE_HOME
return_code=os.system('adb shell input keyevent 3')
print(return_code)
time.sleep(1)
#解锁屏幕
b = os.system('adb shell input swipe 403 478 687 340 ')
print(b)
time.sleep(1)
#按home键到首页
c=os.system('adb shell input keyevent 3')
print(c)
time.sleep(1)
#滑动屏幕
d = os.system('adb shell input swipe 802 385 445 455 ')
e = os.system('adb shell input swipe 802 385 445 455 ')
#打开钉钉
f =os.system('adb shell input tap 115 71')
#输入账号密码
g = os.system('adb shell input tap 139 230')
h = os.system('adb shell input tap 286 764')
i = os.system('adb shell input tap 196 752')
j = os.system('adb shell input tap 540 915')
k = os.system('adb shell input tap 474 842')
l = os.system('adb shell input tap 708 850')
m = os.system('adb shell input tap 126 990')
n = os.system('adb shell input tap 206 759')
o = os.system('adb shell input tap 382 768')
p = os.system('adb shell input tap 554 762')
q = os.system('adb shell input tap 316 298')
r = os.system('adb shell input tap 380 1002')
time.sleep(5)
x = os.system('adb shell input tap 336 331')
time.sleep(10)
y = os.system('adb shell input tap 354 282')
time.sleep(2)
aa =os.system('adb shell input keyevent 4')
dd = os.system('adb shell input tap 697 1003')
ee = os.system('adb shell input tap 67 670')
ff = os.system('adb shell input tap 350 450')
gg = os.system('adb shell input tap 510 558')
time.sleep(2)
bb =os.system('adb shell input keyevent 4')
#按home键到首页
cc=os.system('adb shell input keyevent 3')
#关闭屏幕
hh =os.system('adb shell input keyevent 26')
