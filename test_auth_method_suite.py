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

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):#internet explorer
        # self.browser = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
       driver_lists = globalValue().get_value()
       self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
    
    def test_auth_method(self):
        self.authMethod = testAuthMethod(self.browser)
        login_data = self.authMethod.get_table_data("login")
        data = login_data[1]
        loginPage(self.browser).login(data)
        frameElement(self.browser).switch_to_content()
        frameElement(self.browser).switch_to_top()
        commonFun(self.browser).select_role(1)
        commonFun(self.browser).select_menu(u"策略配置")
        commonFun(self.browser).select_menu(u"策略配置",u"认证强度")
        frameElement(self.browser).from_frame_to_otherFrame("mainFrame")
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
        #修改AD域认证方式
        self.authMethod.mod_ad_method_006()
        #AD域认证方式校验
        self.authMethod.ad_method_checkout_007()
        #radius认证方式校验
        self.authMethod.radius_checkout_008()
        #删除一种认证方式
        self.authMethod.del_radius_auth_method_009()
        #删除多种认证方式
        self.authMethod.del_other_auth_method_010()
        
#    u'''添加AD域认证方式'''
#    def test_001_add_ad_method(self):
#        self.authMethod.add_ad_method_001()
    
#    u'''添加radius认证方式'''
#    def test_002_add_radius_method(self):
#        self.authMethod.add_radius_method_002()
#    
#    u'''添加AD域+口令认证方式'''
#    def test_003_add_ad_and_pwd_method(self):
#        self.authMethod.add_ad_and_pwd_method_003()
#
#    u'''添加radius+口令认证方式'''
#    def test_004_add_radius_and_pwd_method(self):
#        self.authMethod.add_radius_and_pwd_method_004()
#
#    u'''添加数字证书认证方式'''
#    def test_005_add_cert_method(self):
#        self.authMethod.add_cert_method_005()
#    
#    u'''修改AD域认证方式'''
#    def test_006_modey_ad_method(self):
#        self.authMethod.mod_ad_method_006()
#
#    u'''添加数字证书认证方式'''
#    def test_007_ad_method_checkout(self):
#        self.authMethod.ad_method_checkout_007()

#    u'''添加数字证书认证方式'''
#    def test_008_radius_checkout(self):
#        self.authMethod.radius_checkout_008()

#    u'''添加数字证书认证方式'''
#    def test_009_del_radius_method(self):
#        self.authMethod.del_radius_method_009()   

    def tearDown(self):
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
