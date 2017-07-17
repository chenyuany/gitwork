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

sys.path.append("/testIsomp/testCase/user/")
from test_user import User
#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _icommon import frameElement,commonFun
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
sys.path.append("/testIsomp/testCase/department/")
from test_department import testDepartment
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage
import unittest

class testRoleSuite(unittest.TestCase):

	def setUp(self):
		#调用本地驱动
		self.browser = setDriver().set_local_driver()
		#调用远程驱动
		# self.browser = setDriver().set_remote_driver()

		self.testrole = testRole(self.browser)
		self.login = loginPage(self.browser)
		self.cmf = commonFun(self.browser)
		self.frameElem = frameElement(self.browser)
		self.user = User(self.browser)
		self.testdptment = testDepartment(self.browser)
		self.comsuit = CommonSuiteData(self.browser)

		#初始化用户登录
		self.comsuit.isomper_login()

		u'''添加角色'''
		self.testdptment.add_role()
		u'''添加用户'''
		self.testdptment.add_user()
		u'''用户赋予角色'''
		self.testdptment.user_add_role()
		self.login.quit()

		#使用添加的用户登录并切换至系统级角色
		self.comsuit.login_and_switch_to_sys()

		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"组织定义")

	def test_department(self):

		u'''添加和编辑部门'''
		self.testdptment.add_edit_department_001()
		u'''上移和下移部门'''
		self.testdptment.up_down_department_002()
		u'''上移和下移部门校验'''
		self.testdptment.up_down_department_check_003()
		u'''检验添加和编辑部门'''
		self.testdptment.check_add_edit_department_004()
		u'''删除部门'''
		self.testdptment.del_department_005()

		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"角色管理", u"角色定义")

		u'''全选删除角色'''
		self.testrole.bulkdel_role_007()

		#退出登录用初始化用户登录删除用户
		self.login.quit()
		self.comsuit.isomper_login()

		#删除用户
		self.user.del_all_user_008()
		self.login.quit()

	def tearDown(self):
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
