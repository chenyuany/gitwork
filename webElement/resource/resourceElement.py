#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun
from _cnEncode import cnEncode

class resourcePage(object):
    
    #添加按钮
    #RESOURCE_ADD_BUTTON = "add_resource"
    RESOURCE_ADD_BUTTON = "btn_tj"
    #确认按钮
    #OK_BUTTON = "okButton"
    OK_BUTTON = "//div[@id='aui_buttons']/button[@id='okButton']"
    #linux资源类型箭头
    LINUX_TYPE_ARROW = "treeDemo_2_switch"
    #网络设备类型箭头
    NETWORK_TYPE_ARROW = "treeDemo_14_switch"
    #debian资源类型
    DEBIAN_RESOURCE = "treeDemo_12_span"
    #资源名称
    RESOURCE_NAME = "fortResourceName"
    #资源IP
    RESOURCE_IP = "fortResourceIp"
    #从IP
    RESOURCE_RESERVE_IP = "fortIps"
    #系统版本
    SYSTEM_VERSION = "fortVersion"
    #改密驱动名称
    CHANGE_PWD_DRIVER = "fortDriverName"
    #密码策略
    RESOURCE_STRATEGY_PWD = "fortStrategyPasswordId"
    #账号同步
    ACCOUNT_SYNCHRONIZE = "btn_high"
    #管理员账号
    ADMIN_ACCOUNT = "fortAdminAccount"
    #管理员口令
    ADMIN_PASSWORD = "fortAdminPassword"
    #确认口令
    ADMIN_REPASSWORD = "reFortAdminPassword"
    #保存按钮
    SAVE_BUTTON = "save_resource"
    #返回按钮
    BACK_BUTTON = "history_skip"
    
    def __init__(self,driver):
        #selenuim驱动
        self.driver = driver
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
        self.commElem = commonFun(self.driver)
        self.cnEnde = cnEncode()
    
    
    #切换到资源模块
    def switch_to_resource_module(self):
#        self.frameElem.from_frame_to_otherFrame("topFrame")
        self.commElem.select_menu(u'运维管理')
        self.commElem.select_menu(u'运维管理',u'资源')
        
        
    #点击添加按钮    
    def click_add_button(self):
        return self.getElem.find_element_wait_and_click("classname",self.RESOURCE_ADD_BUTTON)
    
    #选择资源类型
    def select_resource_arrow(self,typeindex,resourceindex,status='0'):
        self.driver.implicitly_wait(10)
        self.frameElem.from_frame_to_otherFrame("artIframe")
        try:
#            判断是否有上级资源类型,默认有上级
            if status == '0':
