#Generator 

L=[x*x for x in range(10)]
print L
g=(x*x for x in range(10))
print g

for n in g:
	print n
	
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield b
		a,b=b,a+b
		n=n+1
print fib(6)
for x in fib(10):
	print x
	
def add(x,y,f):
	return f(x)+f(y)
	
print add(-5,6,abs)
	
	
	
