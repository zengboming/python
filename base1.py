#base1

import base64

print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')


print base64.urlsafe_b64encode('i\xb7\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

'abcd' -> 'YWJjZA=='
print base64.b64decode('YWJjZA==')
print safe_b64decode('YWJjZA')