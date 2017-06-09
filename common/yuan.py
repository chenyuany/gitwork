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
from _initDriver import initDriver
from _icommon import *
browers=initDriver().open_driver()
getElem = getElement(browers)
selectElem = selectElement(browers)
frameElem =frameElement(browers)
tableElem=tableElement(browers)
common=commonFun(browers)
a = getElem.find_element_with_wait("id","loginMethod")
selectElem.select_element_by_index(a,0)
getElem.find_element_wait_and_sendkeys("id","username","a")
getElem.find_element_wait_and_sendkeys("id","pwd","1")
getElem.find_element_wait_and_click("id","do_login",5)
frameElem.switch_to_top()
common.select_role(1)
getElem.find_element_wait_and_click("link","角色管理")
getElem.find_element_wait_and_click("link","角色定义")
# frameElem.switch_to_content()
# frameElem.switch_to_main()
frameElem.from_frame_to_otherFrame("mainFrame")
tableElem.get_table_rows("/html/body/form/div/div[6]/div[1]/table")
yu=tableElem.get_table_cell_text("/html/body/form/div/div[6]/div[1]/table","2","2")
print(yu)
# tableElem.get_table_rows_count()
# tableElem.get_table_td_select()
initDriver().close_driver(browers)
