#!/usr/bin/python
# -*- coding: utf-8 -*-
# 多端口请求http
# 支持多线程
# python httpscan.py example.com timeout port-from port-to threads
__author__ = 'kttzd'

import sys
import httplib2
import futures
import time

headers={}
headers['User-Agent']="Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6"

if len(sys.argv)<2:
        print "example:python httpscan.py www.xxx.com 2 80 3000 20"
        sys.exit()
else:

    ADDRESS=sys.argv[1]
    TIMES=int(sys.argv[2])
    START=int(sys.argv[3])
    STOP=int(sys.argv[4])
    THREADS=int(sys.argv[5])


class httpscan():
    def __init__(self,ADDRESS,TIMES):
        self.address=ADDRESS
        #self.headers=headers
        self.times=TIMES
    def scan(self,port):
        h=httplib2.Http(timeout=self.times)
        host="http://"+self.address+":"+str(port)
        #print host
        try:
            res,con=h.request(host,"HEAD")
            print host+"---------I GET IT"
        except Exception,e:
            #print e
            pass
        except KeyboardInterrupt:
	    sys.exit()
        
def main():
    test=httpscan(ADDRESS,TIMES)
    #start = time.time()
    try:
        with futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
            tasks =dict((executor.submit(test.scan,port),port) for port in map(str,xrange(START,STOP)))
            futures.as_completed(tasks)
    except KeyboardInterrupt:
        sys.exit()
        #print "Scan done\n"
    finally:
        print "Have a nice day"

if __name__=="__main__":
    main()
