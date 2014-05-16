import nmap
import optparse
def nmapScan ( tgtHost, tgtPort ):
	nm = nmap.PortScanner()
	nm.scan( tgtHost, tgtPort )
	state = nm[ tgtHost ][ 'tcp' ][ int( tgtPort ) ][ 'state' ]
	print " [*] " + tgtHost + " tcp/" + tgtPort + " " + state

def main():
	parser = optparse.OptionParser( 'usage %prog' + '-H <target host> -p <target ports>' )
	parser.add_option( '-H', dest = 'tgtHost', type = "string", help = 'Specify target host' )
	parser.add_option( '-p', dest = 'tgtPort', type = "string", help = 'Specify target port seperated by comma, e.g. 21,22,23' )
	( options, args ) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	if( tgtHost == None ) | ( tgtPorts[0] == None ):
		print parser.usage
		exit(0)
	for tgtPort in tgtPorts:
		nmapScan( tgtHost, tgtPort )

if __name__ == '__main__':
	main()
