#!/usr/bin/env python3

from scapy.all  import *


request="GET/index.html HTTP/1.1\n\n"
pack=Ether()/IP(dst="www.skillrack.com")/TCP()/request
resp,unanswered=sr(pack)
if(resp):
    for i in resp:
        resp.show()
        resp.summary()
        print(hexdump(resp))
        print(resp[TCP].flags)