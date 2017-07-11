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
from _globalVal import globalValue
from _icommon import getElement,selectElement,frameElement,commonFun
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
from test_mutex import testMutex
sys.path.append("/testIsomp/testCase/department/")
from test_department import testDepartment
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage
import unittest

class testRoleSuite(unittest.TestCase):
	def setUp(self):
		# self.browser = initDriver().open_driver()
		driver_lists = globalValue().get_value()
		self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])

	def test_department(self):
		self.getElem = getElement(self.browser)
		self.cmf = commonFun(self.browser)
		self.selectElem = selectElement(self.browser)
		self.frameElem = frameElement(self.browser)
		self.testrole = testRole(self.browser)
		self.login = loginPage(self.browser)
		self.testdptment = testDepartment(self.browser)
		login_data = self.testrole.get_table_data("login")
		data = login_data[1]
		self.login.login(data)
		u'''添加角色'''
		self.testdptment.add_role()
		u'''用户赋予角色'''
		self.testdptment.user_add_role()
		self.login.quit()
		dptlogin_data = self.testdptment.get_dptmtable_data("deptmetn_login")
		dptdata = dptlogin_data[1]
		self.login.login(dptdata)
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.cmf.select_role(1)
		self.getElem.find_element_wait_and_click_EC("link", u"运维管理")
		self.getElem.find_element_wait_and_click_EC("link", u"组织定义")
		u'''添加部门'''
		self.testdptment.add_department_001()
		u'''编辑部门'''
		self.testdptment.edit_department_002()
		u'''上移部门'''
		self.testdptment.up_department_003()
		u'''下移部门'''
		self.testdptment.down_department_004()
		u'''上移部门校验'''
		self.testdptment.up_department_check_005()
		u'''下移部门校验'''
		self.testdptment.down_department_check_006()
		u'''检验添加部门'''
		self.testdptment.check_add_department_008()
		u'''校验编辑部门'''
		self.testdptment.check_edit_department_009()
		u'''删除部门'''
		self.testdptment.del_department_007()
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.getElem.find_element_wait_and_click_EC("link", u"角色管理")
		self.getElem.find_element_wait_and_click_EC("link", u"角色定义")
		u'''全选删除角色'''
		self.testrole.bulkdel_role_007()

	def tearDown(self):
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
