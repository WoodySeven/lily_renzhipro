#!/usr/bin/env python
# @Author  : sally
import logging
import time
from selenium import webdriver
import unittest
import random
from selenium.webdriver.support.select import Select


class admin_remember_add_del(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost"
        driver = self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass


    def test_remember_add_del(self):
        logging.info("test_remember_add_del start....")
        driver = self.driver
        url = self.base_url + "/ranzhi/www/sys/user-login.html"
        driver.get(url)
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        if driver.find_element_by_id('keepLogin1').is_selected():
            driver.find_element_by_id('keepLogin1').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)
        # 定位到后台管理
        driver.find_element_by_xpath('//*[@id="s-menu-superadmin"]/button').click()
        time.sleep(2)
        driver.maximize_window()
        driver.switch_to_frame('iframe-superadmin')
        driver.find_element_by_link_text('组织').click()
        time.sleep(3)
        #添加成员
        driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div[2]/a[1]').click()
        time.sleep(3)
        driver.find_element_by_name('account').send_keys("{0}{1}".format(random.choice("abcdefghijklmnopqrstuvwxyz"),random.randint(1000,9999)))
        time.sleep(1)
        driver.find_element_by_name('realname').send_keys(random.choice('abcdefghjklqwertyuiomnbvcxz'))
        driver.find_element_by_id('gender1').click()
        Select(driver.find_element_by_id('role')).select_by_value('hr')
        time.sleep(2)
        driver.find_element_by_id('password1').clear()
        driver.find_element_by_id('password1').send_keys('123456')
        driver.find_element_by_id('password2').send_keys('123456')
        driver.find_element_by_id('email').send_keys('{0}@qq.com'.format(random.randint(10000000,99999999)))
        time.sleep(2)
        driver.find_element_by_id('submit').click()
        time.sleep(5)
        # 删除成员
        # driver.find_element_by_link_text('组织').click()
        driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div/table/tbody/tr[2]/td[11]/a[3]').click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        time.sleep(3)






if __name__=="__main__":
    unittest.main