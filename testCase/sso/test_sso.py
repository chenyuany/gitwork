#coding=utf-8
''' 
#文件名：
#作者：顾亚茹
#创建日期：2017/08/14
#模块描述：调用单点登录定义模块
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/sso")
from ssoElement import SsoPage

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

class testSso():
	def __init__(self,driver):
		self.driver = driver
		self.log = log()
		self.cmf = commonFun(driver)
		self.getElem = getElement(driver)
		self.cnEnde = cnEncode()
		self.ssoElem = SsoPage(self.driver)
		self.tableElem = tableElement(self.driver)
		self.selectElem = selectElement(driver)
		self.dataFile = dataFileName()
		self.frameElem = frameElement(self.driver)
	
	u'''获取测试数据
		Parameters:
			- sheetname:sheet名称
			return：表格数据
	'''
	def get_table_data(self,sheetname):
		dataFile = dataFileName()
		filePath = dataFile.get_sso_test_url()
		ssoFileData = dataFile.get_data(filePath,sheetname)
		return ssoFileData
	
	u'''sso'''
	def sso_login_001(self):
		#日志开始记录
		self.log.log_start("ssoLogin")
		#获取添加应用发布的数据
		sso_data = self.get_table_data("sso")
		#无检查点的测试项标识，如果为True说明通过
		flag = False
		for dataRow in range(len(sso_data)):
			data = sso_data[dataRow]
			try:
				#如果不是第一行标题，则读取数据
				if dataRow != 0 :
					self.frameElem.from_frame_to_otherFrame("rigthFrame")
					self.ssoElem.select_account(data[2],data[3])
					self.ssoElem.select_sso_icon(data[2],data[4])
					if data[5] != "":
						self.ssoElem.select_protocol(data[5])
					self.ssoElem.choice_browser(data[4],data[6],data[7],data[8])
					#self.ssoElem.refresh_windows()
					#判断测试项是否通过
					self.log.log_detail(data[0], True)
					#清空标识状态
					flag = False
	
			except Exception as e:
				print ("SSO login fail: ") + str(e)
		self.log.log_end("ssoLogin")
	
	
#if __name__ == "__main__":
#	browser = setDriver().set_local_driver()
#
#	commonSuite = CommonSuiteData(browser)
#	commonSuite.login_and_switch_to_common()
#	
#	ssoTest = testSso(browser)
#	ssoTest.sso_login_001()