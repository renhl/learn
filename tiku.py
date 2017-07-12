#coding = utf-8

from selenium import webdriver
import time
import win32gui
import win32con
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("http://106.75.101.13:80/ceshi_tiku/user-login-page")
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
#输入配题名称
driver.find_element_by_id("paperName").send_keys("test123456")
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
win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, 'C:\\Users\\PC\\Desktop\\1\\1.zip')  # 往输入框输入绝对地址
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 按button
time.sleep(5)
#点击提交
driver.find_element_by_xpath(".//*[@id='from-question-import']/div[5]/input").click()
time.sleep(3)
#选择作业管理
driver.find_element_by_xpath(".//*[@id='exampaper-manager']/a").click()
time.sleep(3)
#点击修改
driver.find_element_by_xpath(".//*[@id='question-list']/table/tbody/tr[1]/td[8]/a[1]").click()
time.sleep(1)
# 选择年份为2017
driver.find_element_by_xpath(".//*[@id='teacher-select']/option[text()='2017']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='exampaper-term-select']/option[text()='春季班']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='exampaper-gradeType-select']/option[text()='小学部']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='exampaper-grade-select']/option[text()='小学三年级']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='exampaper-subject-select']/option[text()='数学']").click()
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='exampaper-classLevel-select']/option[text()='提高班(双师课堂)']").click()
time.sleep(1)


number=["2","3","4","5","6","7","8","9","10","11"]
n = 1
while n < 12:
    Select(driver.find_element_by_id("exampaper-classnum-select")).select_by_value(number[n])
    time.sleep(1)
    # 添加
    driver.find_element_by_xpath(".//*[@id='addClassButton']").click()
    time.sleep(1)
    n = n+1

# 确认修改
driver.find_element_by_xpath(".//*[@id='update-exampaper-btn']").click()
time.sleep(5)
# 上线
driver.find_element_by_xpath(".//*[@id='question-list']/table/tbody/tr[1]/td[8]/a[2]").click()
time.sleep(5)
driver.find_element_by_xpath(".//*[@id='classesconfirm']/div/div/div[3]/button").click()
driver.switch_to_alert().accept()         # js弹窗确认按钮
# driver.switch_to_alert().dismiss()        js弹窗取消按钮
time.sleep(10)
driver.quit()
