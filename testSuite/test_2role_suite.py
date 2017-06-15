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
from _icommon import getElement,selectElement,frameElement,commonFun
#导入登录
sys.path.append("/testIsomp/testCase/role/")
from test_role_case import testRoleCase
import unittest

class testRoleSuite(unittest.TestCase):

	def setUp(self):
		self.browser = initDriver().open_driver()

	def test_role(self):
		role_case = testRoleCase(self.browser)
		role_case.addsysrole()

	def tearDown(self):
		initDriver().close_driver(self.browser)

if __name__ == "__main__" :
	driver=testRoleSuite.setUp()
	getElem = getElement(driver)
	selectElem = selectElement(driver)
	frameElem = frameElement(driver)
	common=commonFun(driver)
	a = getElem.find_element_with_wait("id","loginMethod")
	selectElem.select_element_by_index(a,0)
	getElem.find_element_wait_and_sendkeys("id","username","a")
	getElem.find_element_wait_and_sendkeys("id","pwd","1")
	getElem.find_element_wait_and_click("id","do_login",5)
	frameElem.switch_to_top()
	common.select_role(1)
	getElem.find_element_wait_and_click("link",u"角色管理")
	getElem.find_element_wait_and_click("link",u"角色定义")
	testRoleSuite.test_role()
	testRoleSuite.tearDown()