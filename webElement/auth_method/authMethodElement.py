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

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

class AuthMethodPage():

	#全部认证方式
	ALL_METH_METHOD = "all_globalAuthMethod"
	#已选认证方式
	SELECTED_AUTH_METHOD = "select_globalAuthMethod"
	#认证方式添加按钮
	ADD_BUTTON = "add"
	#删除按钮
	DELETE_BUTTON = "delete"
	#保存按钮
	SAVE_BUTTON = "save_auth_method"
	#AD域1认证IP
	AD_AUTH_IP = "ldapHost0"
	#AD域1认证port
	AD_AUTH_PORT = "ldapPort0"
	#AD域1认证域名
	AD_AUTH_DOMIAN_NAME = "ldapName0"
	#域1对应的添加按钮
	DOMIAN1_ADD_BUTTON = "btn_01"
	#域2对应的删除按钮
	DOMIAN2_DEL_BUTTON = "delete_01"
	#域2配置IP
	DOMIAN2_IP = "ldapHost1"
	#主RADIUS认证IP
	RADIUS_AUTH_IP = "radiusIp0"
	#主RADIUS认证PORT
	RADIUS_AUTH_PORT = "radiusPort0"
	#主RADIUS认证通讯秘钥
	RADIUS_AUTH_KEY = "radiusShareSecret0"
	#备RADIUS认证IP
	BACKUP_RADIUS_IP = "radiusIp1"
	#备RADIUS认证通讯秘钥
	BACKUP_RADIUS_KEY = "radiusShareSecret1"
	
	def __init__(self,driver):
		#selenuim驱动
		self.driver = driver
		self.getElem = getElement(self.driver)
		self.selectElem = selectElement(self.driver)
		self.frameElem = frameElement(self.driver)
		self.commElem = commonFun(self.driver)
		self.cmf = commonFun(self.driver)
		self.dataFile = dataFileName()
		self.login = loginPage(self.driver)
		self.cnEnde = cnEncode()
		self.log = log()
	
	#选择添加的认证方式
	def select_auth_method(self,value):
		try:
			revalue = self.cnEnde.is_float(value)
			select_elem = self.getElem.find_element_with_wait('id',self.ALL_METH_METHOD)
#			select_elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,self.ALL_METH_METHOD)))
			self.selectElem.select_element_by_value(select_elem,str(revalue))
		except Exception as e:
			print ("select auth method error: ") + str(e)

	#选择删除的认证方式
	def select_del_auth_method(self,value):
		revalue = self.cnEnde.is_float(value)
		#print revalue
		try:
			select_elem = self.getElem.find_element_with_wait('id',self.SELECTED_AUTH_METHOD)
			self.selectElem.select_element_by_value(select_elem,str(revalue))
		except Exception as e:
			print ("select auth method will be delete error : ") + str(e)

	#检查全部认证方式中是否存在添加过的认证方式        
	def check_option_is_not_exist(self,type,elem,list_text):
		isExsit = True
		try:
			selectd_elem = self.getElem.find_element_with_wait(type,elem)
			allText = self.selectElem.get_all_option_text(selectd_elem)
			for text in allText:
				if text == list_text:
					isExsit = False
					break
		except Exception:
			print ("Selectd Auth method is not exist ") + list_text
		return isExsit
	
	#检查认证方式是否添加到已选认证方式        
	def check_option_is_selectd(self,type,elem,list_text):
		isExsit = False
		try:
			selectd_elem = self.getElem.find_element_with_wait(type,elem)
			allText = self.selectElem.get_all_option_text(selectd_elem)
			for text in allText:
				if text == list_text:
					isExsit = True
					break
		except Exception:
			print ("Auth method is not selected: ") + list_text
		return isExsit
		
	#填写AD域1认证IP
	def set_ad_auth_ip(self,ip_):
		try:
			ip = self.cnEnde.is_float(ip_)
			self.getElem.find_element_with_wait('id',self.AD_AUTH_IP).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.AD_AUTH_IP,ip)
		except Exception as e:
			#self.log.print_detail("login password error",e)
			print ("Ad auth ip error: ") + str(e) 

	#填写AD域2认证IP
	def set_domian2_ip(self,ip_):
		try:
			ip = self.cnEnde.is_float(ip_)
			self.getElem.find_element_with_wait('id',self.DOMIAN2_IP).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.DOMIAN2_IP,ip)
		except Exception as e:
