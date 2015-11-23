#inheritance

class Animal(object):
	pass
#哺乳动物	
class Mammal(Animal):
	pass
#鸟类
class Bird(Animal):
	pass
	
class Runnable(object):
	def run(self):
		print('Running...')

class Flyable(object):
	def fly(self):
		print('Flying...')
		
#狗	
class Dog(Mammal,Runnable):
	pass
#蝙蝠	
class Bat(Mammal,Flyable):
	pass
#鹦鹉	
class Parrot(Bird,Flyable):
	pass
#鸵鸟	
class Ostrich(Bird,Runnable):
	pass


