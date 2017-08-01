#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _icommon import commonFun

sys.path.append("/testIsomp/testCase/authorization/")
from test_authorization import testAuthorization

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

sys.path.append("/testIsomp/testSuite")
from common_suite_file import CommonSuiteData,setDriver

import unittest

class testAuthSuite(unittest.TestCase):
    def setUp(self):
        #定义驱动
        self.browser = setDriver().set_driver()

        self.commonSuite = CommonSuiteData(self.browser)
        self.authCase = testAuthorization(self.browser)
#        self.commonSuite.login_and_switch_to_dep()
#        self.commonSuite.switch_to_moudle(u'运维管理',u'授权')
        self.commonSuite.authori_module_prefix_condition()
        '''
        #初始化用户登录
        self.commonSuite.isomper_login()
        
        #添加角色
        self.commonSuite.add_sys_role()
        self.commonSuite.add_dep_role()
        #添加用户
        self.commonSuite.add_user_with_role()
        #添加授权用户
        self.commonSuite.add_authorization_user()
        self.commonSuite.user_quit()

        #使用添加的用户登录
        self.commonSuite.login_and_switch_to_dep()

        self.commonSuite.switch_to_moudle(u'运维管理',u'授权')
        '''
    def test_authori(self):
        #添加用户和资源类型的授权
        self.authCase.add_user_and_res_auth_001()
        #添加用户和资源组类型的授权
        self.authCase.add_user_and_res_group_auth_002()
        #添加用户和资源账号类型的授权
        self.authCase.add_user_and_res_account_auth_003()
        #添加用户组和资源类型的授权
        self.authCase.add_user_group_and_res_auth_004()
        #添加用户组和资源组类型的授权
        self.authCase.add_user_group_and_res_group_auth_005()
        #添加用户组和资源账号类型的授权   
        self.authCase.add_user_group_and_res_account_auth_006()
        #修改授权名称
        self.authCase.edit_auth_name_007()
        #授权校验
        self.authCase.auth_checkout_008()
        #授权检索
        self.authCase.auth_query_009()

        #添加访问审批
        self.authCase.Opt_access_approvel_011()
        #双人授权
        self.authCase.add_double_approvel_012()
        #删除授权
        self.authCase.auth_del_010()
    
    def tearDown(self):
        self.commonSuite.authori_module_post_condition()
#        self.commonSuite.user_quit()
        #初始化用户登录
#        self.commonSuite.isomper_login()   
#        self.commonSuite.del_role()
#        self.commonSuite.del_user()
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()

