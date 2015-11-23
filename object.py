#object

print type(123)
print type('str')
print type(None)
print type(abs)

print type(123)==type(456)
print type('abc')==type('efg')
print type(123)==type('abc')

import types
print type('abc')==types.StringType
print type(u'abc')==types.UnicodeType
print type([])==types.ListType
print type(int)==type(str)==types.TypeType
print isinstance('a',(str,unicode))
print isinstance(u'a',(str,unicode))

print dir('ABC')
print len('ABC')
print 'ABC'.__len__()

class MyObject(object):
	def __len__(self):
		return 100

obj=MyObject()
print len(obj)
print obj.__len__()

print 'ABC'.lower()

class MObject(object):
	def __init__(self):
		self.x=9
	def power(self):
		return self.x*self.x
		
obj=MObject()
print obj.power()
print hasattr(obj,'x')
print hasattr(obj,'y')
print getattr(obj,'x')
setattr(obj,'y',19)
print hasattr(obj,'y')
print getattr(obj,'y')

print getattr(obj,'z',404)
print hasattr(obj,'power')
print getattr(obj,'power')
fn=getattr(obj,'power')
print fn
print fn()