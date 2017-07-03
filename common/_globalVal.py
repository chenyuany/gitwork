#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


sys.path.append("/testIsomp/common/")
from _transCoding import jsonTranscoding
from _initDriver import initDriver

class globalValue():
	def set_value(self,hostUrl,browerType):
		global host
		global brower
		global status
		host = hostUrl
		brower = browerType
		
	def get_value(self):
		return host,brower
	
#global_value().set_value("http://192.166.23.3:5555/wb/hub","chrome")
#print global_value().get_value()
#def set_value(host_url,brower_type):
#	global host
#	global brower
#	host = host_url
#	brower = brower_type
#	
#def get_value():
#	return host,brower
#