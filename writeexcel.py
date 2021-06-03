#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/11 16:06

#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/6/2 18:11

from selenium import webdriver
import random
import time

import os

while True:
	# chrome_options = Options()
	# chrome_options.add_argument('--headless')
	driver = webdriver.Chrome()
	driver.get("https://demoschool.talk-cloud.net/office/login.html#/login")
	driver.maximize_window()

	driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[1]/div/input').send_keys("15801336643")
	driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[2]/div/input').send_keys("zyh123456")
	driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/div/div[4]/button/span').click()
	time.sleep(4)
	driver.find_element_by_xpath('//*[@id="tabs"]/div/aside[1]/div/section/ul/li[2]/a/span[1]').click()
	time.sleep(2)
	fanme = driver.find_element_by_xpath('//*[@id="con_106"]/iframe')
	driver.switch_to.frame(fanme)
	time.sleep(2)
	upload = driver.find_element_by_xpath('//*[@id="toolbar"]/a[2]').click()#点击上传文件
	time.sleep(3)
	path = "f:/uploadfile.exe"
	# randoms = random.choice(path)
	os.system(path)
	time.sleep(10)
	driver.quit()