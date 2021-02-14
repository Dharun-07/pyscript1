#!/usr/bin/env python3
from scapy.all import *

p=IP(dst="8.8.8.8")/ICMP()
sr1(p)
p.show()
