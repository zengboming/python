#property

class Student(object):
	def get_score(self):
		return self.score
	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value<0 or value>100:
			raise ValueError('score must be between 0 to 100')
		self.score=value

s=Student()
s.set_score(60)
print s.get_score()

class student(object):

	@property
	def score(self):
		return self._score
		
	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value<0 or value>100:
			raise ValueError('score must be between 0 to 100')
		self._score=value
		
	@property
	def birth(self):
		return self._birth

	@birth.setter
	def birth(self,value):
		self._birth=value
	
	@property
	def age(self):
		return 2015-self._birth
		
s1=student()
s1.score=30
s1.birth=1993
print s1.score
print s1.birth
print s1.age