#                点击上级资源类型
                self.getElem.find_element_wait_and_click("id","treeDemo_" + str(typeindex) + "_switch")
                time.sleep(3)
                self.driver.execute_script("window.scrollBy(0,100)","")
                #选择具体的资源类型
                self.getElem.find_element_wait_and_click('id',"treeDemo_" + str(resourceindex) + "_span")
                self.driver.switch_to_default_content()
                #点击确定按钮
                self.getElem.find_element_wait_and_click('xpath',self.OK_BUTTON)
        except Exception as e:
            print "Not found parent resource type:" + str(e)
        
    u'''公用部分'''
    def common_use(self):
        self.switch_to_resource_module()
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_add_button()
        
    #填写资源名称
    def set_resource_name(self,resourcename):
        try:
            resourcename = self.cnEnde.is_float(resourcename)
            self.getElem.find_element_with_wait('id',self.RESOURCE_NAME).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.RESOURCE_NAME,resourcename)
        except Exception as e:
            print "resourcename is error :" + str(e)
    
    #填写资源IP
    def set_resource_ip(self,ip):
        try:
            reIp = self.cnEnde.is_float(ip)
            #if self.getElem.find_element_with_wait('id',self.RESOURCE_IP).is_displayed() == True
            self.getElem.find_element_with_wait('id',self.RESOURCE_IP).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.RESOURCE_IP,reIp)
        except Exception as e:
            print "resourcename is error :" + str(e)
            
    #填写从IP
    def set_resource_fortIps(self,fortIps):
        try:
            refortIps = self.cnEnde.is_float(fortIps)
            self.getElem.find_element_with_wait('id',self.RESOURCE_RESERVE_IP).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.RESOURCE_RESERVE_IP,refortIps)
        except Exception as e:
            print "fortIps is error:" + str(e)
    
    #填写系统版本
    def set_sys_version(self,sysVersion):
        try:
            resysVersion = self.cnEnde.is_float(sysVersion)
            self.getElem.find_element_with_wait('id',self.SYSTEM_VERSION).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.SYSTEM_VERSION,resysVersion)
        except Exception as e:
            print "system_version is error:" + str(e)
    
    #填写改密驱动名称
    def set_changePwd_driver(self,driverName):
        try:
            redriverName = self.cnEnde.is_float(driverName)
            self.getElem.find_element_with_wait('id',self.CHANGE_PWD_DRIVER).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.CHANGE_PWD_DRIVER,redriverName)
        except Exception as e:
            print "change_pwd_driver is error:" + str(e)
    
    # 选择密码策略       
    def select_pwd_strategy(self,text):
        try:
            retext = self.cnEnde.is_float(text)
            pwd_strategy = self.getElem.find_element_with_wait('id',self.RESOURCE_STRATEGY_PWD)
            self.selectElem.select_element_by_visible_text(pwd_strategy,retext)
        except Exception as e:
            print "Pwd strategy select error:" + str(e)
            
    #点击账号同步
    def click_account_sync(self):
        try:
            self.getElem.find_element_wait_and_click('id',self.ACCOUNT_SYNCHRONIZE)
        except Exception as e:
            print "account sync element is not available:" + str(e)
    
    #设置管理员账号
    def set_admin_account(self,adminAccount):
        try:
            reaccount = self.cnEnde.is_float(adminAccount)
            self.getElem.find_element_with_wait('id',self.ADMIN_ACCOUNT).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.ADMIN_ACCOUNT,reaccount)
        except Exception as e:
            print "Admin account error:" + str(e)
    
    #设置管理员口令
    def set_admin_pwd(self,adminPwd):
        try:
            repwd = self.cnEnde.is_float(adminPwd)
            self.getElem.find_element_with_wait('id',self.ADMIN_PASSWORD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.ADMIN_PASSWORD,repwd)
        except Exception as e:
            print "Admin password error :" + str(e)
            
    #口令确认
    def set_confirm_pwd(self,confirmPwd):
        try:
            reconfirmPwd = self.cnEnde.is_float(confirmPwd)
            self.getElem.find_element_with_wait('id',self.ADMIN_REPASSWORD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.ADMIN_REPASSWORD,confirmPwd)
        except exception as e:
            print "confirm Password is error :" + str(e)
            
    #点击保存按钮
    def click_save_button(self):
        try:
            self.getElem.find_element_wait_and_click("id",self.SAVE_BUTTON)
        except Exception as e:
            print "resource save button error:" + str(e)

    
    #添加unix资源
    def add_unix_resource(self,list):
        self.common_use()
        self.select_resource_arrow(list[2],list[3],list[4])
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.set_resource_name(list[5])
        self.set_resource_ip(list[6])
        self.commElem.select_all_checkbox()
        self.click_save_button()

    def add_network_resource(self,operationindex):
        pass
    #add windows resource
    def add_common_windows_resource(self,list):
        pass
    
    #add yunei resource
    def add_inner_domain_resource(self,list):
        pass
    
    def add_domain_resource(self,list):
        pass
    
    def add_bs_resource(self,list):
        pass
    
    def add_database_resource(self):
        self.switch_to_resource_module()
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.click_add_button()
        self.select_database_resource()
        
        
        
if __name__ == "__main__":
    browser = initDriver().open_driver()
    resource_page = resourcePage(browser)
    getElem = getElement(browser)
    a = getElem.find_element_with_wait("id","loginMethod")
        
    selectElem = selectElement(browser)
    selectElem.select_element_by_index(a,0)
    pwd = "html/body/div[2]/div[3]/form/table/tbody[2]/tr[4]/td/input"
    getElem.find_element_wait_and_sendkeys("id","username","test")
    getElem.find_element_wait_and_sendkeys("xpath",pwd,"1")
    getElem.find_element_wait_and_click("id","do_login",5)
    frameElem = frameElement(browser)
    frameElem.from_frame_to_otherFrame("topFrame")
    common = commonFun(browser)
    #common.click_login_msg_button()
    #选泽xt角色
    common.select_role("2")
#    添加Linux资源
    list = ["","","2","3","0","unix","192.168.23.118"]
    resource_page.add_unix_resource(list)
#    添加网络设备资源类型
#    resource_page.add_unix_resource(22,24)
#    添加mysql资源类型
#    resource_page.add_unix_resource('',57,'1')
    
#    list = [3,"unix","192.168.23.118"]
#    添加windows资源类型
#    resource_page.add_unix_resource(14,15)









    