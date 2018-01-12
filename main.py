import logging
import traceback
import unittest
import time
from testcases.cases.admin_login_logout import admin_login_logout
from testcases.cases.admin_create_product import admin_create_product
from testcases.cases.admin_create_customer import admin_create_customer
from testcases.cases.admin_create_order import admin_create_order
from testcases.cases.admin_remember_add_del import admin_remember_add_del
from testcases.cases.admin_cashier_account import admin_cashier_account

from pro_renzhi.lib import HTMLTestRunner

if __name__ == '__main__':
    logger = logging.Logger('./log/logger.log', logging.INFO)
    logging.info("本次测试开始执行，以下是详细日志")
    try:
        suite = unittest.TestSuite()     # 新建一个suite，测试套件
        loader = unittest.TestLoader()   # 新建一个加载器，自定义的方式把测试用例加载到suite里
        suite.addTest(loader.loadTestsFromTestCase(admin_login_logout))
        # suite.addTests(loader.loadTestsFromTestCase(admin_create_order))  # 把测试类所有的方法都加载到suite里
        # suite.addTest(loader.loadTestsFromTestCase(admin_create_product))
        # suite.addTest(loader.loadTestsFromTestCase(admin_remember_add_del))
        # suite.addTest(loader.loadTestsFromTestCase(admin_cashier_account))
        # suite.addTest(loader.loadTestsFromTestCase(admin_create_customer))
        # unittest.TextTestRunner(verbosity=2).run(suite) # unittest运行suite
        fp = open('reports/report_renzhi_{0}.html'.format(time.strftime("%Y-%m-%d %H-%M-%S")), 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title='renzhi测试报告',
            description='renzhi的所有测试用例执行细节'
        )
        runner.run(suite)
        logging.info("测试顺利结束^_^ ")
    except Exception:
        """print_exc() 把异常输出到屏幕上，而format_exc() 把异常返回成字符串"""
        traceback.print_exc()
        logging.error(traceback.format_exc())
        logging.error("测试异常终止")
    finally:
        if fp is not None:
            fp.close()



