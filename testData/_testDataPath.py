#coding=utf-8
#设定excel数据文件名字，统一调用
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append("/testIsomp/common/")
from _excelRead import excelRead

#登陆excel数据文件
LOGIN_TEST_DATA_URL = "G:/test/testIsomp/testData/login_test_data.xlsx"

#自然人excel数据位置
PERSON_TEST_DATA_URL = "G:/test/testIsomp/testData/person_test_data.xlsx"

#unix资源excel数据位置
UNIX_TEST_DATA_URL = "G:/test/testIsomp/testData/unix_test_data.xlsx"

#unix资源账号excel数据位置
UNIX_USER_TEST_DATA_URL = "G:/test/testIsomp/testData/unix_user_test_data.xlsx"

#windows资源excel数据位置
RESOURCE_TEST_DATA_URL = "G:/test/testIsomp/testData/windows_test_data.xlsx"

#windows资源账号excel数据位置
RESOURCE_TEST_USER_DATA_URL = "G:/test/testIsomp/testData/windows_user_test_data.xlsx"

#网络设备local资源excel数据位置
LOCAL_TEST_DATA_URL = "G:/test/testIsomp/testData/local_test_data.xlsx"

#网络设备local资源账号excel数据位置
LOCAL_USER_TEST_DATA_URL = "G:/test/testIsomp/testData/local_user_test_data.xlsx"

#角色定义数据文件
ROLE_TEST_DATA_URL = "/testIsomp/testData/role_test_data.xlsx"

class dataFileName(object):

    def get_login_test_data_url(self):
        return LOGIN_TEST_DATA_URL
    
    #获取自然人excel中的数据
    def get_person_test_data_url(self):
        return PERSON_TEST_DATA_URL
    
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

    #从sheet名称获取登陆数据
    def get_data(self,dataPath,sheetName):
        #获取excel数据
        data = excelRead().get_excel_data(dataPath,sheetName)
        return data


#print dataFileName().getLogin_Test_Data()