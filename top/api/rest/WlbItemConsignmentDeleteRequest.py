'''
Created by auto_sdk on 2013-06-03 16:32:57
'''
from top.api.base import RestApi
class WlbItemConsignmentDeleteRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ic_item_id = None
		self.owner_item_id = None
		self.rule_id = None

	def getapiname(self):
		return 'taobao.wlb.item.consignment.delete'
