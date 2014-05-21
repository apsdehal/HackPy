#! /usr/bin/python
import sys
from scapy.all import *
'''
Takes first argument given at commandline
'''
dest = sys.argv[1]

'''
sr1 takes a packet sends it and returns first answered packet back
dest: Destination to which packet has to be sent
'''
def sr1Example(dest):
	return sr1(IP(dst=dest)/ICMP()/"Hello World")

'''
Print out the result of answered packed object
'''
def showResult(returnPacket):
	returnPacket.show()

h = sr1Example(dest)

showResult(h) 