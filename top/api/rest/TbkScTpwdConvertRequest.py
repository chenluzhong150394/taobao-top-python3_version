'''
Created by auto_sdk on 2020.02.20
'''
from top.api.base import RestApi
class TbkScTpwdConvertRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.dx = None
		self.password_content = None
		self.site_id = None

	def getapiname(self):
		return 'taobao.tbk.sc.tpwd.convert'
