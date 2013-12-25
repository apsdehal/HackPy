import crypt
def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictfile = open('dictionary.txt','r')

	for word in dictfile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		if( cryptWord == cryptPass):
			print "[+] Found Password: "+word+"\n"
			return
	print "[-]Password not found. \n"
	return
def main():
	passFile = open("password.txt")
	for line in passFile.readline():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line:split(':')[1].strip(' ')
			print "[*] Cracking password for "+user
			testPass(cryptPass)

if __name__ == "__main__":
	main()