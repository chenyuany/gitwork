#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import *

#导入登录
sys.path.append("/testIsomp/testCase/")
from test_login import *

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        self.browser = initDriver().open_driver()
        
    def test_login(self):
        #登录
        testLogin().login_test(self.browser)
    
    def tearDown(self):
        initDriver().close_driver(self.browser)

#if __name__ == "__main__":
#    unittest.main()
