#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/07/07
#模块描述：组织定义部门
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys,time
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsomp/common/")
from _log import log
from _icommon import getElement,selectElement,frameElement,commonFun

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


#引入ActionChains类  提供了鼠标的操作方法
from selenium.webdriver.common.action_chains import  ActionChains


class Department(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.log = log()
		self.action = ActionChains(driver)

	u'''点击用户的保存按钮'''
	def save_user_button(self):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_main()
		self.getElem.find_element_wait_and_click("id", "save_user")

	u'''左边框点击部门'''
	def click_left_department(self):
		self.frameElem.switch_to_content()
		self.frameElem.switch_to_left()
		self.getElem.find_element_wait_and_click("id", "url0")

	u'''点击展开按钮'''
	def click_dept_switch(self):
		self.frameElem.switch_to_content()
		self.driver.switch_to_frame("content1")
		self.driver.switch_to_frame("mainFrame")
		self.driver.switch_to_frame("rigthFrame")
		self.getElem.find_element_wait_and_click("id", "treeDemo_1_switch")

	u'''点击基本操作
	   parameter:
	       - deptname:传入要被操作的部门
	       - operation：代表基本操作0代表添加、1代表编辑、2代表上移、3代表下移
	'''
	def click_basic_operation(self, deptname, operation):
		self.click_dept_switch()
		elems = self.driver.find_elements_by_tag_name("a")
		for elem in elems:
			elemtext = elem.get_attribute("title")
			id = elem.get_attribute("id")
			if deptname == elemtext:
				self.getElem.find_element_wait_and_click_EC("id", id)
				#点击添加部门按钮
				if operation == 0:
					buttonadd = "addBtn_treeDemo_" + str(id[-3])
					self.getElem.find_element_wait_and_click_EC("id", buttonadd)
					break
				#点击编辑部门按钮
				elif operation == 1:
					buttonedit = "treeDemo_" + str(id[-3]) + "_edit"
					self.getElem.find_element_wait_and_click_EC("id", buttonedit)
					break
				#点击上移按钮
				elif operation == 2:
					buttontoup = "toUpBtn_treeDemo_" + str(id[-3])
					self.getElem.find_element_wait_and_click_EC("id", buttontoup)
					break
				#点击下移按钮
				elif operation == 3:
					buttontodown = "toDownBtn_treeDemo_" + str(id[-3])
					self.getElem.find_element_wait_and_click_EC("id", buttontodown)
					break

	u'''点击上移、下移按钮校验
	   parameter:
	       - deptname:传入要被操作的部门
	       - operation：代表基本操作0代表添加、1代表编辑、2代表上移、3代表下移
	'''
	def click_up_button(self, deptname, operation):
		self.frameElem.switch_to_content()
		self.driver.switch_to_frame("content1")
		self.driver.switch_to_frame("mainFrame")
		self.driver.switch_to_frame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		for elem in elems:
			elemtext = elem.get_attribute("title")
			id = elem.get_attribute("id")
			if deptname == elemtext:
				self.getElem.find_element_wait_and_click("id", id)
				#点击上移按钮
				if operation == 2:
					#移动次数
					locates = range(self.return_locate_line(deptname))
					for locate in locates:
						buttontoup = "toUpBtn_treeDemo_" + str(id[-3])
						self.getElem.find_element_wait_and_click("id", buttontoup)
						if locate == locates[-1]:
							break
				#点击下移按钮
				elif operation == 3:
					locates = range(len(elems)-self.return_locate_line(deptname))
					for locate in locates:
						buttontodown = "toDownBtn_treeDemo_" + str(id[-3])
						self.getElem.find_element_wait_and_click("id", buttontodown)
						if locate == locates[-1]:
							break
				break

	u'''返回位于第几行
	   parameter:
	       - deptname:传入要被操作的部门
	'''
	def return_locate_line(self, deptname):
		self.frameElem.switch_to_content()
		self.driver.switch_to_frame("content1")
		self.driver.switch_to_frame("mainFrame")
		self.driver.switch_to_frame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		locate = 0
		for elem in elems:
			elemtext = elem.get_attribute("title")
			id = elem.get_attribute("id")
			locate = locate + 1
			if deptname == elemtext:
				return locate - 1

	u'''点击删除按钮
	   parameter:
	       - deptname:传入要被操作的部门
	'''
	def click_del_button(self, deptname):
		self.frameElem.switch_to_content()
		self.driver.switch_to_frame("content1")
		self.driver.switch_to_frame("mainFrame")
		self.driver.switch_to_frame("rigthFrame")
		elems = self.driver.find_elements_by_tag_name("a")
		for elem in elems:
			elemtext = elem.get_attribute("title")
			id = elem.get_attribute("id")
			if deptname == elemtext:
				self.getElem.find_element_wait_and_click("id", id)
				buttonremove = "treeDemo_" + str(id[-3]) + "_remove"
				self.getElem.find_element_wait_and_click("id", buttonremove)
				break


	u'''在弹出框中填写内容
	   parameter:
	       - deptname:输入填写的部门名称
	'''
	def popup_sendkey(self, deptname):
		self.frameElem.switch_to_content()
		xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div[2]/input"
		self.getElem.find_element_wait_and_sendkeys("xpath", xpath, deptname)

	u'''点击确定按钮'''
	def click_ok_button(self):
		self.frameElem.switch_to_content()
		divselems = self.driver.find_elements_by_class_name("aui_title")
		for divselem in divselems:
			messagetext = divselem.get_attribute('textContent')
			pagetext = u"消息"
			if messagetext == pagetext:
				xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''清空部门文本框内容'''
	def clear_depart_text(self):
		self.frameElem.switch_to_content()
		xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div[2]/input"
		self.getElem.find_element_wait_and_clear("xpath", xpath)

	u'''点击取消按钮'''
	def click_cancel_button(self):
		self.frameElem.switch_to_content()
		divselems = self.driver.find_elements_by_class_name("aui_title")
		for divselem in divselems:
			messagetext = divselem.get_attribute('textContent')
			pagetext = u"消息"
			if messagetext == pagetext:
				self.driver.implicitly_wait(2)
				xpath = "/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break
		# divselem = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "aui_state_lock")))
		# divselem = self.getElem.find_element_with_wait("classname", "aui_state_lock", 5)
		#
		# xpath = "/html/body/div[2]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[2]"
		# divselem.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
		# remove = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, css)))
		# divselem.find_element_by_xpath(xpath).click()

	u'''点击最外层确定按钮'''
	def click_Outermost_button(self):
		self.frameElem.switch_to_content()
		divselems = self.driver.find_elements_by_class_name("aui_title")
		for divselem in divselems:
			messagetext = divselem.get_attribute('textContent')
			pagetext = u"警告"
			if messagetext == pagetext:
				self.driver.implicitly_wait(2)
				xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button"
				self.getElem.find_element_wait_and_click_EC("xpath", xpath)
				break

	u'''多层弹窗类检查点
	   Parameters:
	      - type：定位弹窗中元素的类型
	      - elem：弹窗元素的名字或者路径
	      - data：excel一行的数据
	      - flag:没有检查点的测试项通过标识。Ture为通过，False为未通过
	'''
	def multil_div_check_point(self,type,elem,data,flag):
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
			#判断文本内容是否一致
			elemText = self.getElem.find_element_wait_and_compare_text(type,elem,data)
			self.click_Outermost_button()
			if elemText:
				# 页面的内容与检查点内容一致，测试点通过
				self.log.log_detail(data[0], True)
			else:
				#页面抓取到的内容与检查点不一致，测试点不通过
				self.log.log_detail(data[0],False)