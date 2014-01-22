#Without using optparse
# import zipfile
# from threading import Thread
# def extractFile( zFile, Password ):
# 	try:
# 		zFIle.extractAll(pwd= Password)
# 		print '[+] Found password'+password+'\n'
# 	except:
# 		pass
# def main():
# 	zFile = zipFile.ZipFile('evil.zip')
# 	passFile = open( 'dictionary.txt' )
# 	for lines in passFile.readlines():
# 		password = line.strip('\n')
# 		t= Thread( target = extractFile, args=(zFile, password))
# 		t.start()
# if __name__ == __main__:
# 	main()


#####End

#Using optparse
import zipfile
import optparse
from threading import Thread
def extractFile( zFile, Password ):
	try:
		zFIle.extractAll(pwd= Password)
		print '[+] Found password'+password+'\n'
	except:
		pass
def main():
	parser = optParse.OptionParser( "usage%prog"+ "-f <zipFile> -d <dictionary>")
	parser.add_option('-f',dest='zname',type="string", help="Specify a zip file")
	parser.add_option('-d',dest='dname',type="string", help="Specify a dict file")
	(options, args) = parser.parse_args()
	if( options.zname == None) | (option.dname == None):
		print parser_usage
		exit(0)
	else:
		zname = options.zname
		dname = options.dname
	zFile = zipFile.ZipFile(zname)

	passFile = open( dname )
	for lines in passFile.readlines():
		password = line.strip('\n')
		t= Thread( target = extractFile, args=(zFile, password))
		t.start()
if __name__ == '__main__' :
	main()
