#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：
#生成日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

#导入通用方法类
sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

#导入文件操作类
sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

#导入用户元素类
sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

class User():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.user = UserPage(driver)
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
#		self.login = loginPage(self.driver)
		self.frameElem = frameElement(self.driver)
		self.tableEle = tableElement(self.driver)

	#提示框元素路径
	def user_msg(self):
		user_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return user_msg

	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_person_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData	

	u'''添加用户'''
	def add_user_001(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("addUser")
		#获取添加用户的数据
		user_data = self.get_table_data("add_user")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.add_button()
					self.user.set_user_account(data[2])
					self.user.set_user_name(data[3])
#					self.user.set_user_status(data[7])
					self.user.set_user_pwd(data[8])
					self.user.set_user_enquire_pwd(data[9])
					self.user.click_role_msg()
					self.user.set_user_role(data[15])
					self.user.click_role_add_button()                
					self.user.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					#清空标识状态
					flag = False
					self.user.click_back_button()
					if self.cmf.is_namevalue_exsit(data[2],"fortUserAccount"):
						print ("add user success")
			except Exception as e:
				print ("user add fail: ") + str(e)
		self.log.log_end("addUser")

	u'''编辑用户'''
	def edit_user_002(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("editUser")
		#获取编辑用户的数据
		user_data = self.get_table_data("mod_user")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_edit(data[2])
#					self.user.add_button()
					self.user.set_user_account(data[3])
					self.user.set_user_name(data[4])
					self.user.set_dep(data[7])
					self.user.set_user_status(data[8])
					self.user.set_user_pwd(data[9])
					self.user.set_user_enquire_pwd(data[10])
#					self.user.click_role_msg()
#					self.user.set_user_role(data[15])
#					self.user.click_role_add_button()                 
					self.user.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					#清空标识状态
					flag = False
					self.user.click_back_button()
					self.cmf.back()
					if self.cmf.is_namevalue_exsit(data[2],"fortUserAccount"):
						print ("edit user success")
			except Exception as e:
				print ("edit user fail: ") + str(e)
		self.log.log_end("editUser")	

	u'''生成证书'''
	def create_user_cert_003(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("CreateUserCert")
		#获取生成证书用户的数据
		user_data = self.get_table_data("create_cert")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_cert(data[3])
					self.user.create_cert()
#					if self.getElem.find_element_wait_and_compare_text('id','downLoad',data[1],10):
					if self.user.get_cert() == data[2]:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)						
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
#					self.cmf.back()
			except Exception as e:
				print ("Create user cert fail: ") + str(e)
		self.log.log_end("CreateUserCert")

	u'''重新生成证书'''
	def create_user_cert_again_003(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("ReCreateUserCert")
		#获取重新生成证书的数据
		user_data = self.get_table_data("reCreate_cert")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
#					self.user.operate_cert(data[2])
					cert_text_old = self.user.get_cert_serial_num()
					self.user.create_cert()
					self.cmf.click_login_msg_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					cert_text_new = self.user.get_cert_serial_num()
#					if self.getElem.find_element_wait_and_compare_text('id','downLoad',data[1],10):
					if cert_text_old != cert_text_new:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)						
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
#					self.cmf.back()
			except Exception as e:
				print ("ReCreate user cert fail: ") + str(e)
		self.log.log_end("ReCreateUserCert")

	u'''删除证书'''
	def delete_user_cert_004(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("DeleteUserCert")
		#获取删除证书的数据
		user_data = self.get_table_data("delete_cert")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
#					self.user.operate_cert(data[3])
					self.user.delete_cert()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					if self.user.get_init_cert_name() == data[2]:
						print ("Delete cert success!")						
					#清空标识状态
					flag = False
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.cmf.back()
			except Exception as e:
				print ("Delete user cert fail: ") + str(e)
		self.log.log_end("DeleteUserCert")



	

	u'''校验用户'''
	def checkout_user_005(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("checkoutUser")
		#获取用户校验的数据
		user_data = self.get_table_data("user_check")#user_check
		#无检查点的测试项标识，如果为True说明通过
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.user.add_button()		
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
#					self.user.add_button()
					self.user.set_user_account(data[2])
					self.user.set_user_name(data[3])
					if dataRow == range(len(user_data))[-1]:
						self.user.clear_dep()				
#					self.user.set_user_status(data[7])
					self.user.set_user_pwd(data[7])
					self.user.set_user_enquire_pwd(data[8])
					self.user.set_user_mobile(data[9])
					self.user.set_user_phone(data[10])
					self.user.set_user_email(data[11])            
					self.user.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					#清空标识状态
					flag = False
			except Exception as e:
				print ("checkoutUser fail: ") + str(e)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.user.click_back_button()
		self.log.log_end("checkoutUser")

	u'''检索条件:用户状态'''
	def search_user_by_status_006(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("Search user by status")
		#获取按照用户状态检索的数据
		user_data = self.get_table_data("search_by_status")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.search_by_user_status(data[2])
					self.user.click_search_button()
					self.user.page_select_all()
					search_row = self.user.get_rows()
					row = self.user.search_by_status(data[3])#switch_on
					#清空标识状态
					if row == search_row:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)
					flag = False			
			except Exception as e:
				print ("search user by status fail: ") + str(e)
		self.user.click_reset_button()
		self.log.log_end("Search user by status")

	u'''检索条件:账号或者名称'''
	def search_user_by_username_006(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("Search user by username")
		#获取按照账号或名称检索的数据
		user_data = self.get_table_data("search_by_name")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.search_accountorname(data[3])
					self.user.click_search_button()
					self.user.page_select_all()
					search_row = self.user.get_rows()
					row = self.user.search_direct_by_account_or_name(data[3])
					if row == search_row:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)
					#清空标识状态
					flag = False			
			except Exception as e:
				print ("search user by username fail: ") + str(e)
		self.user.click_reset_button()
		self.log.log_end("Search user by username")
	

	u'''检索条件:部门'''
	def search_user_by_dep_006(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("Search user by department")
		#获取按部门检索的数据
		user_data = self.get_table_data("search_by_dep")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.set_dep(data[3])
					self.user.click_search_button()
					self.user.page_select_all()
					search_row = self.user.get_rows()
					row = self.user.search_direct_by_dep(data[3])#switch_on
					if row == search_row:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)
					#清空标识状态
					flag = False		
			except Exception as e:
				print ("search user by department fail: ") + str(e)
		self.user.click_reset_button()
		self.log.log_end("Search user by department")

	u'''检索条件:角色'''
	def search_user_by_role_006(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("SearchUserByRole")
		#获取按角色检索的数据
		user_data = self.get_table_data("search_by_role")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.search_user_role(data[3])
#					row = self.user.search_by_user_status(data[2])
					self.user.click_search_button()
					self.user.page_select_all()
					search_row = self.user.get_rows()
					row = self.user.search_direct_by_role(data[3])#switch_on
					if row == search_row:
						self.cmf.test_win_check_point("","",data,True)
					else:
						self.cmf.test_win_check_point("","",data,False)
					#清空标识状态
					flag = False		
			except Exception as e:
				print ("search user by role fail: ") + str(e)
		self.user.click_reset_button()
		self.user.click_search_button()
		self.log.log_end("SearchUserByRole")
	

	u'''删除单个用户'''
	def del_user_007(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("DelOneUser")
		#获取删除用户（单个）的数据
		user_data = self.get_table_data("del_user")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.operate_delete(data[2])
					self.cmf.click_login_msg_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					#清空标识状态
					flag = False
					if not self.cmf.is_namevalue_exsit(data[2],"fortUserAccount"):
						print ("del user success")					
			except Exception as e:
				print ("DelOneUser fail: ") + str(e)
		self.log.log_end("DelOneUser")
	
	

	u'''删除一页全部用户'''
	def del_all_user_008(self):
		#保存成功的弹出框
		user_msg = self.user_msg()
		#日志开始记录
		self.log.log_start("DelAllUser")
		#获取用户删除的数据
		user_data = self.get_table_data("del_all_user")#user_check
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(user_data)):
			data = user_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.page_select_all()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.user.select_all_button()
					self.user.del_button()
					self.cmf.click_login_msg_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",user_msg,data,flag)
					#清空标识状态
					flag = False
#					if not self.cmf.is_namevalue_exsit(data[2],"fortUserAccount"):
#						print ("del user success")					
			except Exception as e:
				print ("del all fail: ") + str(e)
		self.log.log_end("DelAllUser")
	

	

	def test(self):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		update_xpath = "//table[@id='content_table']"
		text = self.tableEle.get_table_cell_text(update_xpath,0,4)[0]
		print self.cnEnde.cnCode(text)
#		text = self.getElem.find_element_wait_and_get_text('id',update_xpath)
	
	
	
	

if __name__ == "__main__":#internet explorer
	driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
	user = UserPage(driver)
	userCase = User(driver)
	user.user_login()
#	user.add_login_data()
	user.switch_to_moudle(u'运维管理',u'用户')
	
#	#改变用户开关状态
#	user.change_user_status_button("a","switch_off")
#	userCase.add_user_001()
#	userCase.edit_user_002()
#	userCase.create_user_cert_003()
#	userCase.create_user_cert_again_003()
#	userCase.delete_user_cert_004()
#
#	userCase.checkout_user_005()
#	userCase.search_user_by_username_006()
#	userCase.search_user_by_status_006()
#	userCase.search_user_by_dep_006()
#	userCase.search_user_by_role_006()
#	userCase.del_user_007()
	userCase.del_all_user_008()