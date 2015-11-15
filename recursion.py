# recursion.py

def fact(n):
	if n==1:
		return 1
	else :
		return n*fact(n-1)
		
print fact(1)
print fact(5)
print fact(100)

def fact1(n):
	return fact_item(n,1)

def fact_item(num,product):
	if num==1:
		return product
	return fact_item(num-1,num*product)
	
print fact1(1)
print fact1(5)
print fact1(100)