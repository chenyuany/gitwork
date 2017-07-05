#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/7/3
#模块描述：角色互斥定义
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun

class roleMutex(object):

	#添加互斥角色按钮
	ADD_LEVEL = "add_level"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)

	u'''点击角色互斥的添加按钮'''
	def click_add_mutex(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click_EC("id", self.ADD_LEVEL,5)
		except Exception:
			print("Click Add mutex button failed")

	u'''选择角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	      -number：表示第几次添加
	'''
	def select_role(self, index, number):
		manage_index = index + 1
		option_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[1]/select/option[" + str(manage_index) + "]"
		select_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[1]/select"
		selem = self.getElem.find_element_with_wait("xpath", select_xpath)
		bb = self.selectElem.select_element_check("xpath", option_xpath)
		if bb is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''选择互斥角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	      -number：表示第几次添加
	'''
	def select_mutex_role(self, index, number):
		manage_index = index + 1
		option_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[3]/select/option[" + str(manage_index) + "]"
		select_xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[3]/select"
		selem = self.getElem.find_element_with_wait("xpath", select_xpath)
		bb = self.selectElem.select_element_check("xpath", option_xpath)
		if bb is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''点击添加互斥角色界面的保存按钮
	   Parameters:
	      -number：表示第几次添加
	'''
	def save_mutex_button(self, number):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			xpath = "/html/body/div/div[3]/div["+str(number)+"]/table/tbody/tr/td[4]/input[3]"
			self.getElem.find_element_wait_and_click_EC("xpath", xpath, 5)
		except Exception:
			print("Click the Save button to fail")

	u'''点击编辑按钮
	   Parameters:
	      - name:被编辑的角色列角色名称
	'''
	def edit_mutex(self, name):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			#获取页面有多少个(角色select)
			sltargets = self.driver.find_elements_by_name("select_role")
			for sle in sltargets:
				optargets = sle.find_elements_by_tag_name("option")
				for opt in optargets:
					if opt.text == name and opt.get_attribute("disabled") != "true":
						#获取当前角色select的id
						role_select_id = sle.get_attribute("id")
						#获取当前编辑按钮的id
						mutexid = "edit_role_mutex"+str(role_select_id[-1])
						self.getElem.find_element_wait_and_click_EC("id", mutexid, 5)
						break
				break
		except Exception:
			print("Click the Edit button to fail")

	u'''点击删除按钮
	   Parameters:
	      - name:角色列所选择的角色名称
	'''
	def delete_mutex(self, name):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			#获取页面有多少个(角色select)
			sltargets = self.driver.find_elements_by_name("select_role")
			for sle in sltargets:
				optargets = sle.find_elements_by_tag_name("option")
				for opt in optargets:
					if opt.text == name and opt.get_attribute("disabled") != "true":
						#获取当前角色select的id
						role_select_id = sle.get_attribute("id")
						#获取当前删除按钮的id
						delid = "delete_role_mutex"+str(role_select_id[-1])
						self.getElem.find_element_wait_and_click("id", delid, 5)
						break
				break
		except Exception:
			print("Click the delete button to fail")

	u'''取消编辑的角色互斥select框中选中的项
	   Parameters:
	      - rolename:角色列所选择的角色名称
	      - mutexname:角色互斥列所选择的角色名称
	'''
	def deselect_edit_mutex(self, rolename, mutexname):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		#获取页面有多少个(角色select)
		sltargets = self.driver.find_elements_by_name("select_role")
		for sle in sltargets:
			optargets = sle.find_elements_by_tag_name("option")
			for opt in optargets:
				if opt.text == rolename and opt.get_attribute("disabled") != "true":
					#获取当前角色select的id
					role_select_id = sle.get_attribute("id")
					#获取当前角色互斥select的id
					select_mutex_id = "select_mutex_role"+str(role_select_id[-1])
					#获取当前角色互斥select
					selem = self.getElem.find_element_with_wait("id", select_mutex_id)
					mutextarges = selem.find_elements_by_tag_name("option")
					for mutexopt in mutextarges:
						if mutexopt.get_attribute("class") == "opti":
							self.selectElem.deselect_text_element(selem, mutexname)

	u'''校验选择角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def check_select_role(self, index):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		selem = self.getElem.find_element_with_wait("name", "select_role")
		self.selectElem.select_element_by_index(selem, index)

	u'''校验选择互斥角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def check_select_mutex_role(self, index):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		selem = self.getElem.find_element_with_wait("name", "select_mutex_role")
		self.selectElem.select_element_by_index(selem, index)

	u'''校验点击保存按钮
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def check_save_mutex(self):
		self.getElem.find_element_wait_and_click_EC("name", "save")

	u'''点击用户的角色按钮
	   Parameters:
	      -username：用户账户
	'''
	def click_user_role(self, username):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_top()
		self.getElem.find_element_wait_and_click("link", u"运维管理")
		self.getElem.find_element_wait_and_click("link", u"用户")
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		#获取用户位于第几行
		userrow = self.cmf.find_row_by_name(username, "fortUserAccount")
		role_xpath = "/html/body/form/div/div[7]/div[2]/div/table/tbody/tr[" + str(userrow) + "]/td[9]/input[2]"
		self.getElem.find_element_wait_and_click("xpath", role_xpath)

	u'''选择所有角色
	   Parameters:
	      -index：select的索引，例0,1,2,从0开始计数
	'''
	def select_all_role(self, index):
		manage_index = index + 1
		option_xpath = "//select[@id='Roles']/option[" + str(manage_index) + "]"
		selem = self.getElem.find_element_with_wait("id", "Roles")
		bb = self.selectElem.select_element_check("xpath", option_xpath)
		if bb is False:
			self.selectElem.select_element_by_index(selem, index)

	u'''点击用户添加角色的添加按钮'''
	def click_add_role(self, index):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click_EC("id", "add_roles")
			selem = self.getElem.find_element_with_wait("id", "Roles")
			self.selectElem.deselect_element_by_index(selem, index)
		except Exception:
			print("Click add role button to fail")