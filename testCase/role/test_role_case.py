#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/6/14
#模块描述：调用角色定义模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsomp/common")
from _icommon import commonFun,getElement
from _log import log
sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role

class testRoleCase(object):

	def __init__(self,driver):
		self.driver = driver
		self.log = log()

	#添加系统管理员
	def addsysrole_001(self):

		#日志开始记录
		self.log.log_start("addsysrole")

		#获取添加系统管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"add_sys_role")

		role=Role(self.driver)
		cmf = commonFun(self.driver)

		#保存成功的弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.add()
					role.add_rolename(data[2])
					role.add_shortname(data[3])
					role.select_sysrole()
					role.save_button()
					role.frameElem.switch_to_content()
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					role.back()
					#校验添加的角色是否存在
					if role.is_rolename_exsit(data[2]):
						print(u"角色已添加成功")
					flag = False
			except Exception as e:
				print u"添加系统管理员失败:" + str(e)
		self.log.log_end("addsysrole")

	#添加部门管理员
	def addroledpt_002(self):

		self.log.log_start("addroledpt")

		#获取添加部门管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"add_dpt_role")

		role=Role(self.driver)
		cmf = commonFun(self.driver)

		#保存成功的弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.add()
					role.add_rolename(data[2])
					role.add_shortname(data[3])
					role.level()
					role.select_dptrole()
					role.save_button()
					role.frameElem.switch_to_content()
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					role.back()
					#校验添加的角色是否存在
					if role.is_rolename_exsit(data[2]):
						print(u"角色已添加成功")
					flag = False
			except Exception as e:
				print u"添加部门管理员失败:" + str(e)
		self.log.log_end("addroledpt")

	#编辑系统管理员
	def editrole_003(self):

		self.log.log_start("editrole")

		#获取编辑系统管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"edit_role")

		role=Role(self.driver)
		cmf = commonFun(self.driver)

		#保存成功的弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.edit(data[2])
					role.add_rolename(data[3])
					role.add_shortname(data[4])
					role.save_button()
					role.frameElem.switch_to_content()
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					role.back()
					#校验编辑后的角色是否存在
					if role.is_rolename_exsit(data[3]):
						print(u"编辑角色成功")
					flag = False
			except Exception as e:
				print u"编辑系统管理员失败:" + str(e)
		self.log.log_end("editrole")

	#编辑可管理角色
	def editmanagerole_004(self):

		self.log.log_start("editmanagerole")

		#获取编辑系统管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"edit_mange_role")

		role = Role(self.driver)
		cmf = commonFun(self.driver)

		#右侧已选可管理角色框
		roleMsg="roles"

		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			#无检查点的测试项标识，如果为True说明通过
			flag = False
			try:

				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.edit(data[2])
					role.select_manage_role(int(data[3]))
					role.manage_role_add()
					flag = True
					role.test_check_point("id", roleMsg, data, flag)
					role.save_button()
					role.frameElem.switch_to_content()
					cmf.click_login_msg_button(1)
					role.back()
			except Exception as e:
				print u"编辑系统管理员失败:" + str(e)
		self.log.log_end("editmanagerole")

	#删除角色
	def delrole_006(self):
		self.log.log_start("delrole")

		#获取删除超级管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"del_role")

		role=Role(self.driver)
		cmf = commonFun(self.driver)

		#删除的弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.delete(data[2])
					flag = True
					role.frameElem.switch_to_content()
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					#校验删除后的角色是否存在
					if role.is_rolename_exsit(data[2]):
						print(u"超级管理员已删除")
					flag = False
			except Exception as e:
				print u"删除超级管理员失败:" + str(e)
		self.log.log_end("delrole")

	#全选删除角色
	def bulkdelrole_007(self):
		self.log.log_start("bulkdelrole")

		#获取删除超级管理员测试数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath,"bulk_delrole")

		role=Role(self.driver)
		cmf = commonFun(self.driver)

		#删除的弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.check_all()
					role.bulkdel()
					flag = True
					role.frameElem.switch_to_content()
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					flag = False
			except Exception as e:
				print u"全选删除角色失败:" + str(e)
		self.log.log_end("bulkdelrole")

	#校验角色名称和没有选择菜单项
	def checkrolename(self):

		self.log.log_start("checkrolename")
		#获取校验角色名称的数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath, "check_rolename")
		#实例化Role
		role=Role(self.driver)
		#实例化commonFun
		cmf = commonFun(self.driver)
		#弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		role.add()
		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.add_rolename(data[2])
					role.add_shortname(data[3])
					role.save_button()
					role.frameElem.switch_to_content()
					#设定没有检查点的测试项通过
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					role.frameElem.switch_to_main()
					#清空标识状态
					flag = False
			except Exception as e:
				print u"校验角色名称失败:" + str(e)
		role.back()
		self.log.log_end("checkrolename")

	#检验名称简写
	def checkshortname(self):

		self.log.log_start("checkshortname")
		#获取校验角色名称的数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath, "check_shortname")
		#实例化Role
		role=Role(self.driver)
		#实例化commonFun
		cmf = commonFun(self.driver)
		#弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.add()
					role.add_rolename(data[2])
					role.add_shortname(data[3])
					role.select_sysrole()
					role.save_button()
					role.frameElem.switch_to_content()
					#设定没有检查点的测试项通过
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					role.back()
					#清空标识状态
					flag = False
			except Exception as e:
				print u"校验名称简写失败:" + str(e)

		self.log.log_end("checkshortname")

	#其他权限选择
	def checkother(self):

		self.log.log_start("checkother")
		#获取其他权限选择的数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath, "ckeck_other")
		#实例化Role
		role=Role(self.driver)
		#实例化commonFun
		cmf = commonFun(self.driver)
		#弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.edit(data[2])
					role.other_role_add(int(data[3]))
					role.other_role_add(int(data[4]))
					role.frameElem.switch_to_content()
					#设定没有检查点的测试项通过
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					#清空标识状态
					flag = False
					role.back()
			except Exception as e:
				print u"其他权限选择失败:" + str(e)
		self.log.log_end("checkother")

	#校验批量删除
	def checkbulkdel(self):

		self.log.log_start("checkbulkdel")
		#获取校验角色名称的数据
		dataFile = dataFileName()
		roledfPath = dataFile.get_role_test_data_url()
		roledfData = dataFile.get_data(roledfPath, "check_bulk")
		#实例化Role
		role=Role(self.driver)
		#实例化commonFun
		cmf = commonFun(self.driver)
		#弹出框
		roleMsg="/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(roledfData)):
			#把单行的数据赋值给列表data
			data = roledfData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					role.bulkdel()
					role.frameElem.switch_to_content()
					#设定没有检查点的测试项通过
					flag = True
					cmf.test_win_check_point("xpath", roleMsg, data, flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print u"校验批量删除失败:" + str(e)
		self.log.log_end("checkbulkdel")


