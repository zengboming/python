#pop1

import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils  import parseaddr

def print_info(msg,indent=0):
	if indent==0:
		for header in ['From','To','Subject']:
			value=msg.get(header,'')
			if value:
				if header=='Subject':
					value=decode_str(value)
				else :
					hdr,addr=parseaddr(value)
					name=decode_str(hdr)
					value=u'%s<%s>' %(name,addr)
			print('%s%s:%s'%('  '*indent,header,value))
	if (msg.is_multipart()):
		parts=msg.get_payload()
		for n,part in enumerate(parts):
			print('%spart %s' %('  '*indent,n))
			print('%s--------------------' %('	'*indent))
			print_info(part,indent+1)
	else:
		content_type=msg.get_content_type()
		if content_type=='text/plain' or content_type=='text/html':
			content=msg.get_payload(decode=True)
			charset=guss_charset(msg)
			if charset:
				content=content.decode(charset)
			print('%sText:%s'%('	'*indent,content+'...'))
		else:
			print('%sAttachment: %s'%('	'*indent,content_type))

def decode_str(s):
	value,charset=decode_header(s)[0]
	if charset:
		value=value.decode(charset)
	return value
	
def guss_charset(msg):
	charset=msg.get_charset()
	if charset is None:
		content_type=msg.get('Content-Type','').lower()
		pos=content_type.find('charset=')
		if pos>=0:
			charset=content_type[pos+8:].strip()
	return charset

email=raw_input('zengboming123@163.com')
password=raw_input('zbm510319')
pop3_server=raw_input('pop.163.com')

server=poplib.POP3(pop3_server)
print(server.getwelcome())
server.user(email)
server.pass_(password)
print('Message: %s. Size: %s' %server.stat())
resp,mails,octets =server.list()
print(mails)
index=len(mails)
resp,mails,octets =server.retr(index)
msg_content='\r\n'.join(lines)
msg=Parser().parsestr(msg_content)
print_info(msg)
server.quit()

