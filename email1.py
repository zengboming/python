#email
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText

from_addr='hello<zengboming123@163.com>'
me='zengboming123@163.com'
password='zbm510319'
smtp_server='smtp.163.com'
to_addr='520140341@qq.com'

msg = MIMEText('Hello world!',_subtype='plain',_charset='utf-8')
msg['Subject'] ='hello' 
msg['From'] =from_addr

server=smtplib.SMTP()
server.connect(smtp_server)
server.set_debuglevel(1)
server.login(me,password)
server.sendmail(from_addr,to_addr,msg.as_string())
server.quit()


