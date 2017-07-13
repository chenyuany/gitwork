#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from threading import Thread
from selenium import webdriver
from selenium.webdriver import Remote
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


sys.path.append("/testIsomp/common/")
from _excelRead import excelRead
from _cnEncode import cnEncode
from _transCoding import jsonTranscoding

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/login/")
from loginElement import *

sys.path.append("/testIsomp/common")
from _icommon import commonFun
from _icommon import log
from _fileRead import fileRead
from _initDriver import initDriver
from _log import log

class testLogin(object):
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
    
    #登陆测试
    def login(self):
        self.log.log_start("login")
        
        u'''可以循环设定数据测试系统登录'''
        dataFile = dataFileName()
        loginPath = dataFile.get_login_test_data_url()
        sheets_name = ['default']#'default','ad','pwd_ad','radius'
        for sheetname in sheets_name:
            loginData = dataFile.get_data(loginPath,sheetname)
        
            #实例化login
            loginFun = loginPage(self.driver)
        
            #实例化commonFun
            cmf = commonFun(self.driver)
        
            #登陆的div弹窗的xpath
            loginMes = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
        
            #无检查点的测试项标识，如果为True说明通过
            flag = False
            for dataRow in range(len(loginData)):
                #把单行的数据赋值给列表data
                data = loginData[dataRow]
            
                try:
                    #如果不是第一行标题，则读取数据
                    if dataRow != 0:
                        if sheetname == 'default':
                            loginFun.login(data)
#                            if dataRow == 1:
#                                loginFun.set_max_login_count()
                        elif sheetname == 'ad':
                            loginFun.ad_login(data)
                        elif sheetname == 'pwd_ad':
                            loginFun.ad_pwd_login(data)
                        elif sheetname == 'radius':
                            loginFun.radius_pwd_login(data)
                        
                            #如果登陆成功，点击退出
                        if loginFun.is_login_success():
                            loginFun.quit()
                            #设定没有检查点的测试项通过
                            flag = True
                        
                        cmf.test_win_check_point("xpath",loginMes,data,flag)
                    
                        #清空标识状态
                        flag = False
                    
                except Exception as e: 
                    self.log.print_detail("login type error11",e)
#                    print "login type error:" + str(e)
        
        self.log.log_end("login")
        
        
if __name__ == "__main__":
    driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","internet explorer")
    loginElem = testLogin(driver)
    loginElem.login()
    
#    
#    driver_lists = initDriver().remote_driver_defined()
#    for driver in driver_lists:
#        testLogin(driver).login()
    
    
    
    
    '''
    lists = jsonTranscoding().set_brower()
    threads = []
    
    def execute_case(host,brower):
        driver = initDriver().remote_open_driver(host,brower)
        testLogin(driver).login()
        initDriver().close_driver(driver)
        
    for host,brower in lists.items():
        th = Thread(target=execute_case,args=(host,brower))
        th.start()
        threads.append(th)
            
    for th in threads:
        th.join()
    '''
        

    
    

        
        