#!/usr/bin/env python3
from scapy.all import *


def sniff_packets(packet):
    response=packet
    if(response[IP]):
        return(f"{response[IP].src}-------->{response[IP].dst}")




sniff(iface="eth0",prn=sniff_packets)
