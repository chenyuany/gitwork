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
import unittest
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _icommon import commonFun
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
sys.path.append("/testIsomp/testCase/process/")
from test_double_license import testDobapproval

class testAccapprovalSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.cmf = commonFun(self.browser)
		self.double = testDobapproval(self.browser)

		self.comsuit.login_and_switch_to_dep()
		self.comsuit.switch_to_moudle(u'运维管理', u'授权')

		#资源前置条件
		# self.comsuit.process_module_prefix_condition()

	def test_access_approval(self):
		# 添加双人授权
		self.double.add_double_license_001()
		self.cmf.select_role_by_text(u"运维操作员")
		self.double.same_termina_approvel_002()
		self.comsuit.use_new_user_login()
		self.double.termina_deny_approvel_003()

	def tearDown(self):
		#资源后置条件
		# self.comsuit.process_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()