#!/usr/bin/python
#coding:utf-8
import sys
import httplib2
import futures
import requests
import json
import socket
import os
from getSub import SubDomains
from libnmap.process import NmapProcess
from libnmap.parser import NmapParser,NmapParserException
class scan(object):
	def __init__(self,host=None,ip=None):
		super(scan,self).__init__()
		self.host=host
		self.ip=socket.gethostbyname(self.host) #单独调用调用类本身的参数
		#self.domains
	def getFromChinaZ(self,ip=None):   #ip反查接口  然后列表
		try:
			if ip==None:
				ip=self.ip
			r=requests.get("http://dns.aizhan.com/index.php?r=index/domains&ip=%s&page=%d"%(ip,1)) #ip
			hosts=[]
			hosts=r.json()["domains"]
			return hosts
			#print hosts
		except:
			return []
	def getSubDomains(self,Sub=None):
		services={}
		try:
			if Sub==None:
				Sub=self.host
			subdomains=SubDomains(Sub)
			utf8,token=subdomains.get_token()
			subdomains.get_submains(token,utf8)
			hosts=subdomains.result()["data"]
			services['ip']=hosts['ip']
			services['subdomains']=hosts['subdomains']
			return services
		except Exception,e:
			print "Exception",e
			return {}
	def getDnsZone(self,host=None):
		try:
			if host==None:
				print "sorry ,something wrong"
				
			print "hosts is "+host
			dns_name=os.popen('nslookup -type=ns'+host).read()
			dns_servers=re.findall('nameserver=([\w\.]+)',dns_name)
			for server in dns_servers:
				if len(server)<5:server+=host
				get_dns=os.popen('dig @%s axfr $s'%(server,host)).read()
				print get_dns
		except Exception,e:
			pass
			#print e
	def getAsNum(self,ip=None):
		try:
			if ip==None:
				ip=self.ip
			print "ip is "+ip
			ip=" \'origin %s\'"%ip  #转义单引号  whois -h xxxxx 'origin 1.1.1.1' 
			#print ip
			#通过识别之后的ip查询ip段。可能查询到的是服务商的ip段。或者是公司的ip段。  参考用
			as_num=os.popen('whois -h asn.shadowserver.org'+ip).read()#得到AS号详细信息
			print as_num
			#通过AS号反查ip段 
			num=as_num.split('|')[0].rstrip()
			cmd=" \'prefix %s\'"%as_num
			as_ip=os.popen('whois -h asn.shadowserver.org'+cmd).read().split('\n')
			return as_ip
		except Exception,e:
			print e
			return []
			#pritn e
	def getC(self,ip=None,config=None):
		try:
			if ip==None:
				ip=self.ip
			count={}
			ip=ip+"/24"
			ops="-open -p%s"
			getops=ops%config
			nm=NmapProcess(ip,options=getops)
			ps=nm.run()
			parsed=NmapParser.parse(nm.stdout)
			for host in parsed.hosts:
				count[host.address]=[host.address]
				for serv in host.services:
					if len(serv.cpelist)>1:

						count[host.address].append(serv.service+":"+str(serv.port)+":"+serv.cpelist[0])
					else:
						count[host.address].append(serv.service+":"+str(serv.port))
			return count



		except Exception,e:
			print e
			return []
if __name__=="__main__":
	a=scan(host="www.bhu.edu.cn")
	a.getC(config="80")

