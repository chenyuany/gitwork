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
from test_access_approval import testAccapproval

class testAccapprovalSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.cmf = commonFun(self.browser)
		self.accapproval = testAccapproval(self.browser)

		#资源前置条件
		self.comsuit.process_module_prefix_condition()

	def test_access_approval(self):
		# 添加访问审批
		self.accapproval.add_access_approvel_001()
		self.cmf.select_role_by_text(u"运维操作员")
		#访问审批通过流程控制拒绝审批
		self.accapproval.access_deny_approvel_002()
		self.comsuit.use_new_user_login()
		#访问审批通过流程控制同意审批
		self.accapproval.access_agree_approvel_003()
		self.comsuit.use_new_user_login()
		#紧急运维通过流程控制拒绝审批
		self.accapproval.urgent_deny_approvel_004()
		self.comsuit.use_new_user_login()
		#紧急运维通过流程控制同意审批
		self.accapproval.urgent_agree_approvel_005()

	def tearDown(self):
		#资源后置条件
		self.comsuit.process_module_post_condition()
		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()