#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/07/07
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsomp/common")
from _icommon import commonFun,getElement,selectElement,frameElement,tableElement
from _log import log
sys.path.append("/testIsomp/webElement/role/")
from test_role_mutex import roleMutex
from test_roledf import Role
sys.path.append("/testIsomp/webElement/department/")
from dptmElement import Department
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole

class testDepartment(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.role = Role(driver)
		self.testrole = testRole(driver)
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.tableElem = tableElement(driver)
		self.frameElem = frameElement(driver)
		self.rolemutex = roleMutex(driver)
		self.dptment = Department(driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_dptmtable_data(self, sheetname):
		dataFile = dataFileName()
		dptmPath = dataFile.get_depart_test_data_url()
		dptmData = dataFile.get_data(dptmPath, sheetname)
		return dptmData

	u'''添加角色'''
	def add_role(self):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.getElem.find_element_wait_and_click("link", u"角色管理")
		self.getElem.find_element_wait_and_click("link", u"角色定义")
		self.testrole.add_sysrole_001()
		self.testrole.add_dptrole_002()

	u'''用户赋予角色'''
	def user_add_role(self):
		#获取用户赋予角色测试数据
		dptmData = self.get_dptmtable_data("user_add_role")
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.rolemutex.click_user_role(data[1])
					self.rolemutex.select_all_role(int(data[2]))
					self.rolemutex.click_add_role(int(data[2]))
					self.rolemutex.select_all_role(int(data[3]))
					self.rolemutex.click_add_role(int(data[3]))
					self.rolemutex.frameElem.switch_to_content()
					self.dptment.save_user_button()
					self.cmf.click_msg_button(1)
					self.cmf.back()
			except Exception as e:
				print ("add user_add_role fail:" + str(e))

	u'''添加部门'''
	def add_department_001(self):

		#日志开始记录
		self.log.log_start("add_department")
		#获取添加部门测试数据
		dptmData = self.get_dptmtable_data("add_department")
		#保存成功的弹出框
		dptmMsg = self.testrole.popup()
		self.dptment.click_left_department()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.dptment.popup_sendkey(data[4])
					self.dptment.click_ok_button()
					self.role.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
			except Exception as e:
				print ("add add_department fail:" + str(e))
		self.log.log_end("add_department")

	u'''编辑部门'''
	def edit_department_002(self):

		#日志开始记录
		self.log.log_start("edit_department")
		#获取编辑部门测试数据
		dptmData = self.get_dptmtable_data("edit_department")
		#保存成功的弹出框
		dptmMsg = self.testrole.popup()
		self.dptment.click_left_department()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.dptment.popup_sendkey(data[4])
					self.dptment.click_ok_button()
					self.role.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
			except Exception as e:
				print ("edit_department fail:" + str(e))
		self.log.log_end("edit_department")

	u'''上移部门'''
	def up_department_003(self):

		#日志开始记录
		self.log.log_start("up_department")
		#获取上移部门测试数据
		dptmData = self.get_dptmtable_data("up_department")
		self.dptment.click_left_department()
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.log.log_detail(data[0],True)
			except Exception as e:
				print ("up_department fail:" + str(e))

		self.log.log_end("up_department")

	u'''上移部门校验'''
	def up_department_check_005(self):

		#日志开始记录
		self.log.log_start("up_department_check")
		dptmMsg = self.testrole.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#获取上移部门测试数据
		dptmData = self.get_dptmtable_data("up_department")
		self.dptment.click_left_department()
		self.dptment.click_dept_switch()
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_up_button(data[2], int(data[3]))
					self.role.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
			except Exception as e:
				print ("up_department_check fail:" + str(e))
		self.log.log_end("up_department_check")

	u'''下移部门校验'''
	def down_department_check_006(self):

		#日志开始记录
		self.log.log_start("down_department_check")
		dptmMsg = self.testrole.popup()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		#获取上移部门测试数据
		dptmData = self.get_dptmtable_data("down_department")
		self.dptment.click_left_department()
		self.dptment.click_dept_switch()
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_up_button(data[2], int(data[3]))
					self.role.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
			except Exception as e:
				print ("down_department_check fail:" + str(e))
		self.log.log_end("down_department_check")

	u'''下移部门'''
	def down_department_004(self):

		#日志开始记录
		self.log.log_start("down_department")
		#获取下移部门测试数据
		dptmData = self.get_dptmtable_data("down_department")
		self.dptment.click_left_department()
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					self.log.log_detail(data[0],True)
			except Exception as e:
				print ("down_department fail:" + str(e))
		self.log.log_end("down_department")

	u'''删除部门'''
	def del_department_007(self):

		#日志开始记录
		self.log.log_start("del_department")
		#删除的弹出框
		dptmMsg = self.testrole.popup()
		#获取删除部门测试数据
		dptmData = self.get_dptmtable_data("del_department")
		self.dptment.click_left_department()
		flag = False
		self.dptment.click_dept_switch()
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_del_button(data[2])
					self.role.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath", dptmMsg, data, flag)
					self.role.frameElem.switch_to_content()
					self.cmf.click_msg_button(1)
			except Exception as e:
				print ("del_department fail:" + str(e))
		self.log.log_end("del_department")

	u'''检验添加部门'''
	def check_add_department_008(self):

		#日志开始记录
		self.log.log_start("check_add_department")
		#获取检验添加部门测试数据
		dptmData = self.get_dptmtable_data("check_add_department")
		#保存成功的弹出框
		dptmMsg = self.testrole.popup()
		self.dptment.click_left_department()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					if dataRow != 1:
						self.dptment.popup_sendkey(data[4])
					self.dptment.click_ok_button()
					self.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", dptmMsg, data, flag)
					self.driver.implicitly_wait(1)
					self.frameElem.switch_to_content()
					self.dptment.click_cancel_button()
			except Exception as e:
				print ("check_add_department fail:" + str(e))
		self.log.log_end("check_add_department")

	u'''校验编辑部门'''
	def check_edit_department_009(self):

		#日志开始记录
		self.log.log_start("check_edit_department")
		#获取编辑部门测试数据
		dptmData = self.get_dptmtable_data("check_edit_department")
		#保存成功的弹出框
		dptmMsg = self.testrole.popup()
		self.dptment.click_left_department()
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(dptmData)):
			data = dptmData[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.dptment.click_basic_operation(data[2], int(data[3]))
					if dataRow == 2:
						self.dptment.clear_depart_text()
					if dataRow != 2:
						self.dptment.popup_sendkey(data[4])
					self.dptment.click_ok_button()
					self.role.frameElem.switch_to_content()
					self.dptment.multil_div_check_point("xpath", dptmMsg, data, flag)
					self.driver.implicitly_wait(1)
					self.frameElem.switch_to_content()
					self.dptment.click_cancel_button()
			except Exception as e:
				print ("check_edit_department fail:" + str(e))
		self.log.log_end("check_edit_department")
