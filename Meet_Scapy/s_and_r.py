#! /usr/bin/python
import sys
from scapy.all import *

dest = sys.argv[1]

def sr1Example(dest):
	return sr1(IP(dst=dest)/ICMP()/"Hello World")

def showResult(returnPacket):
	returnPacket.show()

h = sr1Example(dest)

showResult(h) 