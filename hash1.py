#hash1.py

import hashlib

md5=hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest()

md5=hashlib.md5()
md5.update('how to use md5 in')
md5.update('python hashlib?')
print md5.hexdigest()

sha1=hashlib.sha1()
sha1.update('how to use sha1 in')
sha1.update('python shalib?')
print sha1.hexdigest()

def calc_md5(password):
	md5=hashlib.md5()
	md5.update(password)
	return md5.hexdigest()
	
print calc_md5('123456')
print calc_md5('abc999')

db={
	'michael':'e10adc3949ba59abbe56e057f20f883e',
	'bob':'878ef96e86145580c38c87f0410ad153',
	'alice':'99b1c2188db85afee403b1536010c2c9'
}

def login(user,password):
	if db[user]==calc_md5(password):
		print True
	else:
		print False
login('michael','123456')
login('bob','abc999')
login('alice','123456')

def calc_md51(password):
	return get_md5(password+'the-Salt')
