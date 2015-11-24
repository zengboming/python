#file

import os
print os.name
os.environ
os.getenv('PATH')
print os.path.abspath('.')
print os.path.join('/path/to','file')
print os.path.split('/path/to/file.txt')
print os.path.splitext('/path/to/file.txt')
#os.rename('text1.txt','text1.py')
#os.remove('text1.py')
print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) 
and os.path.splitext(x)[1]=='.py']

def search(s,path='.'):
	for x in os.listdir(path):
		y=os.path.join(path,x)
		if os.path.isdir(y):
			search(s,y)
		elif os.path.isfile(y):
			if s in y:
				print y
search('a')