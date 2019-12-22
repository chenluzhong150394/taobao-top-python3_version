# -*- coding: utf-8 -*-
import top.api
import json




req = top.api.TbkScOrderDetailsGetRequest()
req.set_app_info(top.appinfo(‘appkey’, ‘sercert’))

req.query_type = 1
req.position_index = "2222_334666"
req.page_size = 20
req.member_type = 2
req.tk_status = 12
req.end_time = "2019-12-19 13:00:00"
req.start_time ="2019-12-19 10:00:00"
req.jump_type = 1
req.page_no = 1
req.order_scene = 1
try:
    resp = req.getResponse('session')
    print(resp)
except Exception as e:
    print(e)

