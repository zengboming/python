#slots

class Student(object):
	pass
	
s=Student()
s.name='Michael'
print s.name

def set_age(self,age):
	self.age=age
	
from types import MethodType
s.set_age=MethodType(set_age,s,Student)
s.set_age(25)
print s.age

def set_score(self,score):
	self.score=score
Student.set_score=MethodType(set_score,None,Student)
s.set_score(100)
print s.score
s2=Student()
s2.set_score(99)
print s2.score

class student(object):
	__slots__=('name','age')
s=student()
s.name='Michael'
s.age=25

print s.name
print s.age

class graduateStudent(student):
	pass
	
g=graduateStudent()
g.score=999
print g.score