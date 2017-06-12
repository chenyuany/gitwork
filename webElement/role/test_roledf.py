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

	#判断角色名称是否存在
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
		except Exception as e:
			print rolename + " roleName is not exsit."
		return isExsit

	#添加系统管理员
	def add_system_role_001(self,rolename,shortname):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id",self.ADD_ROLE)
			self.getElem.find_element_wait_and_sendkeys("id",self.FORTROLE_NAME,rolename)
			self.getElem.find_element_wait_and_sendkeys("id",self.FORTROLE_SHORTNAME,shortname)
			self.getElem.find_element_wait_and_click("id","treeDemo_1_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_3_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_7_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_11_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_16_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_20_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_23_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_50_check")
			self.getElem.find_element_wait_and_click("id",self.SAVE_ROLE,3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname","aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id","history_skip")
		except Exception:
			print (u"添加系统管理员角色失败")

	#添加部门管理员
	def add_depart_role_002(self,rolename,shortname):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id",self.ADD_ROLE)
			self.getElem.find_element_wait_and_sendkeys("id",self.FORTROLE_NAME,rolename)
			self.getElem.find_element_wait_and_sendkeys("id",self.FORTROLE_SHORTNAME,shortname)
			self.getElem.find_element_wait_and_click("id",self.DEPARTMENT)
			self.getElem.find_element_wait_and_click("id","treeDemo_1_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_17_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_21_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_26_check")
			self.getElem.find_element_wait_and_click("id","treeDemo_31_check")
			self.getElem.find_element_wait_and_click("id",self.SAVE_ROLE,3)
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname","aui_close")
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id","history_skip")
		except Exception:
			print (u"添加部门管理员角色失败")

	#修改角色名称
	def edit_role_003(self):
		pass

	#修改可管理角色
	def edit_managed_role_004(self):
		pass

	#修改其他权限
	def edit_other_role_005(self):
			pass
	#删除角色
	def del_role_006(self):
		pass
	#批量删除角色
	def bulkDel_role_007(self):
		pass
	#检验角色
	def check_role_008(self):
		pass
	
