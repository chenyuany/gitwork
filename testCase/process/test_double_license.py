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

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
from _icommon import commonFun,getElement,selectElement,frameElement,tableElement
from _log import log
sys.path.append("/testIsomp/webElement/process/")
from test_double_license_ment import Dobapproval
sys.path.append("/testIsomp/webElement/authorization")
from authrizationElement import AuthorizationPage
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

class testDobapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.log = log()
		self.data = dataFileName()
		self.cmf = commonFun(driver)
		self.double = Dobapproval(driver)
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)

	u'''获取测试数据
	   Parameters:
	      - sheetname:sheet名称
	   return：表格数据
	'''
	def get_double_data(self, sheetname):
		dataFile = dataFileName()
		dobPath = dataFile.get_double_license_test_data_url()
		dobData = dataFile.get_data(dobPath, sheetname)
		return dobData

	u'''添加双人授权'''
	def add_double_license_001(self):
		#日志开始记录
		self.log.log_start("add_double_license")
		#获取双人授权的数据
		dobData = self.get_double_data("add_double_license")
		for dataRow in range(len(dobData)):
			data = dobData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow != 0:
					self.double.click_double_license_button(data[1])
					self.authElem.click_all_approver()
					self.authElem.click_all_candidate()
					self.authElem.click_start_association()
					self.authElem.click_create_relate()
					self.cmf.click_login_msg_button()
					#点击返回
					self.authElem.click_child_page_back_button()
					self.log.log_detail(u"添加双人授权成功", True)
			except Exception as e:
				print ("add_double_license fail: ") + str(e)

		self.log.log_end("add_double_license")

	u'''双人审批同终端审批'''
	def same_termina_approvel_002(self):
		#日志开始记录
		self.log.log_start("same_termina_approvel")
		#获取双人审批申请的数据
		appData = self.get_double_data("double_license_sso")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果是第1行,读取数据
				if dataRow == 1:
					self.double.send_double_license_applicant(data)
					self.loginElem.quit()
			except Exception as e:
				print ("same_termina_approvel fail: ") + str(e)
		self.log.log_end("same_termina_approvel")

	u'''双人审批终端拒绝审批'''
	def termina_deny_approvel_003(self):
		#日志开始记录
		self.log.log_start("termina_deny_approvel")
		#获取双人审批申请的数据
		appData = self.get_double_data("double_license_sso")

		for dataRow in range(len(appData)):
			data = appData[dataRow]
			try:
				#如果不是第1行,读取数据
				if dataRow == 2:
					self.double.send_double_license_applicant(data)
					self.loginElem.quit()
					self.comsuit.use_new_user_login()
			except Exception as e:
				print ("termina_deny_approvel fail: ") + str(e)
		self.log.log_end("termina_deny_approvel")
