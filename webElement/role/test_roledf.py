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
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement


class Role(object):
	#角色名称
	FORTROLE_NAME="fortRoleName"
	#名称简写
	FORTROLE_SHORTNAME="fortRoleShortName"
	#添加按钮
	ADD_ROLE="add_role"
	#部门级
	DEPARTMENT="department"
	#保存按钮
	SAVE_ROLE="save_role"

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)

	#点击添加按钮
	def add(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", self.ADD_ROLE)
		except Exception:
			print(u"点击添加按钮失败")

	#全选系统级角色
	def select_sysrole(self):
		try:
			self.getElem.find_element_wait_and_click("id", "treeDemo_1_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_3_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_7_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_11_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_16_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_20_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_23_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_50_check")
		except Exception:
			print(u"全选系统级角色失败")

	#点击编辑角色界面的保存按钮
	def save_button(self):
		try:
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
		except Exception:
			print(u"点击保存按钮失败")

	#点击弹出框的确定按钮
	def confirm(self):
		try:
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
		except:
			print(u"点击弹出框的确定按钮失败")

	#点击返回按钮
	def back(self):
		try:
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print(u"点击返回按钮失败")

	u"""添加角色名称
	   参数:
	      - rolename:角色名称
	 """
	def add_rolename(self, rolename):
		try:
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_NAME, rolename)
		except Exception:
			print(u"角色名称填写错误")

	u"""添加名称简写
	    参数：
	       -shortname 名称简写
	"""
	def add_shortname(self, shortname):
		try:
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_SHORTNAME, shortname)
		except Exception:
			print(u"名称简写填写错误")

	u"""查询角色名称位于第几行
	   参数:
	      - rolename:角色名称
	      return：定位该角色名称位于第几行
	 """
	def roleName_row(self, rolename):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		row = 0
		try:
			text_list = self.driver.find_elements_by_name("fortRoleName")
			for fortRoleName in text_list:
				row = row+1
				fortRoleName_text = fortRoleName.text
				if fortRoleName_text == rolename:
					break
		except Exception:
			print rolename + " roleName is not exsit."
		return row

	u"""判断角色名称是否存在
	   参数:
	      - rolename:角色名称
	      return：角色名称是否存在
	 """
	def is_rolename_exsit(self, rolename):
		isExsit = False
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		try:
			text_list = self.driver.find_elements_by_name("fortRoleName")
			for fortRoleName in text_list:
				fortRoleName_text = fortRoleName.text
				if fortRoleName_text == rolename:
					isExsit = True
					break
		except Exception:
			print rolename + " roleName is not exsit."
		return isExsit

	u"""添加系统管理员
	   参数:
	      - rolename:角色名称
	      -shortname：名称简写
	 """
	def add_system_role_001(self, rolename, shortname):
		try:
			self.add()
			self.add_rolename(rolename)
			self.add_shortname(shortname)
			self.select_sysrole()
			self.save_button()
			self.confirm()
			self.back()
		except Exception:
			print (u"添加系统管理员角色失败")

	u"""添加部门管理员
	   参数:
	      - rolename:角色名称
	      -shortname：名称简写
	 """
	def add_depart_role_002(self, rolename, shortname):
		try:
			self.add()
			self.add_rolename(rolename)
			self.add_shortname(shortname)
			self.getElem.find_element_wait_and_click("id", self.DEPARTMENT)
			self.getElem.find_element_wait_and_click("id", "treeDemo_1_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_17_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_21_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_26_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_31_check")
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print (u"添加部门管理员角色失败")

	u"""修改角色名称
	   参数:
	      - rolename:角色名称
	      -newrolename：修改后的角色名称
	 """
	def edit_role_003(self, rolename, newrolename):
		row = self.roleName_row(rolename)
		update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
		try:
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
			self.getElem.find_element_with_wait("id", self.FORTROLE_NAME).clear()
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_NAME, newrolename)
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print (u"修改系统管理员角色失败")

	u"""修改可管理角色
	   参数:
	      - rolename:角色名称
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def edit_managed_role_004(self, rolename, index):
		row = self.roleName_row(rolename)
		update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
		try:
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
			selem = self.getElem.find_element_with_wait("id", "allRoles")
			self.selectElem.select_element_by_index(selem, index)
			self.getElem.find_element_wait_and_click("id", "add_roles")
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print (u"修改可管理角色失败")

	u"""修改其他权限
	   参数:
	      - rolename:角色名称
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def edit_other_role_005(self, rolename, index):
		row = self.roleName_row(rolename)
		update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
		try:
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
			selem = self.getElem.find_element_with_wait("id", "allOtherPrivileges")
			self.selectElem.select_element_by_index(selem, index)
			self.getElem.find_element_wait_and_click("id", "add_privileges")
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print (u"修改其他权限失败")

	u"""删除角色
	   参数:
	      - rolename:角色名称
	"""
	def del_role_006(self, rolename):
		row = self.roleName_row(rolename)
		update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[2]"
		try:
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", " aui_state_highlight")
		except Exception:
			print(u"删除角色失败")

	u"""批量删除角色"""
	def bulkDel_role_007(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "checkbox")
			self.getElem.find_element_wait_and_click("id", "delete_role")
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", " aui_state_highlight")
		except Exception:
			print(u"批量删除角色失败")

	#检验角色
	def check_role_008(self):
		pass
	
