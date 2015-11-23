#subclass

class Animal(object):
	def run(self):
		print 'Animal is running...'
		
class Dog(Animal):
	def run(self):
		print 'Dog is running...'
	def eat(self):
		print 'Eatting meat...'
		
class Cat(Animal):
	def run(self):
		print 'Cat is running...'
	def eat(self):
		print 'Eatting fish...'
	
dog=Dog()
dog.run()
dog.eat()

cat=Cat()
cat.run()
cat.eat()

a=list()
b=Animal()
c=Dog()
print isinstance(a,list)
print isinstance(b,Animal)
print isinstance(c,Dog)
print isinstance(c,Animal)

def run_twice(animal):
	animal.run()
	animal.run()
run_twice(Animal())
run_twice(Cat())
run_twice(Dog())
