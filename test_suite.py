#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
import HTMLTestRunner
import time
import os

sys.path.append("/testIsomp/common/")
from _mail import *

class testSuite(unittest.TestCase):
    u'''运行所有测试用例集'''
    if __name__ == "__main__":
        timeFormat = '%Y-%m-%d %X'
        isTitle = time.strftime(timeFormat, time.localtime())
        
        #定义测试报告的输出页面
        reportFile = "d:/testIsomp/report/testReport.html"
        rf = file(reportFile,'wb')
        
        loader = unittest.TestLoader()
        suite = unittest.TestSuite()
        
        dir = "/testIsomp/testSuite"
        package_tests = loader.discover(start_dir=dir,pattern='test*.py')
        suite.addTests(package_tests)

        runner = HTMLTestRunner.HTMLTestRunner(stream=rf,title=isTitle,description="Report_description")
        runner.run(suite)
        
        #直接跑测试用例
        #unittest.TextTestRunner().run(suite)
        #sendMail().send_mail()

