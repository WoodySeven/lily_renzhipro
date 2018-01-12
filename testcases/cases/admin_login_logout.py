import logging
from selenium import webdriver
import time
import unittest
from selenium.webdriver.support.select import Select
import ddt
from pro_renzhi.lib.utils import capture_screen

test_data = [['admin', '123456', '登陆成功'],
             ['invalid', '123456', '登录失败，请检查您的成员名或密码是否填写正确'],
             ['', '123456', '登录失败，请检查您的成员名或密码是否填写正确']]

@ddt.ddt
class admin_login_logout(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://localhost"
        driver=self.driver
        logging.info("打开浏览器成功")

    def tearDown(self):
        pass

    @ddt.unpack
    @ddt.data(*test_data)
    def test_admin_login_logout(self,admin,password,flag):
        logging.info("test_admin_login_test start....")
        driver = self.driver
        url=self.base_url+"/ranzhi/www/sys/user-login.html"
        driver.get(url)
        driver.find_element_by_name('account').clear()
        driver.find_element_by_name('account').send_keys(admin)
        driver.find_element_by_name('password').clear()
        driver.find_element_by_name('password').send_keys(password)
        # 怎么处理选择字体
        # front=driver.find_element_by_xpath('//*[@id="langs"]/button')
        # Select(front).select_by_value('zh-tw')
        time.sleep(2)
        if driver.find_element_by_id('keepLogin1').is_selected():
            driver.find_element_by_id('keepLogin1').click()
        driver.find_element_by_id('submit').click()
        time.sleep(3)
        self.assertIn(flag, driver.page_source)
        logging.info("test data is : {}, {}, {}".format(admin, password, flag))
        pic_path = capture_screen(driver)
        if pic_path is None:
            logging.error("截图不成功")
        else:
            logging.info(pic_path)
        logging.info("test_admin_login_test end....")





if __name__=="__main__":
    unittest.main()
