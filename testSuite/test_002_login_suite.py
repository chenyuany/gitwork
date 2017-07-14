#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")

from _globalVal import globalValue

#导入登录
sys.path.append("/testIsomp/testCase/login")
from test_login import *

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsomp/testCase/auth_method")
from test_auth_method import testAuthMethod

sys.path.append("/testIsomp/webElement/auth_method/")
from authMethodElement import AuthMethodPage

sys.path.append("/testIsomp/webElement/login/")
from loginElement import loginPage

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        self.browser = initDriver().open_driver()
#        self.browser = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","chrome")
#         driver_lists = globalValue().get_value()
#         self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        self.authMethod = testAuthMethod(self.browser)
        self.authMethodElem = AuthMethodPage(self.browser)
        self.userElem = UserPage(self.browser)
        self.loginElem = loginPage(self.browser)
        
        #初始化用户登录
        self.userElem.user_login()
        #获取添加用户和角色的数据
        add_data = self.authMethod.get_table_data("add_user")
        #添加角色
        role_data = add_data[2]
        self.userElem.add_sys_role(role_data)
        #添加用户
        user_data = add_data[1]
        self.userElem.add_user_with_role(user_data)
        self.loginElem.quit()
        #使用添加的用户的登录
        self.authMethodElem.login_and_switch_auth_method()

        #配置认证方式
        self.authMethodElem.select_all_auth()
        
        #配置最大登录数
        self.loginElem.set_max_login_count()
        
        #添加登录用户
        self.userElem.add_login_data()
        #改变用户a状态为关闭
        self.userElem.change_user_status_off("a")
        self.loginElem.quit()
        
    def test_login(self):
        test_login = testLogin(self.browser)
        #登录
        test_login.login()
    
    def tearDown(self):
        self.userElem.user_login()
        #删除角色     
        self.userElem.del_role()
        #删除用户
        self.userElem.del_user()        
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
