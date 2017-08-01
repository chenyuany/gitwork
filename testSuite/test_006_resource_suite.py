#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/18
#模块描述：资源
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
sys.path.append("/testIsomp/testSuite/common_suite_file/")
from common_suite_file import setDriver,CommonSuiteData
sys.path.append("/testIsomp/testCase/resource/")
from test_linux_resource import testLinuxResource
from test_resource_accountmgr import testResourceAccount

class testResourceSuite(unittest.TestCase):

	def setUp(self):
		#调用驱动
		self.browser = setDriver().set_driver()

		self.comsuit = CommonSuiteData(self.browser)
		self.linuxresource = testLinuxResource(self.browser)
		self.account = testResourceAccount(self.browser)

		#资源前置条件
		self.comsuit.resource_module_prefix_condition()

	def test_resource(self):

		# 添加linux资源
		self.linuxresource.add_linux_resource_001()
		# 查询资源
		self.linuxresource.query_resource_002()
		#编辑linux资源
		self.linuxresource.edit_linux_resource_003()
		#添加和编辑linux资源账号
		self.account.add_edit_linux_resource_account_001()
		#查询资源账号
		self.account.query_resource_account_002()
		#校验资源账号
		self.account.check_linux_resource_account_003()
		#删除资源账号
		self.account.del_resource_account_004()
		#全选删除资源账号
		self.account.bulkdel_resource_account_005()
		#校验linux资源
		self.linuxresource.check_linux_resource_004()
		#删除资源
		self.linuxresource.del_resource_005()
		#全选删除资源
		self.linuxresource.bulkdel_resource_006()

	def tearDown(self):
		#资源后置条件
		self.comsuit.resource_module_post_condition()

		initDriver().close_driver(self.browser)

if __name__ == "__main__":
	unittest.main()