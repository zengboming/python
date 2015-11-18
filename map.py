#map reduce

def f(x):
	return x*x

print map(f,[1,2,3,4,5,6,7,8,9])
print map(str,[1,2,3,4,5,6,7,8,9])

def add(x,y):
	return x+y

print reduce(add,[1,3,5,7,9])

def fn(x,y):
	return x*10+y

print reduce(fn,[1,3,5,7,9])

def char3num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
	'8':8,'9':9}[s]
print reduce(fn,map(char3num,'123456789'))

def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,
		'8':8,'9':9}[s]
	return reduce(fn,map(char2num,s))
print str2int('1234567')

def str3int(s):
	return reduce(lambda x,y:x*10+y,map(char3num,s))
print str3int('12345678')

x=['adam','LISA','barT']
def fun1(s):
	return s.capitalize()
print map(fun1,x)

def fun2(x,y):
	return x*y
def prod(s):
	return reduce(fun2,s)
print prod([1,2,3,4,5,6])
	