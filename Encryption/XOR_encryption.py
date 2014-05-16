from itertools import izip, cycle

def xor(data, key):
    return ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(data, cycle(key)))
def xor3(s,t):
    """xor two strings together"""
    return "".join(chr(ord(a)^ord(b)) for a,b in zip(s,t))

def xor2(s, key):
	output = ""
	length = len(key)
	j=0
	for i in range(0, len(s)):
		if j<length:
			character = chr(ord(s[i]) ^ ord(key[j]))
			output += character
			j+=1
		else:
			j=0
			character = chr(ord(s[i]) ^ ord(key[j]))
			output += character
			j+=1;
	return output

firstString = 'This sentence is encrypted using XOR cipher.'
secondString = 'LAcbGEUKHQEGDgsaHU8bGEUcFgwAEhUNHQtSHhYQFghSMyorWAwbGw0cCkE='
thirdString = 'LAcXSz02Kk8RAhURHR1SAhZZGU8EDhcAWBgXCg5ZGwcdAgYcWAkdGUUYWAwbGw0cCk8TBQFZCwcdHgkdWAEdH0UQFk8CGQQaDAYRDktZLAcXSwMVGQhSDQoLWBsaAhZZFAoEDglZERxSHw0cWAsXCBcACBsbBAtZEwoLSwwNCwoeDUs='

fourth = xor3(firstString, secondString)
print fourth
print xor3(thirdString, fourth)