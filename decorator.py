#decorator

def now():
	print "2015-11-18"
f=now
f()
print now.__name__
print f.__name__

def log(func):
	def wrapper(*args,**kw):
		print 'begin call %s():' %func.__name__
		func(*args,**kw)
		print 'end call %s():' %func.__name__
	return wrapper
@log
def now1():
	print now1.__name__
now1()

now1=log(now1)
now1()

def log1(text):
	def decorator(func):
		def wrapper(*args,**kw):
			print '%s %s():' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator
@log1('execute')
def now2():
	print now2.__name__
now2()

import functools

def log2(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):
		print 'call %s():' %func.__name__
		return func(*args,**kw)
	return wrapper

@log2
def now3():
	print now3.__name__
now3()

def log3(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s():' %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

@log3('execute')
def now4():
	print now4.__name__
now4()

def log4(text):
	if callable(text):
		@functools.wraps(text)
		def wrapper(*args,**kw):
			print 'begin call %s:' %text.__name__
			text(*args,**kw)
			print 'end call '+text.__name__
		return wrapper
	else :
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args,**kw):
				print 'begin call %s %s():' %(text,func.__name__)
				func(*args,**kw)
				print 'end call %s %s():' %(text,func.__name__)
			return wrapper
		return decorator
			
@log4
def now5():
	print 'doing'+now5.__name__
now5()
	
@log4('execute')
def now6():
	print 'doing'+now6.__name__
now6()