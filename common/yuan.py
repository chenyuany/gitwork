#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：
#模块描述：
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from _initDriver import initDriver
from _icommon import getElement,selectElement,frameElement,commonFun,tableElement

sys.path.append("/testIsomp/webElement/role/")
from test_roledf import Role
sys.path.append("/testIsomp/testCase/role/")
from test_role import testRole
import time

browers=initDriver().open_driver()
getElem = getElement(browers)
selectElem = selectElement(browers)
frameElem =frameElement(browers)
tableElem=tableElement(browers)
role = Role(browers)
testrole=testRole(browers)
common=commonFun(browers)
time.sleep(1)
a = getElem.find_element_with_wait("id", "loginMethod")
selectElem.select_element_by_index(a, 0)
getElem.find_element_wait_and_sendkeys("id", "username", "isomper")
getElem.find_element_wait_and_sendkeys("id", "pwd", "1")
getElem.find_element_wait_and_click("id","do_login")
frameElem.switch_to_content()
frameElem.switch_to_top()
getElem.find_element_wait_and_click("link",u"角色管理")
getElem.find_element_wait_and_click("link",u"角色定义")
testrole.add_sysrole_001()
testrole.add_dptrole_002()
testrole.edit_role_003()
testrole.edit_managerole_004()
testrole.check_other_role()
testrole.edit_otherrole_005()
testrole.check_rolename()
testrole.check_shortname()
testrole.check_bulkdel()
testrole.del_role_006()
testrole.bulkdel_role_007()
# role.add_system_role_001(u"系统管理员",u"系统")
# role.add_depart_role_002(u"部门管理员",u"部门")
# role.edit_role_003(u"系统管理员",u"超级管理员")
# role.edit_managed_role_004(u"超级管理员",0)
# role.edit_other_role_005(u"超级管理员",0)
# role.del_role_006(u"超级管理员")
# role.bulkdel_role_007()
# role.add_system_role_001(u"系统管理员",u"系统")
# role.checkout_rolename("")
# role.checkout_rolename(u"!@#")
# role.checkout_shortname(u"系统管理员", "")
# role.checkout_shortname(u"系统管理员", u"!@#")
# role.checkout_shortname(u"系统管理员", u"系统管理员")
# role.checkout_shortname(u"执行管理员", u"系统")
# role.checkout_shortname(u"系统管理员", u"系")
# role.checkout_shortname(u"系统管理员", u"系统")
# role.checkout_no_menu(u"系统管理员", u"系统")
# role.checkout_other(u"系统管理员", 0,1)
# role.checkout_other(u"系统管理员", 1,0)
# role.is_rolename_exsit(u"系统管理员")
# frameElem.switch_to_content()
# frameElem.switch_to_main()
# frameElem.from_frame_to_otherFrame("mainFrame")
# # getElem.find_element_wait_and_click("id","add_role")
# tableElem.get_table_rows("/html/body/form/div/div[6]/div[1]/table")
# yu=tableElem.get_table_cell_text("/html/body/form/div/div[6]/div[1]/table",2,2)
# print(yu)
# tableElem.get_table_rows_count()
# tableElem.get_table_td_select()
initDriver().close_driver(browers)
