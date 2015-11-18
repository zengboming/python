#sort

print sorted([36,5,12,9,21])

def reversed_cmp(x,y):
	if x>y:
		return -1
	elif x==y:
		return 0
	else:
		return 1
print sorted([36,5,12,9,21],reversed_cmp)

print sorted(['bob','about','Zoo','Credit'])

def cmp_ignore_case(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1<u2:
		return -1
	elif u1==u2:
		return 0
	else:
		return 1
print sorted(['bob','about','Zoo','Credit'],cmp_ignore_case)

def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax+=n
		return ax
	return sum
f=lazy_sum(1,3,5,7,9)
print f
print f()

def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs
f1,f2,f3=count()
print f1(),f2(),f3()

def count1():
	fs=[]
	for i in range(1,4):
		def f(j):
			def g():
				return j*j
			return g
		fs.append(f(i))
	return fs
f1,f2,f3=count1()
print f1(),f2(),f3()