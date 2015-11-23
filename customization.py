#customization

class student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return 'student object (name:%s)' %self.name
	def __call__(self):
		print 'My name is %s' %self.name
	__repr__=__str__
	
s=student('Michael')
print s
print student('Michael')
print s()

class fib(object):
	def __init__(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def next(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>10000:
			raise StopIteration()
		return self.a
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for x in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			a,b=1,1
			l=[]
			for x in range(stop):
				if(x>=start):
					l.append(a)
				a,b=b,a+b
			return l
	def __getattr__(self,attr):
		if attr=='score':
			return 99
		if attr=='age':
			return lambda:25

for n in fib():
	print n
f=fib()
print f[0]
print f[1]
print f[5]
print f[100]
print f[3:8]
print f[:10]
print f.score
print f.age()

class Chain(object):
	def __init__(self,path=''):
		self.path=path
	def __getattr__(self,path):
		return Chain('%s%s' %(self.path,path))
	def __str__(self):
		return self.path
print Chain().status.user.timeline.list

print callable(student('tom'))
print callable(max)
print callable([1,2,3])
print callable(None)
print callable('string')
