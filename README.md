Informap
===================================  
版本:0.1
测试版本,功能单一请见谅
Require
----------------------------------- 
Required software:
```
python2.7
dig
```

Required python plugins:
```
json
requests
beautifulsoup4
libnmap
httplib2
```

使用方法
===================================  
例子 ()
----------------------------------- 
```
python informap.py -h vip.com  #通过调用接口,得到子域名,进行CDN的识别 
{"outside.vip.com": ["outside.vip.com", "183.61.89.133", "", "未知", "未知"]}
{"acs.vip.com": ["acs.vip.com", "221.228.213.148", "", "未知", "未知"]}
{"o.vip.com": ["o.vip.com", "14.17.85.10", "14.17.91.10", "", "未知", "未知"]}
{"mapi.vip.com": ["mapi.vip.com", "mapi.vip.com.wscdns.com", ["网宿科技"], "vipshop.xdwscache.glb0.lxdns.com", ["网宿科技"]]}
{"www.vip.com": ["www.vip.com", "www.vip.com.wscdns.com", ["网宿科技"], "vipshop.xdwscache.glb0.lxdns.com", ["网宿科技"]]}
{"pay.vip.com": ["pay.vip.com", "", "未知", "未知"]}

python informap.py -c 192.168.1.1 #简单的c段扫描。感兴趣的c段参数保存在config下的1.txt
{'192.168.1.1': ['192.168.1.1', 'http:80']}
```
功能
===================================
CDN识别   
----------------------------------- 
C段扫描
----------------------------------- 
IP反查
----------------------------------- 
AS号查询
----------------------------------- 
域传送漏洞检查
----------------------------------- 
