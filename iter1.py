#iter1.py

import itertools
#natuals=itertools.count(1)
#for n in natuals:#
#	print n

#cs=itertools.cycle('ABC')
#for c in cs:
#	print c

ns=itertools.repeat('A',10)
for n in ns:
	print n
	
natuals=itertools.count(1)
ns=itertools.takewhile(lambda x:x<=10,natuals)
for n in ns:
	print n
	
for c in itertools.chain('ABC','XYZ'):
	print c
	
for key,group in itertools.groupby('AAABBBCCAAA'):
	print key,list(group)

for key,group in itertools.groupby('AaaBBbcCAAa',lambda x: x.upper()):
	print key,list(group)
	
for x in itertools.imap(lambda x,y:x*y,[10,20,30],itertools.count(1)):
	print x
	
r= itertools.imap(lambda x: x*x,itertools.count(1))
for n in itertools.takewhile(lambda x: x<100,r):
	print n
	