#			self.log.print_detail("login password error",e)
			print ("Ad auth ip error: ") + str(e)

	#填写AD域1认证PORT
	def set_ad_auth_port(self,port_):
		try:
			port = self.cnEnde.is_float(port_)
			self.getElem.find_element_with_wait('id',self.AD_AUTH_PORT).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.AD_AUTH_PORT,port)
		except Exception as e:
#			self.log.print_detail("login password error",e)
			print ("Ad auth ip error: ") + str(e)
				
	#填写AD域1认证域名
	def set_ad_auth_domian_name(self,domianName_):
		try:
			domianName = self.cnEnde.is_float(domianName_)
			self.getElem.find_element_with_wait('id',self.AD_AUTH_DOMIAN_NAME).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.AD_AUTH_DOMIAN_NAME,domianName)
		except Exception as e:
#			self.log.print_detail("login password error",e)
			print ("Ad auth domainName error: ") + str(e)

	#填写主RADIUS认证IP
	def set_radius_auth_ip(self,radiusIp_):
		try:
			radiusIp = self.cnEnde.is_float(radiusIp_)
			self.getElem.find_element_with_wait('id',self.RADIUS_AUTH_IP).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.RADIUS_AUTH_IP,radiusIp)
		except Exception as e:
	#		self.log.print_detail("login password error",e)
			print ("Radius auth ip error:") + str(e)

	#填写备RADIUS认证IP
	def set_backup_radius_ip(self,radiusIp_):
		try:
			radiusIp = self.cnEnde.is_float(radiusIp_)
			self.getElem.find_element_with_wait('id',self.BACKUP_RADIUS_IP).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.BACKUP_RADIUS_IP,radiusIp)
		except Exception as e:
	#		self.log.print_detail("login password error",e)
			print ("Backup Radius auth key error: ") + str(e)

	#填写主RADIUS认证PORT
	def set_radius_auth_port(self,radiusPort_):
		try:
			radiusPort = self.cnEnde.is_float(radiusPort_)
			self.getElem.find_element_with_wait('id',self.RADIUS_AUTH_PORT).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.RADIUS_AUTH_PORT,radiusPort)
		except Exception as e:
	#		self.log.print_detail("login password error",e)
			print ("Radius auth port error:" ) + str(e)

#	def set_radius_auth_key_with_ipisnull(self,list,index):
#		try:
#			radius_key = self.cnEnde.is_float(list[index])
#			self.getElem.find_element_with_wait('id',self.RADIUS_AUTH_KEY).click()

	#填写主RADIUS认证秘钥
	def set_radius_auth_key(self,radiusKey):
		try:
			radius_key = self.cnEnde.is_float(radiusKey)
			WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, self.RADIUS_AUTH_KEY))).clear()
			WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID, self.RADIUS_AUTH_KEY))).send_keys(str(radiusKey))
#			self.getElem.find_element_with_wait('id',self.RADIUS_AUTH_KEY).clear()
#			self.getElem.find_element_wait_and_sendkeys('id',self.RADIUS_AUTH_KEY,str(radiusKey))
		except Exception as e:
	#		self.log.print_detail("login password error",e)
			print ("Radius auth key error: ") + str(e)

	#填写备RADIUS认证秘钥
	def set_backup_radius_key(self,backupKey):
		try:
			backup_key = self.cnEnde.is_float(backupKey)
			self.getElem.find_element_with_wait('id',self.BACKUP_RADIUS_KEY).clear()
			self.getElem.find_element_wait_and_sendkeys('id',self.BACKUP_RADIUS_KEY,str(backup_key))
		except Exception as e:
#			self.log.print_detail("login password error",e)
			print ("Backup Radius auth key error:") + str(e)

	#点击AD域配置域1对应的添加按钮
	def domian1_add_button(self):
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.DOMIAN1_ADD_BUTTON))).click()
		except Exception as e:
			print ("domian1 add button error: ") + str(e)

	#点击AD域2对应的删除按钮
	def domian2_del_button(self):
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.DOMIAN2_DEL_BUTTON))).click()
		except Exception as e:
			print ("domian2 del button error: ") + str(e)

	#点击认证方式添加按钮
	def auth_add_button(self):
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.ADD_BUTTON))).click()
		except Exception as e:
			print ("Auth_method add button error: ") + str(e)
	
	#点击认证方式删除按钮    
	def auth_del_button(self):
		try:
			WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.DELETE_BUTTON))).click()
		except Exception as e:
			print ("Auth method delete button error: ") + str(e)

	#点击保存按钮
	def save_button(self):
		try:
			elem = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.SAVE_BUTTON)))
			elem.click()
		except Exception as e:
			print ("Auth method save button error : ") + str(e)
			
	#取消所有选中的证书
	def quit_selectd_all_method(self):
		try:
			selem = self.getElem.find_element_with_wait("id",self.SELECTED_AUTH_METHOD)
			options = selem.find_elements_by_tag_name("option")
			for option in options:
				value = option.get_attribute('value')
