#type

from Hello1 import Hello
h=Hello()
h.hello()
print type(Hello)
print type(h)

def fn(self,name='WORLD'):
	print 'Hello,%s' %name
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
print type(Hello)
print type(h)
