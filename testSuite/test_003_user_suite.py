#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#导入驱动
sys.path.append("/testIsomp/common/")
from _initDriver import initDriver
from _globalVal import globalValue
from _icommon import getElement,selectElement,frameElement

sys.path.append("/testIsomp/webElement/user/")
from userElement import UserPage

sys.path.append("/testIsomp/testCase/user/")
from test_user import User

sys.path.append("/testIsomp/testData/")
from _testDataPath import dataFileName

import unittest

class testUserSuite(unittest.TestCase):
    def setUp(self):#internet explorer
        self.browser = initDriver().open_driver()
#        self.browser = initDriver().remote_open_driver("http://172.16.10.21:5555/wd/hub","firefox")
#         driver_lists = globalValue().get_value()
#         self.browser = initDriver().remote_open_driver(driver_lists[0],driver_lists[1])
        self.userElem = UserPage(self.browser)
        self.userCase = User(self.browser)
        self.dataFile = dataFileName()
        self.userElem.user_login()

        #添加角色
        data_path = self.dataFile.get_person_test_data_url()
        role_data = self.dataFile.get_data(data_path,'role')
        roledata = role_data[1]       
        self.userElem.add_sys_role(roledata)
        self.userElem.switch_to_moudle(u'运维管理',u'用户')
        

    def test_login(self):
        #添加用户
        self.userCase.add_user_001()
        #修改用户
        self.userCase.edit_user_002()
        #生成证书
        self.userCase.create_user_cert_003()
        #重新生成证书
        self.userCase.create_user_cert_again_003()
        #删除证书
        self.userCase.delete_user_cert_004()
        #用户校验    
        self.userCase.checkout_user_005()
        #用户检索
        self.userCase.search_user_by_username_006()
        self.userCase.search_user_by_status_006()
        self.userCase.search_user_by_dep_006()
        self.userCase.search_user_by_role_006()
        #删除单一用户
        self.userCase.del_user_007()
        #删除全部用户
        self.userCase.del_all_user_008()
    
    def tearDown(self):
        self.userElem.del_role()
#        self.userElem.del_user()   
        initDriver().close_driver(self.browser)

if __name__ == "__main__":
    unittest.main()

