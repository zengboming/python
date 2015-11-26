#equal1

import re

print re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print re.match(r'^\d{3}\-\d{3,8}$','010 12345')
print re.split(r'\s+','a b  c')
print re.split(r'[\s\,]+','a,b, c  d')
print re.split(r'[\s\,\;]+','a,b;; c ,; d')

m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print m
print m.group(0)
print m.group(1)
print m.group(2)

t='19:05:30'
m=re.match(r'^(0[0-9]|1[0-9]|2[0-3][0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9][0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9][0-9])$',t)
print m.group()
print m.group(0)
print m.group(1)
print m.group(2)
print m.group(3)

print re.match(r'^(\d+)(0*)$','102300').group(1)
print re.match(r'^(\d+?)(0*)$','102300').group(1)

re_telephone=re.compile(r'^(\d{3})-(\d{3,8})$')
print re_telephone.match('010-12345').group()
print re_telephone.match('010-8086').group()

t1='someone@gmail.com'
t2='bill.gates@microsoft.com'
re_email=re.compile(r'^([0-9a-zA-Z\_\.]*)\@([a-z]*)\.([a-z]*)$')
print re_email.match(t1).group(1)
print re_email.match(t1).group(2)
print re_email.match(t1).group(3)
print re_email.match(t2).group(1)
print re_email.match(t2).group(2)
print re_email.match(t2).group(3)