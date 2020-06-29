'''
Created by auto_sdk on 2020.02.20
'''
from top.api.base import RestApi
class TbkPrivilegeGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.adzone_id = None
		self.item_id = None
		self.me = None
		self.platform = None
		self.relation_id = None
		self.site_id = None

	def getapiname(self):
		return 'taobao.tbk.privilege.get'
