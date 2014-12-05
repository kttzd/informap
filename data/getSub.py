# *-* coding : utf-8 *-*
import re
import datetime
import json
import requests


from bs4 import BeautifulSoup

class SubDomains(object):
	def __init__(self, domain):
		self.url = 'http://fofa.so/lab/ips'
		self.domain = domain

	def get_token(self):
		self.session = requests.Session()
		r = self.session.get(self.url)
		if r.text:
			soup = BeautifulSoup(r.text)
			inputs = soup.find_all('input')
			utf8 = inputs[0]
			token = inputs[1]

			return utf8['value'], token['value']

		return None, None

	def get_submains(self, token, utf8):
		payload = dict(
			utf8 				= utf8,
			authenticity_token 	= token,
			all 				= True,
			domain 				= self.domain 
			)

		headers = {
		'Host': 'fofa.so',
		'Pragma': 'no-cache',
		'Origin': 'http://fofa.so',
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.78.2 (KHTML, like Gecko) Version/7.0.6 Safari/537.78.2',
		'Referer': 'http://fofa.so/lab/ips'
		}
		
		all_ips = []
		all_sub_domains = []

		r = self.session.post(self.url, data=payload, headers=headers)
		if r.text:
			soup = BeautifulSoup(r.text)
			ips = soup.find_all('div', {'class' : 'col-lg-4'})
			subdomains = soup.find_all('div', {'class' : 'col-lg-8'})

			p = r'<a href="http://(.+?)" target="_blank">(.+?)</a>'
			r1 = re.compile(p, re.DOTALL)

			for ip in ips:
				_ip = r1.findall(str(ip))
				if _ip:
					all_ips.append(_ip[0][0])

			for sub_domain in subdomains:
				_sub_domain = r1.findall(str(sub_domain))
				if _sub_domain:
					all_sub_domains.append(_sub_domain[0][0])

		ip = []
		subdomains = []
		self.subdomains = dict(
			data 		= dict(
				ip 			= all_ips,
				subdomains 	= all_sub_domains,
				),
			domain 				= self.domain,
			ip_count			= len(all_ips),
			sub_domains_count 	= len(all_sub_domains),
			time				= datetime.datetime.now()
			)

	def result(self):
		return self.subdomains




if __name__ == '__main__':
	import sys
	domain=sys.argv[1]
	instance = SubDomains(domain)
	utf8, token = instance.get_token()
	#print utf8, token
	instance.get_submains(token, utf8)
	print instance.result()
