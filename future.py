#future

#still running on python 2.7
from __future__ import unicode_literals
from __future__ import division

print '\'xxx\' is unicode?',isinstance('xxx',unicode)
print 'u\'xxx\' is unicode?',isinstance(u'xxx',unicode)
print '\'xxx\' is unicode?',isinstance('xxx',str)
print 'b\'xxx\' is unicode?',isinstance(b'xxx',str)


print '10/3=',10/3
print '10.0/3=',10.0/3
print '10//3=',10//3