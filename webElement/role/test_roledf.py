#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/6/12
#模块描述：角色定义
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsomp/common/")
from _log import log
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
		self.log = log()

	#点击添加按钮
	def add(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", self.ADD_ROLE)
		except Exception:
			print(u"点击添加按钮失败")

	#选择级别为部门级
	def level(self):
		try:
			self.getElem.find_element_wait_and_click("id", self.DEPARTMENT)
		except Exception:
			print(u"选择级别为部门级失败")

	#全选部门级角色
	def select_dptrole(self):
		try:
			self.getElem.find_element_wait_and_click("id", "treeDemo_1_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_17_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_21_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_26_check")
			self.getElem.find_element_wait_and_click("id", "treeDemo_31_check")
		except Exception:
			print(u"全选部门级角色失败")

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
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", self.SAVE_ROLE, 3)
		except Exception:
			print(u"点击保存按钮失败")

	#点击保存弹出框的确定按钮
	def confirm(self):
		try:
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", "aui_close")
		except Exception:
			print(u"点击弹出框的确定按钮失败")

	#点击删除弹出框的确定按钮
	def del_confirm(self):
		try:
			self.frameElem.switch_to_content()
			self.getElem.find_element_wait_and_click("classname", " aui_state_highlight")
		except Exception:
			print(u"点击删除弹出框的确定按钮失败")

	#点击返回按钮
	def back(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "history_skip")
		except Exception:
			print(u"点击返回按钮失败")

	#勾选全选框
	def check_all(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "checkbox")
		except Exception:
			print(u"勾选全选框失败")

	#点击批量删除按钮
	def bulkdel(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "delete_role")
		except Exception:
			print(u"点击批量删除按钮失败")

	u"""选择可管理角色
	   参数:
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def select_manage_role(self, index):
		try:
			selem = self.getElem.find_element_with_wait("id", "allRoles")
			self.selectElem.select_element_by_index(selem, index)
		except Exception:
			print(u"选择可管理角色失败")

	#点击可管理角色添加
	def manage_role_add(self):
		try:
			self.frameElem.switch_to_content()
			self.frameElem.switch_to_main()
			self.getElem.find_element_wait_and_click("id", "add_roles")
		except Exception:
			print(u"点击添加按钮失败")

	u"""添加其他权限
	   参数:
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def other_role_add(self, index):
		try:
			selem = self.getElem.find_element_with_wait("id", "allOtherPrivileges")
			self.selectElem.select_element_by_index(selem, index)
			self.getElem.find_element_wait_and_click("id", "add_privileges")
		except Exception:
			print(u"添加其他权限失败")

	u"""点击编辑按钮
	   参数:
	      - rolename:角色名称
	"""
	def edit(self, rolename):
		try:
			row = self.roleName_row(rolename)
			update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[1]"
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print(u"点击编辑按钮失败")

	u"""点击删除按钮
	   参数:
	      - rolename:角色名称
	"""
	def delete(self, rolename):
		try:
			row = self.roleName_row(rolename)
			update_xpath = "/html/body/form/div/div[6]/div[2]/div/table/tbody/tr[" + str(row) + "]/td[6]/input[2]"
			self.getElem.find_element_wait_and_click("xpath", update_xpath)
		except Exception:
			print(u"点击删除按钮失败")

	u"""添加角色名称
	   参数:
	      - rolename:角色名称
	"""
	def add_rolename(self, rolename):
		try:
			self.getElem.find_element_with_wait("id", self.FORTROLE_NAME).clear()
			self.getElem.find_element_wait_and_sendkeys("id", self.FORTROLE_NAME, rolename)
		except Exception:
			print(u"角色名称填写错误")

	u"""添加名称简写
	    参数：
	       -shortname 名称简写
	"""
	def add_shortname(self, shortname):
		try:
			self.getElem.find_element_with_wait("id", self.FORTROLE_SHORTNAME).clear()
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
			if self.is_rolename_exsit(rolename):
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
			self.level()
			self.select_dptrole()
			self.save_button()
			self.confirm()
			self.back()
		except Exception:
			print (u"添加部门管理员角色失败")

	u"""修改角色名称
	   参数:
	      - rolename:角色名称
	      -newrolename：修改后的角色名称
	 """
	def edit_role_003(self, rolename, newrolename):
		try:
			self.edit(rolename)
			self.add_rolename(newrolename)
			self.save_button()
			self.confirm()
			self.back()
		except Exception:
			print (u"修改系统管理员角色失败")

	u"""修改可管理角色
	   参数:
	      - rolename:角色名称
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def edit_managed_role_004(self, rolename, index):
		try:
			self.edit(rolename)
			self.select_manage_role(index)
			self.manage_role_add()
			self.save_button()
			self.confirm()
			self.back()
		except Exception:
			print (u"修改可管理角色失败")

	u"""修改其他权限
	   参数:
	      - rolename:角色名称
	      -index：select的索引，例0,1,2,从0开始计数
	"""
	def edit_other_role_005(self, rolename, index):
		try:
			self.edit(rolename)
			self.other_role_add(index)
			self.save_button()
			self.confirm()
			self.back()
		except Exception:
			print (u"修改其他权限失败")

	u"""删除角色
	   参数:
	      - rolename:角色名称
	"""
	def del_role_006(self, rolename):
		try:
			self.delete(rolename)
			self.del_confirm()
		except Exception:
			print(u"删除角色失败")

	u"""批量删除角色"""
	def bulkdel_role_007(self):
		try:
			self.check_all()
			self.bulkdel()
			self.del_confirm()
		except Exception:
			print(u"批量删除角色失败")

	#检验角色名称
	def checkout_rolename(self,rolename):
		self.add()
		self.add_rolename(rolename)
		self.save_button()
		if rolename == u"":
			print(u"角色名称不能为空！")
		elif rolename == u"!@#":
			print(u"名称不能输入非法字符,请重新输入！")
		self.confirm()
		self.back()

	#检验名称简写
	def checkout_shortname(self, rolename, shortname):
		self.add()
		self.add_rolename(rolename)
		self.add_shortname(shortname)
		self.select_sysrole()
		a=len(shortname)
		self.save_button()
		if shortname == u"!@#":
			print(u"名称不能输入非法字符,请重新输入！")
		elif shortname == u"":
			print(u"名称简写不能为空！")
		elif a > 4:
			print(u"简称不能大于四个字")
		elif rolename == u"系统管理员" and shortname == u"系统":
			print(u"角色名称及名称简写已存在!")
		elif shortname == u"系统":
			print(u"角色名称简写已存在!")
		elif rolename == u"系统管理员":
			print(u"角色名称已存在!")

		self.confirm()
		self.back()

	#没有选择菜单项点击保存
	def checkout_no_menu(self, rolename, shortname):
		self.add()
		self.add_rolename(rolename)
		self.add_shortname(shortname)
		self.save_button()
		print(u"请为该角色设置可查看或可编辑菜单")
		self.confirm()
		self.back()

	#同时选择密码包接收人和解密秘钥接收人
	def checkout_other(self, rolename, index1,index2):
		self.edit(rolename)
		self.other_role_add(index1)
		self.other_role_add(index2)
		# if index1 == 0:
		# 	print(u"该权限已添加!")
		# elif index1 == 1:
		# 	print(u"密码包接收人与解密密钥接收人权限互斥")
		# self.confirm()
		# self.back()

	#没有全选进行删除
	def checkout_noall_del(self):
		self.bulkdel()
		print(u"请选择要删除的数据")
		self.confirm()

	u'''右边框检查点
        Parameters:
            - type：定位右边框中元素的类型
            - elem：右边框元素的名字或者路径
            - data：excel一行的数据
            - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过
    '''
	def test_check_point(self,type,elem,data,flag):
		#检查点为空
		if data[1] == "":
			if flag:
				#测试点通过
				self.log.log_detail(data[0],True)
			else:
				#测试点没通过
				self.log.log_detail(data[0],False)

		#检查点不为空
		else:
			#右框中的文本内容
			optin = self.getElem.find_element_with_wait(type, elem)
			allText = self.selectElem.get_all_option_text(optin)
			for num in  range(len(allText)):
				if allText[num] == data[1]:
					#页面的内容与检查点内容一致，测试点通过
					self.log.log_detail(data[0], True)
				else:
					#页面抓取到的内容与检查点不一致，测试点不通过
					self.log.log_detail(data[0], False)

