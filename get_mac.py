#!usr/bin/env python3
from scapy.all import *

print("-------------------------------------GET_MAC------------------------------------")
#a=input("Enter the ip address : ")

response,unanswered= srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.75.2"),timeout=2,retry=10)

print(response)
for r,s in response:
    print(r[Ether].src,s[Ether].src)