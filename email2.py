#email2.py

#!/usr/bin/python
import smtplib
from_mail='zengboming999@163.com'
to_mail='520140341@qq.com'
server=smtplib.SMTP('smtp.163.com')
server.docmd('ehlo','zengboming999@163.com')
server.login('zengboming999@163','zbm510319')
msg='''from:zengboming999@163
to:520140341@qq
subject:I am guol
I'm come 153
.
'''
server.sendmail(from_mail,to_mail,msg)
server.quit()