#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time:2020/5/14 10:58

import unittest
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from pynput.mouse import Button, Controller
import time,os
from randoms import RandomStr,str_five,int_eleven,int_four
from lxml import etree

class Testcace(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.login_url = 'https://demo.talk-cloud.net/144827535/109132/0/2'
		self.url = 'https://doccdn.talk-cloud.net/static/h5_new_3.3.10.3/index.html#/login'
		self.driver.get("http://demo.talk-cloud.net/User/login.html")
		self.driver.maximize_window()

	def tearDown(self):
		# self.driver.quit()
		pass


	def test_login(self,domain="jszc1",username="admin",password="123456"):
		'''
			登陆后台
		'''
		driver = self.driver
		driver.find_element_by_name("companydomain").send_keys("jszc1")
		driver.find_element_by_name("name").send_keys("admin")
		driver.find_element_by_name("password").send_keys("123456")
		login = driver.find_element_by_id('login_btn').text
		driver.find_element_by_id('login_btn').click()
		self.assertEqual("登录",login)
	#
	# def test_createserial(self):
	# 	'''
	# 	 创建房间
	# 	'''
	# 	driver = self.driver
	# 	self.test_login()
	# 	driver.find_element_by_id('add_room').click()
	# 	driver.find_element_by_id('roomname').send_keys(str_five)
	# 	time.sleep(1)
	# 	driver.find_element_by_id('passwordinfo_').click()
	# 	time.sleep(1)
	# 	driver.find_element_by_xpath('//*[@id="end_date"]').send_keys(time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(time.time()+24*3600)))
	# 	time.sleep(2)
	# 	submit = driver.find_element_by_id("submit_save")
	# 	name = submit.get_attribute('value')
	# 	submit.click()
	# 	self.assertEqual("保存",name)

	def test_enter_serial(self):
		'''进入房间'''
		driver = self.driver
		self.test_login()
		driver.find_element_by_xpath('//*[@id="form1"]/div/table/tbody/tr[1]/td[6]/a[1]').click()
		text = driver.find_element_by_xpath('//*[@id="urllabel2"]').text #打印出来的是教室连接,https://demo.talk-cloud.net/1473061506/10756/0/2
		self.driver.get(text) #请求教室连接
		driver.find_element_by_id('nickname').send_keys(str_five) #输入教室昵称
		driver.find_element_by_id('submit_btn').click() #点击进入教室
		mouse = Controller()
		mouse.position = (309, 173)
		mouse.press(Button.left)
		mouse.release(Button.left)
		# time.sleep(3)
		driver.find_element_by_xpath('//*[@id="start-detection"]').click() #开始检测
		driver.find_element_by_xpath('//*[@id="tk_app"]/div/div[2]/div[1]/div[2]/div[3]/span[2]').click()#声音检测前小提示
		time.sleep(1)
		driver.execute_script("""$("div.device_content button:contains('下一步')").removeClass("disabled")""") #声音检测
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div/div[3]/div[2]/button').click()
		time.sleep(1)
		shexiangtou = driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[1]/span').text
		if shexiangtou == "选择摄像头":
			driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[3]/div[2]/button[2]').click()  # 摄像头下一步
		else:
			driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[3]/div[2]/button[1]').click() #摄像头上一步
		time.sleep(1)
		maikefeng = driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[4]/div[2]/button[2]').text
		driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[4]/div[2]/button[2]').click() #麦克风检测
		if maikefeng == "下一步":
			driver.find_element_by_xpath('//*[@id="main_detection_device"]/div[2]/div[3]/div[2]/button[2]').click()
			qingzhijinru = driver.find_element_by_xpath('//*[@id="tk_app"]/div/div[2]/div[2]/div[2]/div[2]').text #系统强制进入提示
			if qingzhijinru == "系统测试结果" :
				driver.find_element_by_xpath('//*[@id="tk_app"]/div/div[2]/div[2]/div[2]/div[4]/button[2]').click() #进入
			else:
				driver.find_element_by_xpath('//*[@id="tk_app"]/div/div[2]/div[2]/div[2]/div[4]/button[1]').click() #取消
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="header_right"]/div[1]/div[3]/button').click() #学生消息
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/div/div').send_keys("学生发送消息")
		time.sleep(2)
		driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/button').click()
		time.sleep(50)
	# def test_fiel_add(self):
	# 	driver = self.driver
	# 	self.test_login()
	# 	file_admin = driver.find_element_by_xpath('/html/body/div[1]/div/aside/ul/a[2]/li/div[2]')
	# 	file_admin.click()
	# 	first = driver.find_element_by_id('adddocument').click()
	# 	first1 = WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("filedata")).send_keys("E:/file/fff.txt")
	# 	first2 = driver.find_element_by_id('btnupload').click()
	# 	file_dir = os.getcwd()












