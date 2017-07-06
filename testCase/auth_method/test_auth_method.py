#coding=utf-8
''' 
#文件名：
#作者：顾亚茹
#创建日期：2017/7/04
#模块描述：调用认证方式定义模块
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
from _icommon import commonFun,getElement,selectElement,frameElement
from _log import log
from _initDriver import *
sys.path.append("/testIsomp/webElement/auth_method/")
from authMethodElement import AuthMethodPage
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage


class testAuthMethod(object):
	#已选角色select框
#	SELECTED_AUTH_METHOD = "select_globalAuthMethod"
	#提示框文件元素路径
	def auth_method_msg(self):
		auth_method_msg = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
		return auth_method_msg

	#登录认证方式select框
#	LOGIN_AUTH_METHOD = "loginMethod"
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.authMethod = AuthMethodPage(driver)
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.login = loginPage(self.driver)
		
	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_auth_method_test_data_url()
		authFileData = dataFile.get_data(filePath,sheetname)
		return authFileData	

	u'''添加AD域认证方式'''
	def add_ad_method_001(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
#		self.authMethod.delete_other_auth_method()
		selem = self.getElem.find_element_with_wait("id",selectd_auth_method)
		self.authMethod.selectd_all_method(selem,'2')
		#日志开始记录
		self.log.log_start("addADMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 1:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_auth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.set_ad_auth_ip(data[4])
					self.authMethod.set_ad_auth_port(data[5])
					self.authMethod.set_ad_auth_domian_name(data[6])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("AD auth method add success")
			except Exception as e:
				print ("AD auth method add fail: ") + str(e)
		self.log.log_end("addADMethod")
		
	u'''添加radius认证方式'''
	def add_radius_method_002(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"		
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("addRadiusMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 2:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_auth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.set_radius_auth_ip(data[4])
					self.authMethod.set_radius_auth_port(data[5])
					self.authMethod.set_radius_auth_key(data[7])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("Radius auth method add success")
			except Exception as e:
				print ("Radius auth method add fail: ") + str(e)
		self.log.log_end("addRadiusMethod")
		
	u'''添加AD域+口令认证方式'''
	def add_ad_and_pwd_method_003(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"		
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("addADAndPwdMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")
	
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 3:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_auth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("AdAndPwd auth method add success")
			except Exception as e:
				print ("AdAndPwd auth method add fail: ") + str(e)
		self.log.log_end("addADAndPwdMethod")

	u'''添加radius+口令认证方式'''
	def add_radius_and_pwd_method_004(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"		
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("addRadiusMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 4:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_auth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("RadiusAndPwd auth method add success")
			except Exception as e:
				print ("RadiusAndPwd auth method add fail: ") + str(e)
		self.log.log_end("addRadiusAndPwdMethod")

	u'''添加证书认证方式'''
	def add_cert_method_005(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("addCertMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("add_auth_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 5:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.select_auth_method(data[2])
					self.authMethod.auth_add_button()
					self.authMethod.check_option_is_not_exist('id',all_auth_method,data[3])
					#校验是否添加到已选认证方式
					self.authMethod.check_option_is_selectd('id',selectd_auth_method,data[3])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("Cert auth method add success")
			except Exception as e:
				print ("Cert auth method add fail: ") + str(e)
		self.log.log_end("addCertMethod")
	
	#修改AD域认证配置
	def mod_ad_method_006(self):
		#已选认证方式
		ad_auth_ip = "ldapHost0"
		ad_auth_domian_name = "ldapName0"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("ModeyADMethodConfig")
		#获取修改AD域配置测试数据
		auth_method_data = self.get_table_data("mod_ad_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_ad_auth_ip(data[2])
					self.authMethod.set_ad_auth_port(data[3])
					self.authMethod.set_ad_auth_domian_name(data[4])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					self.authMethod.compare_elem_text('id',ad_auth_ip,data[2])
					self.authMethod.compare_elem_text('id',ad_auth_domian_name,data[4])
					#清空标识状态
					flag = False					
			except Exception as e:
				print ("Modey AD method config fail: ") + str(e)
		self.log.log_end("ModeyADMethodConfig")
	
	#AD域认证配置校验
	def ad_method_checkout_007(self):
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("ADMethodCheckout")
		#获取修改AD域配置测试数据
		auth_method_data = self.get_table_data("ad_method_checkout")
	
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_ad_auth_ip(data[2])
					self.authMethod.set_ad_auth_port(data[3])
					self.authMethod.set_ad_auth_domian_name(data[4])
					if dataRow == range(len(auth_method_data))[-1]:
						self.authMethod.domian1_add_button()
						self.authMethod.set_domian2_ip(data[5])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
			except Exception as e:
				print ("ADMethodCheckout fail: ") + str(dataRow) + str(e)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authMethod.domian2_del_button()
		self.log.log_end("ADMethodCheckout")
	
	
	u'''radius认证校验'''
	def radius_checkout_008(self):
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("RadiusCheckout")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("radius_method_checkout")#radius_method_checkout,Sheet1
		#radius通讯秘钥
		radius_auth_key = "radiusShareSecret0"

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_radius_auth_ip(data[2])
					self.authMethod.set_radius_auth_port(data[3])
					if data[2] == "" or data[2] == "123.abc":
						self.getElem.find_element_with_wait('id',radius_auth_key).click()
						self.cmf.click_login_msg_button()
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.set_radius_auth_key(data[4])
					self.authMethod.set_radius_auth_key(data[4])
#					if dataRow == range(len(auth_method_data))[-1]:
					self.authMethod.set_backup_radius_ip(data[5])
					self.authMethod.set_backup_radius_key(data[6])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("Radius auth method add success")
			except Exception as e:
				print ("RadiusCheckout fail: ") + str(e)
		self.log.log_end("RadiusCheckout")

	u'''删除radius认证方式'''
	def del_radius_auth_method_009(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("delradiusMethod")
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("del_raius_method")

		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow == 1:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.quit_selectd_all_method()
					self.authMethod.select_del_auth_method(data[2])
					self.authMethod.auth_del_button()
					#校验已选认证是否删除radius认证
					self.authMethod.check_option_is_not_exist('id',selectd_auth_method,data[3])
					#校验是否添加到全部认证方式
					self.authMethod.check_option_is_selectd('id',all_auth_method,data[3])
					self.authMethod.set_radius_auth_ip(data[4])
					self.authMethod.set_radius_auth_key(data[5])					
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
					#清空标识状态
					flag = False
					
					#校验登录页面是否有认证方式
#					self.login.quit()
#					self.frameElem.switch_to_content()
#					if self.authMethod.check_option_is_selectd('id',login_auth_method,data[3]):
#						print("AD auth method add success")
			except Exception as e:
				print ("delradiusMethod fail: ") + str(e)
		self.log.log_end("delradiusMethod")

	u'''删除其他认证方式'''
	def del_other_auth_method_010(self):
		#全部认证方式
		all_auth_method = "all_globalAuthMethod"
		#已选认证方式
		selectd_auth_method = "select_globalAuthMethod"
		login_auth_method = "loginMethod"
		#获取添加系统管理员测试数据
		auth_method_data = self.get_table_data("del_raius_method")		
		#保存成功的弹出框
		auth_method_msg = self.auth_method_msg()
		#日志开始记录
		self.log.log_start("delotherMethod")
		flag = False
		for dataRow in range(len(auth_method_data)):
			data = auth_method_data[dataRow]
			try:
				#如果是第2行标题，则读取数据
				if dataRow == 2:
					self.frameElem.from_frame_to_otherFrame("mainFrame")
					self.authMethod.quit_selectd_all_method()
					selem = self.getElem.find_element_with_wait("id",selectd_auth_method)
					self.authMethod.selectd_all_method(selem,'2','1')
					self.authMethod.auth_del_button()
					#校验已选认证方式只有默认方式
					self.authMethod.check_option_is_selectd('id',all_auth_method,data[3])
					self.authMethod.save_button()
					self.frameElem.switch_to_content()
					self.cmf.test_win_check_point("xpath",auth_method_msg,data,flag)
				#清空标识状态
				flag = False				
			except Exception as e:
				print ("delotherMethod fail: ") + str(e)
		self.log.log_end("delotherMethod")

#if __name__ == "__main__":
#	driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
#	login_data = testAuthMethod(driver).get_table_data("login")
#	data = login_data[1]
#	loginPage(driver).login(data)
#	frameElement(driver).switch_to_content()
#	frameElement(driver).switch_to_top()
#	commonFun(driver).select_role(1)
#	commonFun(driver).select_menu(u"策略配置")
#	commonFun(driver).select_menu(u"策略配置",u"认证强度")
#	frameElement(driver).from_frame_to_otherFrame("mainFrame")
#	authMethod = AuthMethodPage(driver)
#	authMethod.delete_other_auth_method()
#	testAuthMethod(driver).add_ad_method_001()
#	testAuthMethod(driver).add_radius_method_002()
#	testAuthMethod(driver).add_ad_and_pwd_method_003()
#	testAuthMethod(driver).add_radius_and_pwd_method_004()
#	testAuthMethod(driver).add_cert_method_005()
#	frameElement(driver).from_frame_to_otherFrame("mainFrame")
#	authMethod.quit_selectd_all_method()
#	testAuthMethod(driver).mod_ad_method_006()
#	testAuthMethod(driver).ad_method_checkout_007()
#	testAuthMethod(driver).radius_checkout_008()
#	testAuthMethod(driver).del_radius_auth_method_009()
#	testAuthMethod(driver).del_other_auth_method_010()