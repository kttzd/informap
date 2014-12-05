#!/usr/bin/python
# -*- coding: utf-8 -*-
# 多端口请求TCP
# 多线程支持 默认10线程
# python scanport.py example.com port_start port_stop (threads)

__author__ = 'kttzd'

import sys
import socket
import futures
import time

ADDRESS=sys.argv[1]
START=int(sys.argv[2])
STOP=int(sys.argv[3])
try:
    THREADS=int(sys.argv[4])
except:
    THREADS=10

def url2ip(ADDRESS):
    try:
        ip=socket.gethostbyname(ADDRESS)
        return ip
    except:
        print "sorry,something wrong"
class portscan():
    def __init__(self,IP):
        self.ip=IP
        #self.timeout=TIMEOUT
    def scan(self,port):

        s=socket.socket()
        s.settimeout(0.1) #timeout 手动修改 > <
        try:
            s.connect((self.ip,port))
        except Exception,e:
            #print e
            pass
        else:
            print '%s open'% port
        s.close()
if __name__=="__main__":
    start = time.time()
    IP=url2ip(ADDRESS)
    test=portscan(IP)
    #test.scan(port)
    print "ip ------------>"+str(IP)

    with futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        tasks=dict((executor.submit(test.scan,port),port) for port in range(START,STOP))
        futures.as_completed(tasks)
