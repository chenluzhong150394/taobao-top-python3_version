'''
Created by auto_sdk on 2019.07.04
'''
from top.api.base import RestApi
class TbkScPublisherInfoSaveRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.info_type = None
		self.inviter_code = None
		self.note = None
		self.offline_scene = None
		self.online_scene = None
		self.register_info = None
		self.relation_from = None

	def getapiname(self):
		return 'taobao.tbk.sc.publisher.info.save'
