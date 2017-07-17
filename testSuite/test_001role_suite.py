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
from _icommon import commonFun
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
from test_mutex import testMutex
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage
sys.path.append("/testIsomp/testCase/department/")
from test_department import testDepartment
sys.path.append("/testIsomp/testCase/user/")
from test_user import User
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
import unittest

class testRoleSuite(unittest.TestCase):

	def setUp(self):

		#调用本地驱动
		self.browser = setDriver().set_local_driver()
		#调用远程驱动
		# self.browser = setDriver().set_remote_driver()

		self.testrole = testRole(self.browser)
		self.cmf = commonFun(self.browser)
		self.login = loginPage(self.browser)
		self.user = User(self.browser)
		self.testdptment = testDepartment(self.browser)
		self.comsuit = CommonSuiteData(self.browser)
		#初始化用户登录
		self.comsuit.isomper_login()

		u'''添加用户'''
		self.testdptment.add_user()

		#切换到角色定义页面
		self.cmf.select_menu(u"角色管理", u"角色定义")

	def test_role(self):

		self.testmutex = testMutex(self.browser)
		u'''添加系统级角色'''
		self.testrole.add_sysrole_001()
		u'''添加部门管理员'''
		self.testrole.add_dptrole_002()
		u'''编辑系统管理员'''
		self.testrole.edit_role_003()
		u'''角色查询'''
		self.testrole.role_query_008()
		u'''切换到角色互斥定义页面'''
		self.cmf.select_menu(u"角色管理", u"角色互斥定义")
		u'''添加互斥角色'''
		self.testmutex.add_mutex_role_001()
		u'''校验添加互斥角色后用户添加角色'''
		self.testmutex.check_addmutex_user_addrole_002()
		u'''校验添加互斥角色后用户编辑中的添加角色'''
		self.testmutex.check_addmutex_user_editrole_003()
		u'''编辑互斥角色'''
		self.testmutex.edit_mutex_role_004()
		u'''校验编辑互斥角色后用户添加角色'''
		self.testmutex.check_editmutex_user_addrole_005()
		u'''校验编辑互斥角色后用户编辑中的添加角色'''
		self.testmutex.check_editmutex_user_editrole_006()
		u'''删除角色互斥'''
		self.testmutex.del_mutex_role_007()
		u'''校验角色互斥'''
		self.testmutex.check_mutex_role_008()
		u'''编辑可管理角色'''
		self.testrole.edit_managerole_004()
		u'''校验其他权限选择'''
		self.testrole.check_other_role()
		u'''编辑其他权限'''
		self.testrole.edit_otherrole_005()
		u'''校验角色名称和没有选择菜单项'''
		self.testrole.check_rolename()
		u'''检验名称简写'''
		self.testrole.check_shortname()
		u'''校验批量删除'''
		self.testrole.check_bulkdel()
		u'''删除角色'''
		self.testrole.del_role_006()
		u'''全选删除角色'''
		self.testrole.bulkdel_role_007()
		self.cmf.select_menu(u"运维管理", u"用户")
		#用初始化用户登录删除用户
		self.user.del_all_user_008()
		#退出登录
		self.login.quit()

	def tearDown(self):
		initDriver().close_driver(self.browser)


if __name__ == "__main__":
	unittest.main()
