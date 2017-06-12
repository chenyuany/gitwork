#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
#导入登录
sys.path.append("/testIsomp/testCase/role/")
from test_role import *
import unittest

class testRoleSuite(unittest.TestCase):
	browers=initDriver().open_driver()
	testrolecase = testRoleCase(browers)