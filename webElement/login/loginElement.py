#coding=utf-8
u''' 
#文件名：login
#被测软件版本号：V2.8.1
#作成人：于洋
#生成日期：2015-09-16
#模块描述：登录页面
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.support.ui import Select

sys.path.append("G:/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement

 
class loginPage(object):
    #登录方式
    LOGIN_METHOD = "loginMethod"
    #用户名
    LOGIN_USERNAME = "username"
    #口令
    LOGIN_PWD = "pwd"
    #登录按钮
    LOGIN_BUTTON = "do_login"
    #系统名称
    LOGIN_SYSTEM_NAME = "systemName"
    #帮助与控件下载
    LOGIN_DOWNLOAD = "/html/body/div[2]/div[5]/a"
    #版权所有
    LOGIN_COPYRIGHT = "/html/body/div[2]/div[5]/text()[2]"
    #退出
    QUIT = "logout"

    def __init__(self,driver):
        #selenuim驱动
        self.driver = driver
        self.getElem = getElement(driver)
        self.selectElem = selectElement(driver)
        self.frameElem = frameElement(self.driver)
    #获取登录方式
    def get_login_method(self):
        loginMethod = self.getElem.find_element_with_wait('id',self.LOGIN_METHOD)
        return self.selectElem.get_option_text(loginMethod,0)
        
    #设定登录方式
    def set_login_method(self,index): 
        try:
            loginMethod = self.getElem.find_element_with_wait('id',self.LOGIN_METHOD)
            self.selectElem.select_element_by_index(loginMethod,index)
        except Exception as e:
            print "login type error:" + str(e)
        
    #填写用户名
    def set_login_username(self,username):
        try:
            self.getElem.find_element_with_wait('id',self.LOGIN_USERNAME).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_USERNAME,username)
        except Exception as e:
            print "login name error:" + str(e)
        
    #填写口令
    def set_login_pwd(self,pwd):
        try:
            self.getElem.find_element_with_wait('id',self.LOGIN_PWD).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.LOGIN_PWD,pwd)
        except Exception as e:
            print "login password error:" + str(e)
    
    #点击登录按钮
    def click_login_button(self):
        try:
            self.getElem.find_element_wait_and_click('id',self.LOGIN_BUTTON) 
        except Exception as e:
            print "login button error:" + str(e)


    #点击版权所有
    def click_login_copyright(self,driver): 
        pass
        
    #用户名口令认证登录
    def login(self,list):
        self.set_login_method(int(list[2]))
        self.set_login_username(list[3])
        self.set_login_pwd(str(int(list[4])))
        self.click_login_button()
    
    #登陆成功
    def is_login_success(self):
        success = False
        
        try:
            self.frameElem.switch_to_top()
            text = self.getElem.find_element_wait_and_get_text("id","message")
        except Exception as e:
            text = ""
        
        if text == "个人信息维护":
            success = True

        return success
        
        
    #AD域认证登录
    def ad_login(self,driver,loginMethod,username,pwd):
        pass

    #AD域+口令认证登录
    def ad_pwd_login(self,driver,loginMethod,username,pwd):
        pass

    #RADIUS认证登录
    def otp_pwd_login(self,driver,loginMethod,username,pwd):
        pass

    
    #点击退出
    def quit(self):
        self.frameElem.switch_to_top()
        self.getElem.find_element_wait_and_click('id',self.QUIT)
    
#if __name__ == "__main__":
#    #启动页面
#    browers = initDriver().open_driver()
#    
#    login_page = loginPage(browers)
#    list = ["","","0","aaaa","1"]
#    login_page.login(list)
#    #login_page.quit()
#    login_page.click_msg_button()
    
    #关闭页面
    #initDriver().close_driver(browers)