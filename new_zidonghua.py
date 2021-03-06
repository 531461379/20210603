#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/9 8:59

import unittest
from selenium import webdriver
import time,os
import faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
fake = faker.Faker()

class Testcase(unittest.TestCase):

    def setUp(self):
        chrome_driver = r'E:/python/chromedriver'
        os.environ["webdriver.Chrome.driver"] = chrome_driver
        option = webdriver.ChromeOptions()
        option.add_experimental_option("detach", True)
        option.add_experimental_option("excludeSwitches",
                                       ['enable-automation'])  # 设置chrome浏览器的参数，使其不弹框提示（chrome正在受自动测试软件的控制）
        prefs = {'profile.default_content_setting_values.media_stream_camera': 1,
                 'profile.default_content_setting_values.media_stream_mic': 1,
                 'profile.default_content_setting_values.notifications': 1,
                 'profile.default_content_setting_values.geolocation': 1}
        # 设置chrome浏览器的参数，使其不弹框提示（是否保存密码）
        prefs["credentials_enable_service"] = False
        prefs["profile.password_manager_enabled"] = False
        option.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=option)
        self.base_url = "https://global.talk-cloud.net/1364152026/10032/1/0"
        self.driver.maximize_window()

    def tearDown(self):
        pass


    def test_enter_room(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_name("nickname").send_keys(fake.name())
        self.driver.find_element_by_id("roompwd").send_keys(1)
        self.driver.find_element_by_id('submit_btn').click()
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'start-detection'))).click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[2]/div[5]/button[2]').click() #检测视频
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[3]/div[4]/button[2]').click() #扬声器检测
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[4]/div[7]/button[2]').click()  # 扬声器检测
        self.driver.find_element_by_xpath('//*[@id="main_detection_device"]/div/div[6]/div/button[2]').click()
        time.sleep(5)
        # next = self.driver.find_element_by_xpath(
        #     '//*[@id="all_root"]/body/div[5]/div/div[3]/div[2]/div/div/div[3]/button').text
        # if next:
        #     self.assertEqual(next, "下一个")
        # else:
        #     begin = self.driver.find_element_by_xpath('//*[@id="room_classBegin"]').text
        #     self.assertEqual(begin, "上课")
        self.driver.execute_script('document.getElementsByClassName("Popover")[0].style.display="none";') #跳过帮助提示
        time.sleep(2)
        WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, 'room_classBegin'))).click()
        time.sleep(2)
        self.driver.execute_script('document.getElementsByClassName("popover-worp left")[0].style.display="none";')
        self.driver.find_element_by_xpath('//*[@id="header_container"]/article[2]/div[1]/div[3]/button').click()
        self.driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/div/div').send_keys("asfasfasf")
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="chatbox"]/div[2]/div[2]/button').click()


if __name__ == '__main__':
    unittest.main()


