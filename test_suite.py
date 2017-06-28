#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
import HTMLTestRunner
import time
import os

sys.path.append("/testIsomp/common/")
from _mail import sendMail
from _transCoding import jsonTranscoding
from _initDriver import initDriver
from _globalVal import globalValue


class testSuite(unittest.TestCase):
    u'''运行所有测试用例集'''
    if __name__ == "__main__":
        lists = jsonTranscoding().set_brower()
        
        timeFormat = '%Y-%m-%d %X'
        isTitle = time.strftime(timeFormat, time.localtime())
    for index in range(len(lists)):
        host_url = lists.keys()[index] 
#        print host_url
        brower_type = lists.values()[index]
        globalValue().set_value(host_url,brower_type)
#        print brower_type

        #定义测试报告的输出页面
        reportFile = "/testIsomp/report/" + str(brower_type.strip()) + "testReport.html"
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
        # sendMail().send_mail()

