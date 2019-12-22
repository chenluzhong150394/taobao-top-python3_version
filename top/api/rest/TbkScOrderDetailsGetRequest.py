'''
Created by auto_sdk on 2019.11.12
'''
from top.api.base import RestApi
class TbkScOrderDetailsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_time = None
		self.jump_type = None
		self.member_type = None
		self.order_scene = None
		self.page_no = None
		self.page_size = None
		self.position_index = None
		self.query_type = None
		self.start_time = None
		self.tk_status = None

	def getapiname(self):
		return 'taobao.tbk.sc.order.details.get'
