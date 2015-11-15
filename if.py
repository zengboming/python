# print abstract value of integer
# -*- coding: utf-8 -*-

age=20
if age>=6:
    print'tenager'
elif age>=18:
    print'adult'
else :
    print'kid'
	
birth=int(raw_input('birth: '))
if birth<2000:
	print u'00前'
else:
	print u'00后'