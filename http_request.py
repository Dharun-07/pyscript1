#!/usr/bin/env python3
from scapy.all import *

load_layer("http")
req = HTTP()/HTTPRequest(
    Accept_Encoding=b'gzip, deflate',
    Cache_Control=b'no-cache',
    Connection=b'keep-alive',
    Host=b'www.google.com',
    Pragma=b'no-cache'
)
a = TCP_client.tcplink(HTTP, "www.google.com", 80)
answser = a.sr1(req)
a.close()
print(HTTPRequest.show(),1)
with open("www.google.html", "wb") as file:
    file.write(answser.load)