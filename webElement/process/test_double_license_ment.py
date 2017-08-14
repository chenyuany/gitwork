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
import sys, time

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("/testIsomp/common/")
from _log import log
from _icommon import getElement, selectElement, frameElement, commonFun
from _cnEncode import cnEncode

sys.path.append("/testIsomp/webElement/authorization")
from authrizationElement import AuthorizationPage

sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsomp/webElement/department/")
from test_dptm_ment import Department

sys.path.append("/testIsomp/webElement/process/")
from test_access_approval_ment import Accapproval


class Dobapproval(object):

	def __init__(self, driver):
		self.driver = driver
		self.getElem = getElement(driver)
		self.selectElem = selectElement(driver)
		self.frameElem = frameElement(driver)
		self.cmf = commonFun(driver)
		self.log = log()
		self.cnEn = cnEncode()
		self.depart = Department(driver)
		self.loginElem = loginPage(self.driver)
		self.authElem = AuthorizationPage(self.driver)
		self.acproval = Accapproval(driver)

	u'''点击授权操作列双人授权按钮
        parameters:
            name : 授权名称
    '''
	def click_double_license_button(self, name):
		self.frameElem.from_frame_to_otherFrame("mainFrame")
		self.authElem.operate_double_approval(name)

	u'''点击双人审批图标
            parameters :
                rename : 资源名称
    '''
	def click_double_license_icon(self, rename):
		self.frameElem.from_frame_to_otherFrame("rigthFrame")
		rname = self.cnEn.is_float(rename)
		row = self.acproval.select_resoure_sso(rname)
		xpath = "/html/body/div[1]/div[7]/div[2]/div/table/tbody/tr[" + str(
			row * 2) + "]/td/div/table/tbody/tr/td[2]/a/img"
		self.getElem.find_element_wait_and_click_EC("xpath", xpath)

	u'''选择授权人
            parameters :
                authorizer : 授权人名称
    '''
	def select_authorizer(self, authorizer):
		self.frameElem.switch_to_artIframe()
		author = self.cnEn.is_float(authorizer)
		selem = self.getElem.find_element_with_wait_EC("id", "fortApproverId")
		self.selectElem.select_element_by_visible_text(selem, author)

	u'''勾选同终端直接输入口令访问'''
	def check_same_termina(self):
		self.frameElem.switch_to_artIframe()
		self.getElem.find_element_wait_and_click_EC("id", "fortIsRemoteApply")

	u'''填写授权人密码
	   Parameters:
	      - passwd:授权人密码
	'''
	def set_authorizer_pwd(self, passwd):
		self.frameElem.switch_to_artIframe()
		pwd = self.cnEn.is_float(passwd)
		self.getElem.find_element_wait_and_clear("id", "password")
		self.getElem.find_element_wait_and_sendkeys("id", "password", pwd)

	u'''申请人发送双人审批申请
	   Parameters:
          - data:excel中的一行数据
	'''
	def send_double_license_applicant(self, data):
		self.acproval.select_resoure_account(data[1], data[2])
		self.click_double_license_icon(data[1])
		self.select_authorizer(data[3])
		if data[4] != 'no':
			self.check_same_termina()
			self.set_authorizer_pwd(data[4])
		self.acproval.set_operation_description(data[5])
		self.acproval.click_sure_button()
		self.driver.implicitly_wait(10)
		self.log.log_detail(data[0], True)

	u'''审批人通过流程控制进行审批
	   Parameters:
          - acpData:审批人进行审批的数据
          - number:流程号
	'''
	def approver_by_process_approval(self, acpData, number):
		pass

	def call_other_browsers(self):
		pass

	# newhlond = webdriver.Ie()
	# #IE窗口最大化
	# newhlond.maximize_window()
	# newhlond.get("https://172.16.10.169")
	# newhlond.get("javascript:document.getElementById('overridelink').click();")
	# self.frameElem.switch_to_content()
	# self.loginElem.set_login_method(listuser)
	# self.loginElem.set_login_username(user)
	# self.user_login(listuser)

