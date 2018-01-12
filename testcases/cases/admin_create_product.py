#!/usr/bin/env python
# @Author  : sally
import logging
import time
from selenium import webdriver
import unittest
import random

class admin_create_product(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass

    def test_create_product(self):
        logging.info("test_create_product start....")
        driver = self.driver
        url = self.base_url + "/ranzhi/www/sys/user-login.html"
        driver.get(url)
        # admin登陆
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        if driver.find_element_by_id('keepLogin1').is_selected():
            driver.find_element_by_id('keepLogin1').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)

        # 定位到客户管理
        driver.find_element_by_xpath('//*[@id="s-menu-1"]/button').click()
        time.sleep(2)
        driver.maximize_window()
        # print(driver.current_url)
        # second_url='http://localhost/ranzhi/www/crm/dashboard/'
        # driver.get(second_url)
        driver.switch_to_frame('iframe-1')
        driver.find_element_by_link_text('产品').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="menuActions"]/a').click()
        #添加产品
        driver.find_element_by_name('name').send_keys(random.randint(1000,99999))
        # driver.find_element_by_name('code').send_keys("{0}{1}".format(random.choices("abcdefghijklmnopqrstuvwxyz"),random.randint(1000,9999)))
        driver.find_element_by_id("code").send_keys("{0}{1}".format(random.choice('abcdefghjklqwertyuiomnbvcxz'), random.randint(1000, 9999)))
        time.sleep(3)
        driver.find_element_by_id('submit').click()


if __name__=="__main__":
    unittest.main