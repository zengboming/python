#private oop
class student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print '%s:%s' %(self.__name,self.__score)
	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else :
			raise ValueError('bad score')

tom=student('Tom',95)
lisa=student('Lisa',74)
tom.print_score()
lisa.print_score()
tom.set_score(55)
tom.print_score()

print tom._student__name