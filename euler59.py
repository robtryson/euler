# euler59.py
__author__ = 'RTryson'

# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import sys
import numpy as np

def increment_key(s):
	kl = list(s)
	kl = list(map(ord,kl))
	kl[2] += 1
	if kl[2] > ord('z'):
		kl[2] = ord('a')
		kl[1] += 1
		if kl[1] > ord('z'):
			kl[1] = ord('a')
			kl[0] += 1
	return ''.join(list(map(chr,kl)))
	
def extend_key(key, l):
	num = (l // len(key)) + 1 # guaranteed too long, just truncate
	exkey = num * key
	return exkey[:l]
	
def reasonable(check):
	flag = False
	if check >= 32 and check <= 33: # space or bang
		flag = True
	if check == 39 or check == 46: # apostrophe or period
		flag = True
	if check >= 48 and check <= 57: # 0-9
		flag = True
	if check == 63: # question mark
		flag = True
	if check >= 65 and check <= 90: # capitals
		flag = True
	if check >= 97 and check <= 122: # lowercase
		flag = True
	return flag
	
def decrypt(data, key):
	decrypted = list()
	for i,c in enumerate(data):
		#cv = ord(c)
		k = key[i]
		kv = ord(k)
		check = c ^ kv
		if check >= 32 and check < 127: #printable characters
			decrypted.append(chr(check))
		else:
			return False
	return decrypted

def mess_to_ascii(message):
	ascii = list(message)
	ascii = list(map(ord,ascii))

f = open('datafiles/p059_cipher.txt','r')
sourcedata = f.readline()
sourcedata = sourcedata.split(",")
sourcedata = list(map(int, sourcedata))
f.close()
# sourcedata is a list of ints

#key = "aaa"
key = "god" # found it!

extend_len = len(sourcedata)
extended_key = extend_key(key, extend_len)
message = decrypt(sourcedata, extended_key)
answer = sum(list(map(ord,list(message))))
print(key, answer)

# used to find the key
while key[0] <= 'z':
	extend_len = len(sourcedata)
	extended_key = extend_key(key, extend_len)
	message = decrypt(sourcedata, extended_key)
	if message:
		print(''.join(message))
		print(key)
		input('press any key to continue')
	key = increment_key(key)