#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入通用方法和日志模块
sys.path.append("/testIsomp/common")
from _icommon import commonFun
from _icommon import tableElement,getElement,frameElement


#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import *

class testSSO(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.tableElem = tableElement(driver)
        self.getElem = getElement(driver)
        self.frameElem = frameElement(driver)

    
    def win_sso(self):
        #实例化login
        loginFun = loginPage(self.driver)
        #登录
        loginFun.login(["","",0,"a","1"])
        
        #选择账号
        self.tableElem.get_table_td_select(0,5,0)
        
        imgXpath = "//img[@alt='mstsc']"
        #点击mstsc图标
        self.getElem.find_element_wait_and_click("xpath",imgXpath)
        
        self.frameElem.switch_to_content()
        self.getElem.find_element_wait_and_click("id","okButton")
        
        
        
        
        
        
        
        

#单文件测试使用
if __name__ == "__main__":
    browser = initDriver().open_driver()
    
    testSSO(browser).win_sso()
