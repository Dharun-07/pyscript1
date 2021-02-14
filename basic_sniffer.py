#!/usr/bin/env python3
from scapy.all import *


def sniff_packets(packet):
    return(f"{packet[0][1].src}===>{packet[0][1].dst}")




sniff(iface="eth0",prn=sniff_packets)
