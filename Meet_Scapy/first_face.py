#!/usr/bin/python
from scapy.all import *

'''
Send an IMCP packet to google's server
'''
def send_packet():
	send(IP(dst="8.8.8.8")/ICMP()/"Hello World");

send_packet();	