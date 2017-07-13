#coding=utf-8
u''' 
#文件名：
#被测软件版本号：V2.8.1
#作成人：
#生成日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

sys.path.append("/testIsomp/common/")
from _initDriver import *
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement
from _cnEncode import cnEncode
from _log import log

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role

class UserPage():
    #添加按钮class
    ADD_BUTTON = "btn_tj"
    #删除按钮
    DEL_BUTTON = "delete_user"
    #用户部门检索
    SEARCH_DEP = "department_name"
    #账号或名称检索
    SEARCH_ACCOUNT_OR_NAME = "fortUserAccountOrName"
    #角色检索
    SEARCH_ROLE = "fortRoleId"
    #用户状态检索
    SEARCH_USER_STATUS = "fortUserState"
    #点击部门清空
    DEP_CLEAR = "clean_tree_data"

    #检索按钮
    SEARCH_BUTTON = "fort_user"
    #重置按钮
    RESRT_BUTTON = "resetting"
    #用户账号
    USER_ACCOUNT = "fortUserAccount"
    #用户名称
    USER_NAME = "fortUserName"
    #开始时间
    USER_START_TIME = "fortStartTime"
    #结束时间
    USER_END_TIME = "fortEndTime"
    #用户状态
    USER_STATUS = "fortUserState"
    #用户部门
    USER_DEP = "department_name"
    #登录时是否修改
    LOGIN_MODEY = "fortInitializePassword"
    #用户密码
    USER_PWD = "fortUserPassword"
    #确认密码
    USER_RE_PWD = "fortUserPasswordAgain"
    #手机号
    USER_MOBILE = "fortUserMobile"
    #电话
    USER_PHONE = "fortUserPhone"
    #审计查看审批管理员
    IS_APPROVAL = "isDownLoadApproval"
    #邮箱
    USER_EMAIL = "fortUserEmail"
    #地址
    USER_ADDRESS = "fortUserAddress"
    #高级选项
    ADVANCED_OPTIONS = "btn_high"
    #时间规则
    TIME_RULE = "fortRuleTimeId"
    #地址规则
    ADDRESS_RULE = "fortRuleAddressId"
    #认证方式
    AUTH_CODE = "fortAuthenticationCode"
    #域账号
    USER_DOMAIN_ACCOUNT = "fortDomainAccount"
    #radius账号
    USER_RADIUS = "fortRadius"
    #保存按钮
    SAVE_BUTTON = "save_user"
    #点击角色信息
    ROLE_MEG_BUTTON = "//html/body/form[@id='user_form']/div/div[2]/div[1]/a[2]"
    #角色选择框
    ROLE_SELECTD_ELEM = "Roles"
    #角色添加按钮
    ROLE_ADD_BUTTON = "add_roles"
    #全选按钮
    SELECT_ALL_BUTTON = "checkbox"
    #生成证书
    CREATE_CERT = "createCertificate"
    DELETE_CERT = "deleteCertificate"
    #证书名称
    CERT_NAME = "downLoad"
    #没有生成证书之前的名字
    INIT_CERT_NAME = "certificateName"
    #证书序列号
    CERT_SERIAL_NUM = "certificateNum"
    
    def __init__(self,driver):
        self.driver = driver
        self.log = log()
        self.role = Role(driver)
        self.cmf = commonFun(driver)
        self.getElem = getElement(driver)
        self.cnEnde = cnEncode()
        self.tableElem = tableElement(self.driver)
        self.selectElem = selectElement(driver)
        self.dataFile = dataFileName()
        self.login = loginPage(self.driver)
        self.frameElem = frameElement(self.driver)

    u'''点击添加按钮'''
    def add_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.ADD_BUTTON))).click()
        except Exception as e:
            print ("user add button error: ") + str(e)

    u'''点击删除按钮'''
    def del_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CLASS_NAME, self.DEL_BUTTON))).click()
        except Exception as e:
            print ("Delete button error: ") + str(e)

    '''账号或名称检索框
        parameters:
            accountName : 账号或名称
    '''
    def search_accountorname(self,accountName):
        try:
            reaccountName = self.cnEnde.cnCode(accountName)
            self.getElem.find_element_with_wait('id',self.SEARCH_ACCOUNT_OR_NAME).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.SEARCH_ACCOUNT_OR_NAME,reaccountName)
        except Exception as e:
            print ("search account or name error: ") + str(e)

    '''用户角色检索框
        parameters:
            roleText : 用户角色
    '''
    def search_user_role(self,roleText):
        try:
            selem = self.getElem.find_element_with_wait('id',self.SEARCH_ROLE)
            self.selectElem.select_element_by_visible_text(selem,str(roleText))
        except Exception as e:
            print ("User role search is error: ") + str(e)

    '''用户状态检索
        parameters:
            status : 用户状态
    '''    
    def search_by_user_status(self,status):
        try:
            reStatus = self.cnEnde.is_float(status)
            selem = self.getElem.find_element_with_wait('id',self.SEARCH_USER_STATUS)
            self.selectElem.select_element_by_value(selem,str(reStatus))
            
        except Exception as e:
            print ("search by user status is error: ") + str(e)

    '''点击检索按钮'''     
    def click_search_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.SEARCH_BUTTON))).click()
        except Exception as e:
            print ("search button is error: ") + str(e)

    u'''点击重置按钮'''
    def click_reset_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.RESRT_BUTTON))).click()
        except Exception as e:
            print ("click reset button error: ") + str(e)

    u'''每页选择全部'''
    def page_select_all(self):
        try:
            
            self.frameElem.switch_to_content()
            self.frameElem.switch_to_main()
            
            #选择每页显示全部
            selem =  self.getElem.find_element_with_wait('id','page_select')
            self.selectElem.select_element_by_value(selem,'2000')
            
        except Exception as e:
            print ("page select all error: ") + str(e)

    u'''获取行数'''
    def get_rows(self):
        try:
            self.page_select_all()
            table_xpath = "//table[@id='content_table']"
            rows = self.tableElem.get_table_rows_count(table_xpath)
            return rows
        except Exception as e:
            print ("get tables row error: ") + str(e)

    u'''保存按钮'''
    def save_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.SAVE_BUTTON))).click()
        except Exception as e:
            print ("user save button error: ") + str(e)

    u'''点击全选按钮'''
    def select_all_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.SELECT_ALL_BUTTON))).click()
        except Exception as e:
            print ("select all button error: ") + str(e)
    
    u'''点击角色信息'''
    def click_role_msg(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,self.ROLE_MEG_BUTTON))).click()
        except Exception as e:
            print ("user role message button error: ") + str(e)

    u'''选择角色
            parameters:
                text : 角色名称
    '''
    def set_user_role(self,text):
        try:
            select_elem = self.getElem.find_element_with_wait('id',self.ROLE_SELECTD_ELEM)
            self.selectElem.select_element_by_visible_text(select_elem,str(text))
        except Exception as e:
            print ("select role option error: ") + str(e)
    
    u'''角色添加按钮'''
    def click_role_add_button(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.ROLE_ADD_BUTTON))).click()
        except Exception as e:
            print ("role add button error: ") + str(e)

    u'''点击用户操作列对应的按钮
        parameters:
            account : 用户账号
            index : 操作功能按钮对应的input位置
    '''
    def user_operate_list(self,account,index):
        row = self.cmf.find_row_by_name(account, "fortUserAccount")
        update_xpath = "//table[@id='content_table']/tbody/tr[" + str(row) + "]/td[9]/input[" + index + "]"
        self.getElem.find_element_wait_and_click("xpath", update_xpath)


    u'''点击用户操作列对应的编辑按钮
        parameters:
            account : 用户账号
    '''
    def operate_edit(self,account):
        try:
            self.user_operate_list(account,"1")
        except Exception:
            print("Click user operation edit button fail")


    u'''点击用户操作列对应的角色按钮
        parameters:
            account : 用户账号
    '''    
    def operate_role(self,account):
        try:
           self.user_operate_list(account,"2")
        except Exception:
            print("Click user operation role button fail")

    u'''点击用户操作列对应的证书按钮
        parameters:
            account : 用户账号
    '''     
    def operate_cert(self,account):
        try:
            self.user_operate_list(account,"3")
        except Exception:
            print("Click user operation cert button fail")

    u'''点击用户操作列对应的删除按钮
        parameters:
            account : 用户账号
    '''     
    def operate_delete(self,account):
        try:
            self.user_operate_list(account,"4")
        except Exception:
            print("Click user operation delete button fail")

    u'''填写变量内容
        parameters:
            var_text : 变量内容
            *locator : 定位方式
    '''      
    def set_common_func(self,var_text,locator):
        try:
            self.frameElem.from_frame_to_otherFrame("mainFrame")
            revar_text = self.cnEnde.is_float(var_text)
            var_elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,locator)))
            var_elem.clear()
            var_elem.send_keys(revar_text)
        except Exception as e:
            print ("set user common text error: ") + str(revar_text) + str(e)


    u'''填写用户账号
        parameters:
            account : 用户账号
    '''      
    def set_user_account(self,account):
        self.set_common_func(account,self.USER_ACCOUNT)

    u'''填写用户名称
        parameters:
            name : 用户名称
    '''     
    def set_user_name(self,name):
        self.set_common_func(name,self.USER_NAME)
        
#        rename = self.cnEnde.cnCode(name)
#        self.set_common_func(name,self.USER_NAME)

    u'''设置开始时间
        parameters:
            startTime : 开始时间
    '''    
    def set_start_time(self,startTime):
        try:
            start_time_js = "$('input[id=fortStartTime]').attr('readonly',false)"
            self.driver.execute_script(start_time_js)
        except Exception as e:
            print ("start_time js execute error: ") + str(e)
            
        self.set_common_func(startTime,self.USER_START_TIME)

    u'''设置结束时间
        parameters:
            endTime : 结束时间
    '''      
    def set_end_time(self,endTime):
        try:
            end_time_js = "$('input[id=fortEndTime]').attr('readonly',false)"
            self.driver.execute_script(end_time_js)           
        except Exception as e:
            print ("set endTime error: ") + str(e)
        
        self.set_common_func(endTime,self.USER_END_TIME)

    u'''设置用户状态
        parameters:
            value : 0代表锁定,1代表正常
    '''          
    def set_user_status(self,statusValue):
        self.set_common_rule(statusValue,self.USER_STATUS)

    u'''设置部门
        parameters:
            dep : 部门
    '''     
    def set_dep(self,dep):
        try:
            redep = self.cnEnde.cnCode(dep)
            #设置为false
            js = "$('input[id=department_name]').attr('readonly',false)"
            self.driver.execute_script(js)
            self.getElem.find_element_with_wait('id',self.USER_DEP).clear()
            self.getElem.find_element_wait_and_sendkeys('id',self.USER_DEP,dep)            
        except Exception as e:
            print ("set user department error: ") + str(e)

    u'''清空部门'''
    def clear_dep(self):
        self.getElem.find_element_wait_and_click("id", self.USER_DEP)
        self.getElem.find_element_wait_and_click("id", self.DEP_CLEAR)

    u'''勾选登录时修改'''
    def set_login_selectd(self):
        try:
            checkbox = self.getElem.find_element_with_wait('id',self.LOGIN_MODEY)
            if checkbox.is_selected() == False:
                checkbox.click()
        except Exception as e:
            print ("set login selected error: ") + str(e)

    u'''填写口令
        parameters:
            pwd : 用户口令
    '''  
    def set_user_pwd(self,pwd):
        return self.set_common_func(pwd,self.USER_PWD)

    u'''填写确认口令
        parameters:
            pwd : 确认口令
    '''      
    def set_user_enquire_pwd(self,repwd_):
        return self.set_common_func(repwd_,self.USER_RE_PWD)

    u'''填写手机号
        parameters:
            mobile : 手机
    '''
    def set_user_mobile(self,mobile):
       return self.set_common_func(mobile,self.USER_MOBILE)

    u'''填写电话
        parameters:
            phone : 电话
    '''        
    def set_user_phone(self,phone):
        return self.set_common_func(phone,self.USER_PHONE)

    u'''勾选审计查看审批管理员'''
    def set_audit_admin_selectd(self):
        try:
            checkbox = self.getElem.find_element_with_wait('id',self.IS_APPROVAL)
            if checkbox.is_selected() == False:
                checkbox.click()
        except Exception as e:
            print ("select audit admin error: ") + str(e)

    u'''填写邮箱
        parameters:
            email : 邮箱
    '''      
    def set_user_email(self,email):
        return self.set_common_func(email,self.USER_EMAIL)

    u'''填写地址
        parameters:
            address : 地址
    '''        
    def set_user_address(self,address):
        return self.set_common_func(address,self.USER_ADDRESS)

    u'''点击高级选项'''
    def click_advanced_option(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID,self.ADVANCED_OPTIONS))).click()
        except Exception as e:
            print ("click advanced options error: ") + str(e)
    
    u'''访问方式通用方法
            parameter:
                var_value : 访问方式value值
                locator : ID值
    '''
    def set_common_rule(self,var_value,locator):
        try:
            revar_value = self.cnEnde.is_float(var_value)
            select_elem = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,locator)))
            self.selectElem.select_element_by_value(select_elem,str(revar_value))
        except Exception as e:
            print ("set common access rule error: ") + str(revar_value) + str(e)

    u'''设置时间访问规则
            parameter:
                timeValue : 时间规则option的value值(-1代表请选择)
    '''
    def set_time_access_rule(self,timeValue):
        return self.set_common_rule(timeValue,self.TIME_RULE)

    u'''设置地址访问规则
            parameter:
                addressValue : 地址规则option的value值(-1代表请选择)
    '''    
    def set_address_access_rule(self,addressValue):
        return self.set_common_rule(addressValue,self.ADDRESS_RULE)

    u'''设置访问方式
            parameter:
                loginValue : 访问方式option的value值(2代表默认)
    '''    
    def set_auth_method_rule(self,loginValue):
        return self.set_common_rule(loginValue,self.AUTH_CODE)

    u'''填写AD域用户
            parameter:
                adUser : AD域用户名称
    '''        
    def set_ad_name(self,adUser):
        return self.set_common_func(adUser,self.USER_DOMAIN_ACCOUNT)

    u'''填写RADIUS用户
            parameter:
                radiusUser : RADIUS用户名称
    '''        
    def set_radius_name(self,radiusUser):
        return self.set_common_func(radiusUser,self.USER_RADIUS)   

    u'''切换模块
            parameter:
                levelText1 : 一级模块名称
                levelText2 : 二级模块名称
    '''     
    def switch_to_moudle(self,levelText1,levelText2):
        self.frameElem.switch_to_content()
        self.frameElem.switch_to_top()
        
        self.cmf.select_menu(levelText1)
        self.cmf.select_menu(levelText1,levelText2)

    u'''点击角色添加页面确定按钮'''
    def click_ok_button(self):
    	self.driver.switch_to_default_content()
        ok_button_xpath = "/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button"
    	self.getElem.find_element_wait_and_click_EC("xpath",ok_button_xpath,5)
    

    u'''添加系统级角色
            parameter : 
                list : 角色数据列表
    '''
    def add_sys_role(self,list):
        self.switch_to_moudle(u'角色管理',u'角色定义')
        self.role.add()
        self.role.edit_rolename(list[0])
        self.role.edit_shortname(list[1])
        self.role.select_sysrole()
        self.role.save_button()
        self.click_ok_button()

    u'''添加部门级角色
            parameter : 
                list : 角色列表数据
    '''    
    def add_dep_role(self,list):
        self.role.add()
        self.role.edit_rolename(list[0])
        self.role.edit_shortname(list[1])
        self.role.select_sysrole()
        self.role.save_button()
        self.click_ok_button()

    u'''初始化用户登录'''
    def user_login(self):
        data_path = self.dataFile.get_person_test_data_url()
        login_data = self.dataFile.get_data(data_path,'login')
        logindata = login_data[1]
        login = loginPage(self.driver)
        login.login(logindata)
    
    u'''切换至mainFrame'''
    def switch_to_main_frame(self):
        self.frameElem.switch_to_content()
        self.frameElem.switch_to_main()        

    u'''通过用户状态获取行数
            parameters:
                value : 开关value值(switch_on:关,switch_off:开)
    '''
    def search_by_status(self,value):
        self.switch_to_main_frame()
        
        row = 0
        try:
            self.page_select_all()
            
            #获取所有行的用户开关状态
            switchs = self.driver.find_elements_by_id("btn_qh")
            for switch in switchs:
                if switch.get_attribute('class') == value:
                    row = row + 1
            return row
        except Exception as e:
            print ("No users switch status is ") + str(value) + str(e)

    u'''通过用户账号或名称获取行数
            parameters:
                accountName : 账号或名称
    '''    
    def search_direct_by_account_or_name(self,accountName):
        self.switch_to_main_frame()

        row = 0
        reName = self.cnEnde.cnCode(accountName)
        try:
            self.page_select_all()

            #查找name属性为fortUserAccount的所有元素
            account_elems = self.driver.find_elements_by_name("fortUserAccount")
            
            #查找name属性为fortUserName的所有元素
            username_elems = self.driver.find_elements_by_name("fortUserName")
            
#            list1 = list(set(account_elems).union(set(username_elems)))
            for index in range(len(account_elems)):
                accountValue_text = account_elems[index].text
                nameValue_text = username_elems[index].text
                
                if (accountValue_text == accountName) or (nameValue_text == accountName):
                    row = row + 1
            return row
        except Exception as e:
            print ("No users accountOrName is ") + str(reName) + str(e)

    u'''通过部门获取行数
            parameters:
                dep : 部门名称
    '''      
    def search_direct_by_dep(self,dep):
        self.switch_to_main_frame()
        
        row = 0
        redep = self.cnEnde.cnCode(dep)
        try:
            self.page_select_all()
            
            text_list = self.driver.find_elements_by_name("fortDepartmentName")
            for fortDepValue in text_list:
                fortDepValue_text = fortDepValue.text
                if fortDepValue_text == dep:
                    row = row + 1
        except Exception:
            print redep + "is not exsit."
        return row

    u'''通过角色名称获取行数
            parameters:
                roleName :角色名称
    '''          
    def search_direct_by_role(self,roleName):
        self.switch_to_main_frame()
        
        row = 0
        reRole = self.cnEnde.cnCode(roleName)
        try:
            self.page_select_all()
            role_list = self.driver.find_elements_by_class_name("js_k")
            for role in role_list:
                if roleName in role.get_attribute('title') :
                    row = row + 1
            return row
        except Exception as e:
            print ("NO users role is ") + str(reRole) + str(e)

    #证书相关---------------------------------------------------------------
    u'''生成证书'''
    def create_cert(self):
        self.switch_to_main_frame()
        
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.CREATE_CERT))).click()
            
        except Exception as e:
            print ("click create button error: ") + str(e)

    u'''删除证书'''
    def delete_cert(self):
        try:
            WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.ID, self.DELETE_CERT))).click()
            
        except Exception as e:
            print ("click delete cert button error: ") + str(e)
    
    u'''获取证书指定属性的内容
            parameters:
                locator ： ID值
    '''
    def get_cert_var_text(self,locator):
        try:    
            cert_var_text = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,locator))).text
            return cert_var_text
        
        except Exception as e:
            print ("Get cert var text error: ") + str(cert_var_text) + str(e)        

    u'''获取生成的证书名字'''
    def get_cert(self):
        self.get_cert_var_text(self.CERT_NAME)

    u'''获取初始证书名字'''
    def get_init_cert_name(self):
        
        return self.get_cert_var_text(self.INIT_CERT_NAME)

    u'''获取证书序列号'''
    def get_cert_serial_num(self):
        self.get_cert_var_text(self.CERT_SERIAL_NUM)

    u'''点击返回按钮'''
    def click_back_button(self):
        try:
            self.switch_to_main_frame()
            
            back_xpath = "//html/body/form/div/div[4]/input[@id='history_skip']"
            self.getElem.find_element_wait_and_click('xpath',back_xpath)
        except Exception:
            print("Click the return button to fail")

    u'''添加用户
            parameters:
                data : 用户列表数据
    '''
    def add_user_with_role(self,data):
        self.switch_to_moudle(u"运维管理",u"用户")				
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.add_button()
        self.set_user_account(data[3])
        self.set_user_name(data[1])
        self.set_user_pwd(data[4])
        self.set_user_enquire_pwd(data[5])
        
        #点击角色信息按钮
        self.click_role_msg()
        self.set_user_role(data[6])
        self.click_role_add_button()                 
        self.save_button()
        self.cmf.click_login_msg_button()

           
        
                
            
                
                
        

#if __name__ == "__main__":
#    driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
#    selectElem = selectElement(driver)
    
#    list_sys = [u'系统管理员',u'系统']
#    list_dep = [u'部门管理员',u'部管']
#    dataFile = dataFileName()
#    file_path = dataFile.get_person_test_data_url()
#    login_data = dataFile.get_data(file_path,'login')
#    logindata = login_data[1]
#    login = loginPage(driver)
#    login.login(logindata)    
#    self.frameElem.switch_to_content()
#    self.frameElem.switch_to_top()
#    self.cmf.select_menu(u"角色管理")
#    self.cmf.select_menu(u"角色管理",u"角色定义")    
#    userElem =  UserPage(driver)
#    userElem.set_start_time("2016-02-93 12:34:23")
#    userElem.switch_to_role_moudle()
#    userElem.add_sys_role(list_sys)
##