from scapy.all import *
import sys

dest = sys.argv[1]
dport = sys.argv[2]

def srExample(dest, Dport):
	return sr(IP(dst=dest)/TCP(dport=Dport)/"Hello World")

def showResult(packet):
	ans, unans = packet
	ans.summary()
	unans.summary()

p = srExample(dest, int(dport))
showResult(p) 	 	