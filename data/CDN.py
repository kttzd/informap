#!/usr/bin/python
# encoding: utf-8
import re
import sys
import json
import requests
from pprint import pprint 
from bs4 import BeautifulSoup
class cdn(object):
	def __init__(self,host=None):
		self.host=host
		self.result=None
		self.url="http://tool.17mon.cn/cdn.php"
		self.payload=dict(node="2",host=self.host) 
	def getCdn(self):
		try:
			r=requests.post(self.url,data=self.payload)
			get_result=BeautifulSoup(r.text).find_all('table', {'class' : "table table-striped table-bordered"})
			#获得 标题
			#print "1"
			m_a=re.findall(r'<th>(.*?)</th>',str(get_result[0]))
			#m_a  可能为 域名 IP CHAME 服务商
			#print m_a
			m_b=re.findall(r'(?isu)<td[^>]*>(.*?)</td>',str(get_result[0]),re.I|re.M)
			m_c=[]
			#print "3"
			for i in range(len(m_b)):
				info=m_b[i].strip().split("<br/>")
				for k in range(len(info)):
					test=info[k].strip()
					if re.findall(r'target="_blank">(.+?)</a>',test):
						m_c.append(re.findall(r'target="_blank">(.+?)</a>',test))
					else:
						m_c.append(test)
			services={}
			services[self.host]=m_c
			print json.dumps(services,encoding="UTF-8",ensure_ascii=False)
		except:
			pass
			print "something wrong"
if __name__=="__main__":
	listnum=['outside.vip.com', 'acs.vip.com', 'o.vip.com', 'mapi.vip.com', 'weixin-api.vip.com', 'pay.vip.com', 'sh-api.tms.vip.com', 'category.vip.com', 'qq.vip.com', 'crm.vip.com', 'www.ubb.vip.com', 'client.vip.com', 'n.myopen.vip.com', 'sc.vip.com', 'union.vip.com', 'pay-static.vip.com', 'img4.vip.com', 'tuan.vip.com', 'sapi.vip.com', 'ap.vip.com', 'weixin-static.vip.com', '400queue.vip.com', 'u.vip.com', 'fashion.vip.com', 's1.vip.com', 'img3.vip.com', 'wap.vip.com', 'img2.vip.com', 'ota.vip.com', 'clicks.emkt.vip.com', 'ir.vip.com', 'www.kkk.vip.com']	
	num=['www.kfc.com.cn', 'www.wap.kfc.com.cn', 'chitong1.kfc.com.cn', 'wap.kfc.com.cn', 'order.kfc.com.cn', 'zhaji.kfc.com.cn']
	num_test=["laifeng.com","pay.laifeng.com","www.laifeng.com","bbs.laifeng.com"]
	for host in num_test:

		h=cdn(host)
		h.getCdn()
	
