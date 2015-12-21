# -*- coding: utf-8 -*-
from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = "zengboming123@163.com"
password = "zbm510319"
# 输入SMTP服务器地址:
smtp_server = "smtp.163.com"
# 输入收件人地址:
to_addr = ["463215695@qq.com"]

import smtplib
server = smtplib.SMTP() 
server.connect(smtp_server,25);# SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
