#filter

def is_odd(n):
	return n%2==1
print filter(is_odd,[1,2,3,4,5,6,7,8,9])

def not_empty(s):
	return s and s.strip()
print filter(not_empty,['A','','B',None])

x=range(1,101)
def ss(x):
	if x==1:
		return True
	else:
		for n in range(2,x):
			if x%n==0:
				return False
		return True
print filter(ss,x)

def is_not_primer(n):
	for x in range(2,n):
		if n%x==0:
			return False
	return True
print filter(is_not_primer,x)	
