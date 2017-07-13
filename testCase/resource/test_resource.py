#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import unittest
sys.path.append("/testIsomp/common/")
from _excelRead import excelRead
from _cnEncode import cnEncode

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/resource/")
from resourceElement import *

sys.path.append("/testIsomp/common")
from _icommon import commonFun
from _icommon import log

class testAddResource():
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()

    def add_resource(self):
        self.log.log_start("resource")
        u'''可以循环设定数据测试系统登录'''
#        dataFile = dataFileName()
#        loginPath = dataFile.get_unix_test_data_url()
#        sheets_name = ['unix']
#       assertEqual 判断是否相等     
#        loginData = dataFile.get_data(loginPath,sheetname)
##        实例化resourceElement
#        resourceFun = resourcePage(self.driver)
##        实例化commonFun
#        cmf = commonFun(self.driver)
##        保存按钮弹出框
#        resourceMes = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
#        for dataRow in range(len(loginData)):
#            data = loginData[dataRow]
#            try:
#                if dataRow != 0:
#                    resourceFun.add_unix_resource(data)
#                    self.assertEqual(cmf.get_win_test("xpath",resourceMes),data[1])
#            except Exception as e:
#                print "add unix resource error"

        for sheetname in sheets_name:
            loginData = dataFile.get_data(loginPath,sheetname)
            #loginData = dataFile.get_data(r"D:\testIsomp\testData\unix_test_data.xlsx",sheetname)
            print loginData
            #实例化login
            resourceFun = resourcePage(self.driver)
        
            #实例化commonFun
            cmf = commonFun(self.driver)
            #登陆的div弹窗的xpath
            resourceMes = "html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div"
            #无检查点的测试项标识，如果为True说明通过
            flag = False
            for dataRow in range(len(loginData)):
                #把单行的数据赋值给列表data
                data = loginData[dataRow]
                        
                try:
                    #如果不是第一行标题，则读取数据
                    if dataRow != 0:
                        if sheetname == 'unix':
                            #resourceFun.add_unix_resource(data)
                            
                            
                            #设定没有检查点的测试项通过
                            flag = True
                                    
                        cmf.test_win_check_point("xpath",resourceMes,data,flag)
                                
                        #清空标识状态
                        flag = False
                                
                except Exception as e: 
                    print "add resource error:" + str(e)
                    
        self.log.log_end("addResource")

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
    #data = ['','','3','unix','192.168.23.118']
    testAddResource(browser).add_unix_resource()
            
        


