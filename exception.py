#exception

try:
	print 'try...'
	r=10/1
	print 'result:',r
except ZeroDivisionError,e:
	print 'ZeroDivisionError:',e
except ValueError,e:
	print 'ValueError:',e
else :
	print 'no error!'
finally:
	print 'finally...'
print 'End'

import logging

def foo(s):
	return 10/int(s)
def bar(s):
	return foo(s)*2
def main():
	try :
		bar('0')
	except StandardError,e:
		print 'Error!'
		logging.exception(e)
	finally :
		print 'finally'
		
main()
print 'END'

class FooError(StandardError):
	pass
def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value:%s' %s)
	return 10/n
	
foo('0')

def foo(s):
	n=int(s)
	return 10/n
def bar(s):
	try :
		return foo(s)*2
	except StandardError,e:
		print 'Error!'
		raise
def main():
	bar('0')
	
main()

try:
	10/0
except ZeroDivisionError,e:
	raise ValueError('input error!')
