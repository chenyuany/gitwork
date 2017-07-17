#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _icommon import getElement,selectElement,frameElement,commonFun
from _initDriver import initDriver
from _globalVal import globalValue

sys.path.append("/testIsomp/webElement/auth_method/")
from authMethodElement import AuthMethodPage

sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role

#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

class setDriver():
   
    u'''本地驱动'''
    def set_local_driver(self):
        driver = initDriver().open_driver()
        return driver

    u'''远程驱动'''
    def set_remote_driver(self):
        driver_lists = globalValue().get_value()
        driver = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        
#        driver = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","firefox")
        return driver
    

class CommonSuiteData():
    
    def __init__(self,driver):
        self.driver = driver
        self.dataFile = dataFileName()
        self.cmf = commonFun(self.driver)
        self.initDriver = initDriver()
        self.loginElem = loginPage(self.driver)
        self.roleElem = Role(self.driver)
        self.userElem = UserPage(self.driver)
        self.frameElem = frameElement(self.driver)
        self.authElem = AuthMethodPage(self.driver)

    u'''切换模块
            parameter:
                levelText1 : 一级模块名称
                levelText2 : 二级模块名称
    '''     
    def switch_to_moudle(self,levelText1,levelText2):
        self.frameElem.from_frame_to_otherFrame("topFrame")
        
        self.cmf.select_menu(levelText1)
        self.cmf.select_menu(levelText1,levelText2)
    

#-----------------------------------角色相关----------------------------------        
    u'''填写角色基本信息'''
    def set_role_basic_info(self,list):
        self.switch_to_moudle(u'角色管理',u'角色定义')
        self.roleElem.add()
        self.roleElem.edit_rolename(list[0])
        self.roleElem.edit_shortname(list[1])
        
        
    u'''系统级角色模板
            parameter : 
                list : 角色数据列表
    '''
    def set_sys_role(self,list):
        self.set_role_basic_info(list)
        self.roleElem.select_sysrole()
        self.roleElem.save_button()
        self.roleElem.click_ok_button()
    
    u'''部门级角色模板
            parameter : 
                list : 角色列表数据
    '''    
    def set_dep_role(self,list):
        self.set_role_basic_info(list)
        self.roleElem.select_sysrole()
        self.roleElem.save_button()
        self.roleElem.click_ok_button()
    
    u'''删除角色'''
    def del_role(self):
        self.switch_to_moudle(u'角色管理',u'角色定义')
        self.cmf.check_all()
        self.cmf.bulkdel("delete_role")
        self.roleElem.click_ok_button()

#----------------------------------------用户相关------------------------------
    u'''填写用户基本信息
            parameters:
                data : 用户列表数据
    '''
    def set_user_basic_info(self,data):
        self.switch_to_moudle(u"运维管理",u"用户")				
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.add_button()
        self.userElem.set_user_account(data[3])
        self.userElem.set_user_name(data[1])
        self.userElem.set_user_pwd(data[4])
        self.userElem.set_user_enquire_pwd(data[5])
        self.userElem.set_start_time(data[6])
        
        #设置访问方式
        self.userElem.click_advanced_option()
        self.userElem.set_auth_method_rule(data[7])
        
        #访问方式不是默认方式
        if int(data[7]) != 2:
            self.userElem.set_ad_name(data[8])
        self.userElem.save_button()
        self.cmf.click_login_msg_button()
    
    u'''为用户设置角色
            parameters :
                data : 用户角色数据
    '''
    def set_user_role(self,roleText):
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.click_role_msg()
        roleList = roleText.split(',')
        for roleName in roleList:
            self.userElem.set_common_select_elem_by_text(roleName,"Roles")
        #判断角色是否为空
        if roleText != "":
            self.userElem.click_role_add_button()
        self.userElem.save_button()
        self.cmf.click_login_msg_button()
    
    

    u'''删除用户'''
    def del_user(self):
        self.switch_to_moudle(u"运维管理",u"用户")
        self.frameElem.from_frame_to_otherFrame("mainFrame")
        self.userElem.select_all_button()
        self.userElem.del_button()
        self.cmf.click_login_msg_button()
    
#-----------------------------通用数据---------------------------------------
    u'''获取数据
        Parameters:
            - sheetname:sheet名称
            return：表格数据
    '''
    def get_table_data(self,sheetname):
        filePath = self.dataFile.get_common_suite_test_data_url()
        fileData = self.dataFile.get_data(filePath,sheetname)
        return fileData

    u'''初始化用户登录'''
    def isomper_login(self):
        login_data = self.get_table_data('isomper')
        logindata = login_data[1]
        self.loginElem.login(logindata)
    
    u'''添加系统级角色'''    
    def add_sys_role(self):
        role_data = self.get_table_data("add_role")
        roleData = role_data[1]
        self.set_sys_role(roleData)
    
    u'''添加部门级角色'''    
    def add_dep_role(self):
        role_data = self.get_table_data("add_role")
        roleData = role_data[2]
        self.set_dep_role(roleData)
    
        
    u'''添加系统管理员和部门管理员的用户'''
    def add_user_with_role(self):
        user_data = self.get_table_data("common_user")
        userData = user_data[1]
        self.set_user_basic_info(userData)
        self.set_user_role(userData[9])
        
    def login_and_switch_to_common(self):
        login_data = self.get_table_data("common_user")
        logindata = login_data[1]
        self.loginElem.login(logindata)
        #获取角色
        roleList = logindata[9].split(',')
#        print roleList[0],roleList[1]
        return roleList

    u'''使用添加的用户登录并切换至系统级角色'''
    def login_and_switch_to_sys(self):
        roleList = self.login_and_switch_to_common()
        self.cmf.select_role_by_text(roleList[0])
    
    u'''使用添加的用户登录并切换至部门级角色'''
    def login_and_switch_to_dep(self):
        roleList = self.login_and_switch_to_common()
        self.cmf.select_role_by_text(roleList[1])
    
    def user_quit(self):
        self.loginElem.quit()
    
    
    u'''添加认证配置'''
    def add_meth_method(self):
        meth_data = self.get_table_data("meth_method")
        methData = meth_data[1]
        
        self.switch_to_moudle(u"策略配置",u"认证强度")
        
        self.authElem.select_all_auth(methData)
    
    u'''会话配置,设置最大登录数'''
    def set_login_max_num(self):
        self.loginElem.set_max_login_count()
    
    u'''添加登录测试用户'''
    def add_login_data(self):
        user_data = self.get_table_data("add_login_data")
        for dataRow in range(len(user_data)):
            data = user_data[dataRow]
            if dataRow != 0:
                self.set_user_basic_info(data)
#                self.userElem.click_back_button()
    
    def user_quit(self):
        self.loginElem.quit()
        
if __name__ == "__main__":
    driver = setDriver().set_local_driver()
    commonDataElem =  CommonSuiteData(driver)
    commonDataElem.isomper_login()
#    commonDataElem.add_sys_role()
#    commonDataElem.add_dep_role()
    commonDataElem.add_login_data()
#    commonDataElem.add_user_with_role()
#    commonDataElem.user_quit()
#    commonDataElem.login_and_switch_to_sys()
#    commonDataElem.add_meth_method()
#    commonDataElem.set_login_max_num()
