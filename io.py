#IO

f=open('test.txt','r')
print f.read()
f.close()

f1=open('f:/python/workspace/test.txt','r')
print f1.read()
f1.close()

try:
	f=open('test.txt','r')
	print f.read()
finally:
	if f:
		f.close()
		
with open('test.txt','r') as f:
	for line in f.readlines():
		print line.strip()

f=open('test.png','rb')
f.read()
f.close()

import codecs
with codecs.open('test.txt','r','gbk') as f:
	print f.read()
	
with open('test.txt','w') as f:
	f.write('Hello,world!')
with open('test.txt','r') as f:
	print f.read()