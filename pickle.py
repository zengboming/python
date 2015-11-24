#pickle

try:
	import cPickle as pickle
except ImportError:
	import pickle
	
d=dict(name='Bob',age=20,score=88)
print pickle.dumps(d)

f=open('dump.txt','wb')
pickle.dump(d,f)
f.close()

f=open('dump.txt','rb')
d=pickle.load(f)
f.close()
print d

import json
d=dict(name='Tom',age=40,score=55)
print json.dumps(d)
json_str='{"age":40,"score":55,"name":"Tom"}'
print json.loads(json_str)

class Student(object):
	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score
		
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
		
s=Student('Lisa',18,99)
print json.dumps(s,default=student2dict)
print json.dumps(s,default=lambda obj:obj.__dict__)

def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
json_str='{"age":40,"score":55,"name":"Tom"}'
print json.loads(json_str,object_hook=dict2student)