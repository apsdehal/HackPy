#!/usr/bin/python
from scapy.all import *

'''
Send an IMCP packet to google's server
Use wireshark to capture packets and see whats really happening
'''
def send_packet(source,life = 64):
	send(IP(src=source,dst="8.8.8.8",ttl=life)/ICMP()/"Hello World");
'''
You can manipulate the source by the src parameter in IP layer
But if do so you won't get ping reply since you spoofed the source IP
ttl: You can add this param to change the time to live for the packet, default: 64
'''
send_packet('10.0.0.1');	