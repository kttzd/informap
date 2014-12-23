#!/usr/bin/python
#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import re
import requests
from bs4 import BeautifulSoup
from urlparse import urlparse
global sub
class GetSub(object):
	def __init__(self,site,tn):
		self.site=site
		self.url="http://www.baidu.com/s"
		self.tn=tn
		self.rn=100
		self.wd="site:%s -site:www.%s"
		self.headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'}
		self.pn=0
	def get_nums(self):
		payload={"wd":self.wd%(self.site,self.site),"rn":self.rn,"tn":self.tn}
		h=requests.get(self.url,params=payload,headers=self.headers)
		soup=BeautifulSoup(h.text)
		get_num=soup.find("div",class_="nums")
		get_num=str(get_num.string)
		regex = re.compile(r"[\xa6](.*?)[\xe4]")
		matchArray = regex.findall(get_num)
		nums=matchArray[1].replace(",","")
		return nums
	def get_url(self,pn):
		global sub
		sub=[]
		payload={"wd":self.wd%(self.site,self.site),"rn":self.rn,"tn":self.tn,"pn":pn}
		h=requests.get(self.url,params=payload,headers=self.headers)
		soup=BeautifulSoup(h.text)
		get_url=soup.find_all("span",class_="g")
		for i in range(len(get_url)):
			test=str(get_url[i].string)
			test="http://"+test
			sub.append(urlparse(test[0:test.index("\xc2")]).netloc)	

def main():
	global sub
	fuck=GetSub(site="189.cn",tn="coming soon")
	nums=int(fuck.get_nums())
	if nums<=100:fuck.get_url(pn=0)
	elif nums<=200:
		for payload_pn in xrange(0,300,100):
			fuck.get_url(pn=payload_pn)
	elif nums<=300:
		for payload_pn in xrange(0,400,100):
			fuck.get_url(pn=payload_pn)
	elif nums<=400:
		for payload_pn in xrange(0,500,100):
			fuck.get_url(pn=payload_pn)
	elif nums<=500:
		for payload_pn in xrange(0,600,100):
			fuck.get_url(pn=payload_pn)
	elif nums<=600:
		for payload_pn in xrange(0,700,100):
			fuck.get_url(pn=payload_pn)
	elif nums<=700:
		for payload_pn in xrange(0,800,100):
			fuck.get_url(pn=payload_pn)
	else:
		for payload_pn in xrange(0,900,100):
			fuck.get_url(pn=payload_pn)
	#fuck.get_url(pn=100)
	#fuck.get_url(pn=200)
	sub=list(set(sub))
	print sub
if __name__=="__main__":
	#print fuck.get_nums()
	main()
