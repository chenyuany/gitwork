#coding=utf-8
u''' 
#文件名：login
#被测软件版本号：V2.8.1
#作成人：顾亚茹
#生成日期：2017-06-10
#模块描述：登录页面
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



class loginPage(object):
    #登录方式
    LOGIN_METHOD = "loginMethod"
    #用户名(ad+口令)
    LOGIN_USERNAME = "username"
    #AD域方式用户名
    LOGIN_LDAP_USERNAME = "ldapUsername"
    #口令(ad+口令)
    LOGIN_PWD = "pwd"
    #AD域方式口令
    LOGIN_LDAP_PWD = "ldapPwd"
    #radius+口令登录方式口令
    LOGIN_RADIUS_PWD = "radiusPwd"
    #登录按钮
    LOGIN_BUTTON = "do_login"
    #系统名称
    LOGIN_SYSTEM_NAME = "systemName"
    #帮助与控件下载
    LOGIN_DOWNLOAD = "/html/body/div[2]/div[5]/a"
    #版权所有
    LOGIN_COPYRIGHT = "/html/body/div[2]/div[5]/text()[2]"
    #访问失败次数
    ACCESS_MAX_ACCOUNT = "lockStrategyCount"
    #会话策略保存按钮
    STRATEGY_SAVE_BUTTON = "save_globalStrategy"
    #退出
    QUIT = "logout"

    def __init__(self,driver):

        self.driver = driver
        self.getElem = getElement(self.driver)
        self.dataFile = dataFileName()
        self.selectElem = selectElement(self.driver)
        self.frameElem = frameElement(self.driver)
        self.commElem = commonFun(self.driver)
        self.cmf = commonFun(self.driver)
        self.cnEnde = cnEncode()
        self.log = log()

    u'''获取登录方式'''
    def get_login_method(self):
        loginMethod = self.getElem.find_element_with_wait('id',self.LOGIN_METHOD)
        return self.selectElem.get_option_text(loginMethod,0)
        
    u'''设定登录方式
            parameters : 
                value : 登录方式value值
    '''
    def set_login_method(self,value): 
        revalue = self.cnEnde.is_float(value)
        wait = WebDriverWait(self.driver,10)
        loginMethod = wait.until(EC.presence_of_element_located((By.ID, self.LOGIN_METHOD)))
        try:
            self.selectElem.select_element_by_value(loginMethod,str(revalue))
        except Exception as e:
            self.log.print_detail("login type error",e)

    u'''填写变量内容
        parameters:
            var_text : 变量内容
            locator : 定位方式对应的属性值
    '''       
    def set_common_var_text(self,var_text,locator):
    	try:
    	    revar_text = self.cnEnde.is_float(var_text)
    	    var_elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,locator)))
    	    var_elem.clear()
    	    var_elem.send_keys(revar_text)
    	except Exception as e:
#            self.log.print_detail("set login var text error: ",revar_text + " " + e)
    	    print ("set login var text error: ") + str(revar_text) + str(e)
    
        
    u'''填写用户账号
        parameters:
            account : 用户账号
    '''       
    def set_login_username(self,account):
        return self.set_common_var_text(account,self.LOGIN_USERNAME)
            
    u'''填写AD域用户名
        parameters:
            account : AD域用户账号
    '''
    def set_ad_login_username(self,adUsername):
        return self.set_common_var_text(adUsername,self.LOGIN_LDAP_USERNAME)
           
        
    u'''填写口令
        parameters:
            account : 口令
    '''
    def set_login_pwd(self,pwd):
        return self.set_common_var_text(pwd,self.LOGIN_PWD)
            
    u'''填写填写AD域密码
        parameters:
            account : AD域密码
    '''
    def set_ad_login_pwd(self,adPwd):
        return self.set_common_var_text(adPwd,self.LOGIN_LDAP_PWD)
            
    u'''填写填写RADIUS密码
        parameters:
            account : RADIUS密码
    '''    
    def set_radius_login_pwd(self,radiusPwd):
        return self.set_common_var_text(radiusPwd,self.LOGIN_RADIUS_PWD)
        
    u'''点击登录按钮'''
    def click_login_button(self):
        try:
            wait = WebDriverWait(self.driver,10)
            body = wait.until(EC.element_to_be_clickable((By.TAG_NAME,'body')))
            do_login = wait.until(EC.element_to_be_clickable((By.ID,self.LOGIN_BUTTON)))
            do_login.click()

        except Exception as e:
            self.log.print_detail("click login button error",e)


    u'''点击版权所有'''
    def click_login_copyright(self): 
        pass
        
    u'''用户名口令认证登录
            parameters:
                list : 登录用户列表信息
    '''
    def login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.click_login_button()
    
    u'''判断是否登陆成功'''
    def is_login_success(self):
        success = False
        try:
            #self.frameElem.switch_to_top()
            self.frameElem.from_frame_to_otherFrame('topFrame')
            text = self.getElem.find_element_wait_and_get_text("id","message")
#            print text
        except Exception as e:
            text = ""
        
        if text == "个人信息维护":
            success = True

        return success
        
    u'''AD域认证登录
            parameters:
                list : 登录用户列表信息
    '''    
    def ad_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_ad_login_username(list[3])
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
        
    u'''AD域+口令认证登录
            parameters:
                list : 登录用户列表信息
    '''   
    def ad_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(int(list[2]))
        self.set_login_username(list[3])
        self.set_login_pwd(int(list[4]))
        self.set_ad_login_pwd(list[5])
        self.click_login_button()
    
    u'''Radius认证登录
            parameters:
                list : 登录用户列表信息
    '''
    def radius_pwd_login(self,list):
        self.frameElem.switch_to_content()
        self.set_login_method(list[2])
        self.set_login_username(list[3])
        self.set_login_pwd(list[4])
        self.set_radius_login_pwd(list[5])
        self.click_login_button()
        
    #证书认证登录
    def cert_login(self,list):
        brower_name = self.driver.capabilities['browserName']
    
        
    u'''设置访问失败最大次数
            parameters:
                roleName : 角色名称
    '''
    def set_max_login_count(self):
        
        self.frameElem.from_frame_to_otherFrame('topFrame')
        #切换至系统管理员角色
#        self.commElem.select_role_by_text(roleName)

        self.commElem.select_menu(u"策略配置")
        self.commElem.select_menu(u"策略配置",u"会话配置")
        
        self.frameElem.from_frame_to_otherFrame('mainFrame')

        #选择密码策略默认配置
        strategy_option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,'fortPasswordStrategyId')))
        self.selectElem.select_element_by_visible_text(strategy_option,u'请选择')
        
        #设置最大登录数
        access_max_elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,self.ACCESS_MAX_ACCOUNT)))
        access_max_elem.clear()
        access_max_elem.send_keys(3)
        lock_time = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID,"lockStrategyTime")))
        lock_time.clear()
        lock_time.send_keys(1)        
#        time.sleep(3)
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.STRATEGY_SAVE_BUTTON))).click()   
        self.commElem.click_login_msg_button()

    u'''点击退出'''
    def quit(self):
        self.frameElem.from_frame_to_otherFrame('topFrame')
        wait = WebDriverWait(self.driver,10)
        quit_btn = wait.until(EC.element_to_be_clickable((By.ID,self.QUIT)))
        quit_btn.click()

        
        
#if __name__ == "__main__":
    #启动页面
#    browers = initDriver().open_driver()
#    

#    login_page = loginPage(browers)
#    list = ["","","0","test","1",'22',""]
#    login_page.login(list)
#    list = ["","","0","aaaa","1"]
#    login_page.login(list)
#    login_page.set_max_login_count()
#    login_page.quit()
#    login_page.click_msg_button()
    
    #关闭页面
    #initDriver().close_driver(browers)