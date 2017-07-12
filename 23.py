#coding = utf-8

from selenium import webdriver
import time
import win32gui
import win32con
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
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
driver.find_element_by_xpath(".//*[@id='exampaper-classLevel-select']/option[text()='尖子班(双师课堂)']").click()
time.sleep(1)

Select(driver.find_element_by_id('exampaper-classnum-select')).select_by_index(6)