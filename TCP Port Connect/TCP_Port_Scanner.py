import optparse
from socket import *
from threading import *

screenLock = Semaphore( value = 1 )

def connScan( tgtHost, tgtPort ):
	try:
		connSkt = socket( AF_INET, SOCK_STREAM)
		connSkt.connect( ( tgtHost, tgtPort ) )
		connSkt.send( 'ViolentPython\r\n' )
		results = connSkt.recv( 100 )
		screenLock.acquire()
		print '[+]%d/tcp open'% tgtPort
		print '[+] ' + str(results)
	except:
		screenLock.acquire()
		print '[-]%d/tcp closed'%tgtPort
	finally:
		screenLock.release()
		connSkt.close()

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
		t = Thread( target = connScan, args = ( tgtHost, int( tgtPort ) ) )
		print 'Scanning Port ' + tgtPort
		t.start()

def main():
	parser = optparse.OptionParser( "usage%prog"+ "-H <target host> -p <target port>")
	parser.add_option('-H',dest='tgtHost',type="string", help="Specify a target host")
	parser.add_option('-p',dest='tgtPort',type="string", help="Specify target ports seperated by commas E.g. 21,22,23")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str( options.tgtPort ).split(',')
	if( tgtHost == None ) | (tgtPorts[0] == None):
		print '[-] You must specify a target host and target port(s)'
		exit(0)
	portScan( tgtHost, tgtPorts )

if __name__ == '__main__' :
	main()
