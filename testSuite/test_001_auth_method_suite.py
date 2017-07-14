#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _globalVal import globalValue
from _icommon import getElement,selectElement,frameElement
#导入认证
sys.path.append("/testIsomp/testCase/auth_method")
from test_auth_method import *
#导入登录
sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):#internet explorer
#        self.browser = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
        driver_lists = globalValue().get_value()
        self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        self.authMethod = testAuthMethod(self.browser)
        self.userElem = UserPage(self.browser)
        self.loginPage = loginPage(self.browser)
        #初始化用户登录添加用户
        login_data = self.authMethod.get_table_data("login")
        login_data = login_data[1]
        self.loginPage.login(login_data)
        #获取添加用户和角色的数据
        add_data = self.authMethod.get_table_data("add_user")
        #添加角色
        role_data = add_data[2]
        self.userElem.add_sys_role(role_data)
        #添加用户
        user_data = add_data[1]
        self.userElem.add_user_with_role(user_data)
        self.loginPage.quit()
        #使用添加的用户的登录
        loginPage(self.browser).login(user_data)
        frameElement(self.browser).switch_to_content()
        frameElement(self.browser).switch_to_top()
        #切换到系统管理员角色
        commonFun(self.browser).select_role_by_text(user_data[6])
        commonFun(self.browser).select_menu(u"策略配置")
        commonFun(self.browser).select_menu(u"策略配置",u"认证强度")
        frameElement(self.browser).from_frame_to_otherFrame("mainFrame")        
    
    def test_auth_method(self):
        #添加AD域认证方式
        self.authMethod.add_ad_method_001()
        #添加radius认证方式
        self.authMethod.add_radius_method_002()
        #添加AD域+口令认证方式
        self.authMethod.add_ad_and_pwd_method_003()
        #添加RADIUS+口令认证方式
        self.authMethod.add_radius_and_pwd_method_004()
        #添加数字证书认证方式
        self.authMethod.add_cert_method_005()
        #校验认证方式是否添加成功
        self.authMethod.auth_method_add_is_success_006()
        #修改AD域认证方式
        self.authMethod.mod_ad_method_007()
        #AD域认证方式校验
        self.authMethod.ad_method_checkout_008()
        #radius认证方式校验
        self.authMethod.radius_checkout_009()
        #删除多种认证方式
        self.authMethod.del_auth_method_010()

    def tearDown(self):
        self.loginPage.quit()
        #初始化用户登录添加用户  
        self.userElem.user_login()    
        self.userElem.del_role()
        self.userElem.del_user()
        
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
