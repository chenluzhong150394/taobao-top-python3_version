'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class WlbInventorySyncRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_id = None
		self.item_type = None
		self.quantity = None

	def getapiname(self):
		return 'taobao.wlb.inventory.sync'
