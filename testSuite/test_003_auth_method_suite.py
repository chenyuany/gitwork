#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入认证
sys.path.append("/testIsomp/testCase/auth_method")
from test_auth_method import *

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)        
        self.authMethod = testAuthMethod(self.browser)
        
        #初始化用户登录
        self.commonSuite.isomper_login()
        
        #添加角色
        self.commonSuite.add_sys_role()
        self.commonSuite.add_dep_role()

        #添加用户
        self.commonSuite.add_user_with_role()
        
        #初始化用户退出
        self.commonSuite.user_quit()
        
        #使用添加的用户登录并切换至系统管理员角色
        self.commonSuite.login_and_switch_to_sys()
        
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
        self.commonSuite.user_quit()
        #初始化用户登录添加用户  
        self.commonSuite.isomper_login()    
        self.commonSuite.del_role()
        self.commonSuite.del_user()
        
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
