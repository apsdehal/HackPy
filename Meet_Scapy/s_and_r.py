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

'''
If you want a true port scanner we must enter a random sport, give an interval b/w packets, maybe retries and timeouts
Inter : Time to wait b/w to consecutive packets
Retry: No of retries to be handled in case of unanswered packets. For e.g. if no of retries are 2, scapy will try to send 
		unanswered packets 2 times, if its -2, scapy will resend unanswered packets unil no more answers are are given for 
		same set of unanswered packets two times in a row
Timeout: Time to wait after sending last packet		
'''

def srPortScanner( dest, dPortArray, interval, retries, timeouts):
	return sr(IP(dst=dest)/TCP(sport= RandShort(),dport= dPortArray, inter= interval, retry= retries, timeout= timeouts)) 

p = srExample(dest, int(dport))
showResult(p) 	 	