import optparse
import socket
from socket import *

def connScan( tgtHost, tgtPort ):
	try:
		connSkt = socket( AF_INET, SOCK_STREAM)
		connSkt.connect( ( tgtHost, tgtPort ) )
		connSkt.send( 'ViolentPython\r\n' )
		results = connSkt.recv( 100 )
		print '[+]%d/tcp open'% tgtPort
		print '[+] ' + str(results)
		connSkt.close()
	except:
		print '[-]%d/tcp closed'%tgtPort

def portScan( tgtHost, tgtPorts ):
	try:
		tgtIP = gethostbyname( tgtHost )
	except:
		"[-] Cannot resolve '%s': Unknown Host"% tgtHost
		return
	try:
		tgtName = gethostbyaddr( tgtIP )
		print '\n[+] Scan Results for:' + tgtName[0]
	except:
		print '\n[+] Scan Results for:' + tgtIP
	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		tgtPort = tgtPort
		print 'Scanning Port ' + tgtPort
		connScan( tgtHost, int( tgtPort ) )

def main():
	parser = optparse.OptionParser( "usage%prog"+ "-H <target host> -p <target port>")
	parser.add_option('-H',dest='tgtHost',type="string", help="Specify a target host")
	parser.add_option('-p',dest='tgtPort',type="string", help="Specify target ports seperated by commas")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str( options.tgtPort ).split(', ')
	if( tgtHost == None ) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and target port(s)'
		exit(0)
	portScan( tgtHost, tgtPorts )

if __name__ == '__main__' :
	main()