#				self.selectElem.select_element_by_value(selem,value)
				self.selectElem.deselect_element_by_value(selem,value)
		except Exception as e:
			print ("Quit all method error：") + str(e)

	#选中所有的认证方式
	def selectd_all_method(self,selem,value_,status='0'):
		try:
			#selem = self.getElem.find_element_with_wait("id",self.SELECTED_AUTH_METHOD)
			options = selem.find_elements_by_tag_name("option")
			select_options_text = self.selectElem.get_all_option_text(selem)
			default_auth_text = "用户名+口令(默认方式)"
			text =  self.cnEnde.cnCode(','.join(select_options_text))			
			num = len(options)
			if num != 1 or(num == 1 and default_auth_text not in select_options_text):
				for option in options:
					value = option.get_attribute('value')
					if value != value_:
						self.selectElem.select_element_by_value(selem,value)
				if status == '0':
					self.auth_del_button()
					self.save_button()
					self.cmf.click_login_msg_button()
		except Exception as e:
			print ("Seleted all method error: ") + str(e)


	#判断元素内容是否修改成功
	def compare_elem_text(self,type,value,text_):
		try:
			elem_text = WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element((type,value),text_))
			if elem_text == True:
				print ("Modey element success")
		except Exception:
			return False

	#判断两个list是否相等
	def compare_list_is_equal(self,list1,list2,data):
		try:
			selem1_option_text = sorted(list1)
			selem2_option_text = sorted(list2)
			selem1_option_num = len(selem1_option_text)
			selem2_option_num = len(selem2_option_text)
			if selem1_option_num != selem2_option_num:
				return False
			elif selem1_option_text == selem2_option_text:
				self.log.log_detail(data[0],True)
				return True
			else:
				return False
		except Exception as e:
			print ("Two select element is not equal: ") + str(e)
			
	#获取select元素所有option的文本值
	def get_select_options_text(self,type,value):
		try:
			selem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((type,value)))
			#selem = self.getElem.find_element_with_wait(type,value)
			select_options_text = self.selectElem.get_all_option_text(selem)
			return select_options_text
		except Exception as e:
			print ("select element text get error: ") + str(e)

	#点击用户的高级选项
	def get_user_select_auth_text(self,data):
		self.frameElem.from_frame_to_otherFrame("topFrame")
		self.cmf.select_menu(u"运维管理")
		self.cmf.select_menu(u"运维管理",u"用户")
		#获取用户isomper对应的行号
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		user_row = self.cmf.find_row_by_name(data[3],"fortUserAccount")
#		print user_row
		edit_xpath = "//table[@id='content_table']/tbody/tr[" + str(user_row) + "]/td[9]/input[1]"
		self.getElem.find_element_wait_and_click('xpath',edit_xpath,5)
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		#点击高级选项
		self.getElem.find_element_wait_and_click('id','btn_high')
	#		self.get_select_options_text(type,value)

	#登录并切换至认证方式页面
	def login_and_switch_auth_method(self):
		file_path = self.dataFile.get_auth_method_test_data_url()
		login_data = self.dataFile.get_data(file_path,'add_user')
#		auth_method_data = self.get_table_data("login")
		logindata = login_data[1]
		self.login.login(logindata)
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.cmf.select_role_by_text(logindata[6])
		self.cmf.select_menu(u"策略配置")
		self.cmf.select_menu(u"策略配置",u"认证强度")
		self.frameElem.from_frame_to_otherFrame("mainFrame")

	#选择所有认证方式
	def select_all_auth(self):
		selem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,self.ALL_METH_METHOD)))
		select_list_text = self.selectElem.get_all_option_text(selem)
		options = selem.find_elements_by_tag_name("option")
		for option in options:
			if option.is_selected() == False:
				option.click()
		if select_list_text != []:
			self.auth_add_button()
			self.set_ad_auth_ip("172.16.10.240")
			self.set_ad_auth_domian_name("hgcs")
			self.set_radius_auth_ip("192.168.23.128")
			self.set_radius_auth_key("123")
			self.save_button()
			self.cmf.click_login_msg_button()