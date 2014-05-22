from scapy.all import *
import sys

dest = sys.argv[1]
dport = sys.argv[2]

'''
You can also pass an array to dport so it will act like a port scanner (nmap)
'''
def srExample(dest, Dport):
	return sr(IP(dst=dest)/TCP(dport=Dport)/"Hello World")

def showResult(packet):
	ans, unans = packet
	ans.summary()
	unans.summary()
'''
You can also define the type of packets to be send using flag parameter, for e.g. for sending a SYN 
packet send flag='S', for ACK send 'A', remember you need to do SYN ACK before you send ACK packets
'''

def srExampleWithFlag(dest, SPort, DPort, flag):
	return sr(IP(dst=dest)/TCP(sport= SPort, dport= DPort, flags= flag)/'Hello World') #Sport is the sending port from your side


p = srExample(dest, int(dport))
showResult(p) 	 	