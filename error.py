#error

def foo(s):
	n=int(s)
	assert n!=0,'n is zero!'
	return 10/n
def main():
	foo('0')
	


import logging
import pdb
logging.basicConfig(level=logging.INFO)

s='0'
n=int(s)
logging.info('n=%d'%n)
print 10/n


s='0'
n=int(s)
pdb.set_trace()
print 10/n