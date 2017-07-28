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
sys.path.append("/testIsomp/testCase/group/")
from test_rsgroup import testRegroup
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage
sys.path.append("/testIsomp/testCase/resource/")
from test_linux_resource import testLinuxResource

import unittest

class testDepartSuite(unittest.TestCase):

	def setUp(self):

		#调用驱动
		self.browser = setDriver().set_driver()

		self.testrole = testRole(self.browser)
		self.login = loginPage(self.browser)
		self.cmf = commonFun(self.browser)
		self.frameElem = frameElement(self.browser)
		self.user = User(self.browser)
		self.testdptment = testDepartment(self.browser)
		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.testregroup = testRegroup(self.browser)

		#初始化用户登录
		self.comsuit.isomper_login()

		u'''添加角色'''
		self.testdptment.add_role()
		u'''添加用户'''
		self.testdptment.add_user()
		u'''用户赋予角色'''
		self.testdptment.user_add_role()
		self.login.quit()
		#使用新添加的用户登录
		self.comsuit.use_new_user_login()
		#换至系统级角色
		self.cmf.select_role_by_text(u"系统管理员")
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"组织定义")
		u'''添加和编辑部门'''
		self.testdptment.add_edit_department_001()
		self.frameElem.switch_to_content()
		# 换至部门级角色
		self.cmf.select_role_by_text(u"部门管理员")

		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"资源")
		# 添加linux资源
		self.linuxresource.add_linux_resource_001()
		self.cmf.select_menu(u"运维管理", u"组织定义")

	def test_department(self):

		u'''添加和编辑资源组'''
		self.testregroup.add_edit_regroup_001()
		u'''上移和下移资源组'''
		self.testregroup.up_down_regroup_002()
		u'''上移和下移资源组校验'''
		self.testregroup.up_down_regroup_check_003()
		u'''检验添加和编辑资源组'''
		self.testregroup.check_add_edit_regroup_004()
		u'''资源组中添加资源'''
		self.testregroup.regroup_add_resource_001()
		u'''资源组中查询资源名称和IP'''
		self.testregroup.query_regroup_002()
		u'''资源组删除资源'''
		self.testregroup.regroup_del_resouce_003()
		u'''资源组全选删除资源'''
		self.testregroup.regroup_bulk_resouce_004()
		u'''删除资源组'''
		self.testregroup.del_regroup_005()

	def tearDown(self):

		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"资源")
		#全选删除资源
		self.linuxresource.bulkdel_resource_006()

		#换至系统级角色
		self.cmf.select_role_by_text(u"系统管理员")

		#切换到组织定义页面
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理", u"组织定义")

		u'''删除部门'''
		self.testdptment.del_department_005()

		#切换到角色定义页面
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
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()
