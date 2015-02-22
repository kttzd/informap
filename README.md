Informap
===================================  
版本:1.1
 _          __                                 
(_) _ __   / _|  ___   _ __ ___    __ _  _ __  
| || '_ \ | |_  / _ \ | '_ ` _ \  / _` || '_ \ 
| || | | ||  _|| (_) || | | | | || (_| || |_) |
|_||_| |_||_|   \___/ |_| |_| |_| \__,_|| .__/ 
                                          |_|    

Require
----------------------------------- 
Required software:
```
python2.7
nmap
dig
nslookup
```

Required python plugins:
```
sys
urlparse
json
requests
beautifulsoup4
libnmap
httplib2
```

使用方法
===================================  
例子 
----------------------------------- 
```
python informap.py -h vip.com  #通过调用接口,得到子域名,进行CDN的识别 
{"outside.vip.com": ["outside.vip.com", "183.61.89.133", "", "未知", "未知"]}
{"acs.vip.com": ["acs.vip.com", "221.228.213.148", "", "未知", "未知"]}
{"o.vip.com": ["o.vip.com", "14.17.85.10", "14.17.91.10", "", "未知", "未知"]}
{"mapi.vip.com": ["mapi.vip.com", "mapi.vip.com.wscdns.com", ["网宿科技"], "vipshop.xdwscache.glb0.lxdns.com", ["网宿科技"]]}
{"www.vip.com": ["www.vip.com", "www.vip.com.wscdns.com", ["网宿科技"], "vipshop.xdwscache.glb0.lxdns.com", ["网宿科技"]]}
{"pay.vip.com": ["pay.vip.com", "", "未知", "未知"]}
```
功能
===================================
CDN识别    
----------------------------------- 
```
python informap.py -t 要识别的网站.txt 
{"www.vip.com": ["www.vip.com", "www.vip.com.wscdns.com", ["网宿科技"], "vipshop.xdwscache.glb0.lxdns.com", ["网宿科技"]]}
```
C段扫描
----------------------------------- 
```
python informap.py -c 192.168.1.1 #简单的c段扫描。感兴趣的c段参数保存在config下的1.txt
{'192.168.1.1': ['192.168.1.1', 'http:80']}
```
IP反查和AS号查询
----------------------------------- 
```
python informap.py -i 8.8.8.8 
[u'www.128edu.com', u'www.51weixing.com', u'www.7y1.com', u'www.89sf.com', u'www.925975.com', u'www.99anju.com', u'www.aiyun.com', u'www.as51z.com', u'www.caihan.com', u'www.china-goldfish.com', u'www.chinaemv.com', u'www.chufaba.com', u'www.ciic-e.com', u'www.cnwwe.com', u'www.colorfulbrand.com', u'www.cq139.com', u'www.cqhao.com', u'www.crusher-cn.com', u'www.csdgt.com', u'www.ctgchina.com']

```
域传送漏洞检查
----------------------------------- 
```
python informap.py -d xxx.com
```
搜索引擎采集子域名
-----------------------------------
```
python informap.py -b 189.cn
获得使用者当地运营商劫持的tn账号，然后打印出子域名

tn ->当地劫持的tn账号
ha.189.cn
club.189.cn
enavi.189.cn
passport.189.cn
game.189.cn
gz.189.cn
yn.189.cn
web.sh.ptt.189.cn
open.189.cn
dm.189.cn
cloud.189.cn
speed.sc.189.cn
nb.189.cn
eyun.sh.189.cn
netreport.sh.189.cn
ctrl.189.cn
mall.hb.189.cn
music.189.cn
kzone.zhidao.189.cn
fj.189.cn
mail.189.cn
help.189.cn
ah.passport.189.cn
tj.189.cn
d.gd.189.cn
800.189.cn
shop.sc.189.cn
gs.189.cn
等等
```
