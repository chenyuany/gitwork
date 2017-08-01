#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入登录
sys.path.append("/testIsomp/testCase/login")
from test_login import *

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testLoginSuite(unittest.TestCase):
    def setUp(self):
        
        #定义驱动
        self.browser = setDriver().set_driver()
        self.commonSuite = CommonSuiteData(self.browser)
        self.userElem = UserPage(self.browser)
        
        self.commonSuite.login_module_prefix_condition()
        '''
        #初始化用户登录
        self.commonSuite.isomper_login()
        
        #添加角色
        self.commonSuite.add_sys_role()
        self.commonSuite.add_dep_role()
        
        #添加用户
        self.commonSuite.add_user_with_role()
        #初始化用户退出
        self.commonSuite.user_quit()
        
        #使用添加的用户登录
        self.commonSuite.login_and_switch_to_sys()
        #配置认证方式
        self.commonSuite.add_meth_method()
        #配置最大登录数
        self.commonSuite.set_login_max_num()
        
        #添加登录用户数据
        self.commonSuite.add_login_data()
        #改变a的状态为关
        self.userElem.change_user_status_off("a")
        self.commonSuite.user_quit()
        '''

    def test_login(self):
        test_login = testLogin(self.browser)
        #登录
        test_login.login()
    
    def tearDown(self):
        self.commonSuite.login_module_post_condition()
        '''
        self.commonSuite.isomper_login()
        #删除角色     
        self.commonSuite.del_role()
        #删除用户
        self.commonSuite.del_user()
        '''       
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()
