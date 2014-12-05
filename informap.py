#!/usr/bin/python
#by kttzd
#coding:utf-8
import os
import sys
import getopt
from data.infor_class import scan
from data.CDN import cdn
def main():
	try:
		opts,args=getopt.getopt(sys.argv[1:],"yh:i:u:c:",["help","host=","ip=","url=","c="])
	except getopt.GetoptError:
		print "--------"
	_host=None
	_ip=None
	_url=None
	_c=None
	for name,value in opts:
		if name in ("-y","--help"):
			
			sys.exit()

		elif name in ("-h","--host"):
			_host=value
		elif name in ("-i","--ip"):
			_ip=value
		elif name in ("-u","--url"):
			_url=value
		elif name in ("-c","--c"):
			_c=value
	if _host:
		
		host=scan(_host)
		#host.getDnsZone()
		a=host.getSubDomains()
		for host in  a["subdomains"]:
			h=cdn(host)
			h.getCdn()
	if _ip:
		ip=scan(_ip)
		print ip.getFromChinaZ()
		print ip.getAsNum()
	if _url:
		url=scan(_url)
	if _c:
		with open("config/1.txt") as f:
			config=f.readlines()[0].strip("\n")
		getC=scan(host=_c)
		h=getC.getC(config=config)
		print h
		#for key in h.keys():
		#	print getC.getFromChinaZ(ip=key)


if __name__=="__main__":
	main()
