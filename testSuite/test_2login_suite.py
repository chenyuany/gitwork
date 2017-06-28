#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import *
from _globalVal import globalValue

#导入登录
sys.path.append("/testIsomp/testCase/login")
from test_login import *



import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        driver_lists = globalValue().get_value()
        self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        
#        self.browser = initDriver().open_driver()
        
    def test_login(self):
        test_login = testLogin(self.browser)
        #登录
        test_login.login()
    
    def tearDown(self):
        initDriver().close_driver(self.browser)

#if __name__ == "__main__":
#    unittest.main()
