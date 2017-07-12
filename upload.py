#coding = utf-8

from selenium import webdriver
# 引入keys包
# from selenium.webdriver.common.keys import Keys
import time
import win32gui
import win32con

driver = webdriver.Firefox()
driver.get("http://101.200.37.119/ceshi_tiku/user-login-page")
# driver.maximize_window()       #将浏览器最大化展示
#输入用户名密码
driver.find_element_by_xpath("html/body/div[1]/div/div/div/div/div[2]/form/div[1]/div/input").send_keys("teacher")
driver.find_element_by_xpath("html/body/div[1]/div/div/div/div/div[2]/form/div[2]/div/input").send_keys("123456")
time.sleep(1)
# 选择地区
# driver.find_element_by_id("areaCode")
driver.find_element_by_xpath(".//*[@id='areaCode']/option[text()='南京']").click()
time.sleep(1)
# 点击登录
driver.find_element_by_xpath("html/body/div[1]/div/div/div/div/div[2]/form/div[4]/div/button[1]").click()
time.sleep(1)
#点击上传文件
upload = driver.find_element_by_id("SWFUpload_0")
upload.click()
time.sleep(2)
# win32gui
dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 确定按钮Button

win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\PC\\Desktop\\1\\张欣1106日志.zip')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button