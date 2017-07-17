#coding=utf-8
#设定excel数据文件名字，统一调用
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _excelRead import excelRead

#通用数据excel文件
COMMON_SUITE_TEST_DATA_URL = r"/testIsomp/testData/common_suite_test_data.xlsx"
#登陆excel数据文件
LOGIN_TEST_DATA_URL = r"/testIsomp/testData/login_test_data.xlsx"

#用户excel数据位置
USER_TEST_DATA_URL = r"/testIsomp/testData/user_test_data.xlsx"

#unix资源excel数据位置
UNIX_TEST_DATA_URL = r"/testIsomp/testData/unix_test_data.xlsx"

#unix资源账号excel数据位置
UNIX_USER_TEST_DATA_URL = "/testSimp/testData/unix_user_test_data.xlsx"

#windows资源excel数据位置
RESOURCE_TEST_DATA_URL = "/testSimp/testData/windows_test_data.xlsx"

#windows资源账号excel数据位置
RESOURCE_TEST_USER_DATA_URL = "/testSimp/testData/windows_user_test_data.xlsx"

#网络设备local资源excel数据位置
LOCAL_TEST_DATA_URL = "/testSimp/testData/local_test_data.xlsx"

#网络设备local资源账号excel数据位置
LOCAL_USER_TEST_DATA_URL = "/testIsomp/testData/local_user_test_data.xlsx"

#角色定义数据文件
ROLE_TEST_DATA_URL = r"/testIsomp/testData/role_test_data.xlsx"

#组织定义数据文件
DEPARTMENT_TEST_DATA_URL = r"/testIsomp/testData/department_test_data.xlsx"

#认证方式数据文件
AUTH_METHOD_TEST_DATA_URL = r"/testIsomp/testData/auth_method_test_data.xlsx"

class dataFileName(object):
    #获取通用excel中的数据
    def get_common_suite_test_data_url(self):
        return COMMON_SUITE_TEST_DATA_URL
    
    #获取用户登录excel中的数据
    def get_login_test_data_url(self):
        return LOGIN_TEST_DATA_URL
    
    #获取认证方式excel中的数据
    def get_auth_method_test_data_url(self):
       return AUTH_METHOD_TEST_DATA_URL 
    
    #获取用户excel中的数据
    def get_person_test_data_url(self):
        return USER_TEST_DATA_URL
    
    #获取unix资源excel中数据
    def get_unix_test_data_url(self):
        return UNIX_TEST_DATA_URL
    
    #获取unix资源账号excel数据位置
    def get_unix_user_test_data_url(self):
        return UNIX_USER_TEST_DATA_URL
    
    #获取网络设备local资源excel中的数据
    def get_local_test_data_url(self):
        return LOCAL_TEST_DATA_URL

    #获取资源excel中的数据
    def get_resource_test_data_url(self):
        return RESOURCE_TEST_DATA_URL
    
    #获取资源用户中excel中的数据
    def get_resource_test_user_data_url(self):
        return RESOURCE_TEST_USER_DATA_URL
    
    
    #获取网络设备local资源账号excel中的数据
    def get_local_user_test_data_url(self):
        return LOCAL_USER_TEST_DATA_URL

    u"""获取角色定义数据文件的数据"""
    def get_role_test_data_url(self):
        return ROLE_TEST_DATA_URL

    u"""获取组织定义部门文件的数据"""
    def get_depart_test_data_url(self):
        return DEPARTMENT_TEST_DATA_URL

    #从sheet名称获取登陆数据
    def get_data(self,dataPath,sheetName):
        #获取excel数据
        data = excelRead().get_excel_data(dataPath,sheetName)
        
        return data
    
#dataFile = dataFileName()
#login_data = dataFileName().get_data(dataFileName().get_auth_method_test_data_url(),'add_auth_method')
#for dataRow in range(len(login_data)):
#    data = login_data[dataRow]
#    print data
    