#fun2.py

def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s

a=power(15,2)
b=power(15)
print a,b

def enroll(name,gender,age=6,city='Beijing'):
	print 'name:',name 
	print 'gender:',gender
	print 'age:',age
	print 'city:',city

enroll('Sarash','F')
enroll('Bob','M',7)
enroll('Adam','M',city='Tianjing')

def add_end(L=None):
	if L is None:
		L=[]
	L.append('End')
	return L

print add_end()
print add_end(['a','b','c'])
print add_end(['1'])

def calc(*number):
	sum=0
	for n in number:
		sum+=n*n
	return sum
print calc(1,2,3)
print calc(1,3,5,7)
print calc()

nums=[1,2,3]
print calc(nums[0],nums[1],nums[2])
print calc(*nums)

def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw

person('Michael',30)
person('Bob',35,city='Beijing')
person('Adam',45,gender='M',joib='Engineer')

kw={'city':'Beijing','job':'Engineer'}
person('Jack',24,city=kw['city'],job=kw['job'])
person('Jack',24,**kw)

def func(a,b,c=0,*args,**kw):
	print 'a:',a,'b:',b,'c:',c,'args:',args,'other:',kw
	
func(1,2)
func(1,2,3)
func(1,2,c=3)
func(1,2,3,'a','b')
func(1,2,3,'a','b',x=99)