#!/usr/bin/env python3
from scapy.all import *
print(get_if_list())
print(conf.route)
print(getmacbyip("192.168.75.2"))
print(conf.route.route("192.168.75.129"))