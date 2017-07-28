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
from _log import log
from _icommon import getElement,selectElement,frameElement,commonFun
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Usergroup(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.log = log()

	u'''左边框点击用户组'''
	def click_left_usergroup(self):
		self.frameElem.from_frame_to_otherFrame("leftFrame")
		self.getElem.find_element_wait_and_click_EC("id", "url1")

	u'''点击用户组展开按钮'''
	def click_usergroup_switch(self):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		self.getElem.find_element_wait_and_click_EC("id", "user_group_1_switch")
