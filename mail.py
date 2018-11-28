# Author : Halim, v1.0;

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

msg = MIMEMultipart()
fromaddr = "username@topglove.com.my"
toaddr = "username@topglove.com.my"
msg["To"] = fromaddr
msg["From"] = toaddr
msg["Subject"] = "subject"

attachment = #attachment link

body="body"
msgText = MIMEText('<b>%s</b><br><img src="cid:%s"><br>' % (body, attachment), 'html')  
msg.attach(msgText)

fp = open(attachment, 'rb')                                                    
img = MIMEImage(fp.read())
fp.close()
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)

import smtplib
server = smtplib.SMTP('owa.topglove.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("username", "password")#username@topglove.com.my
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)