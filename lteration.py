#lteration

d={'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.itervalues():
	print value
for k,v in d.items():
	print k,v
for ch in 'ABCDEF':
	print ch

from collections import Iterable
print isinstance('abc',Iterable)
print isinstance([1,2,3],Iterable)
print isinstance(123,Iterable)

for i,value in enumerate(['A','B','C']):
	print i,value
for x,y in [(1,2),(3,4),(5,6)]:
	print x,y