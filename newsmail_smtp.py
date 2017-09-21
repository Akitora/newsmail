# -*- coding: utf-8 -*-
 
import smtplib
from email.mime.text import MIMEText 
from email.header import Header
from email.utils import formatdate
 
def smtp(subject,text,to_address):
    from_address = "xxx@xxx.xxx"
 
    charset = "utf-8"
     
    msg = MIMEText(text.encode(charset),"plain",charset)
    msg["Subject"] = Header(subject,charset)
    msg["From"]    = from_address
    msg["To"]      = to_address
    msg["Date"]    = formatdate(localtime=True)
 
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('xxx@xxx.xxx','password')

    smtp.sendmail(from_address,to_address,msg.as_string())
    smtp.close()

if __name__ == '__main__':
    to_address = "xxx@xxx.xxx" 
    subject = u"メールの件名です"
    text    = u"メールの本文です"
    smtp(subject,text,to_address)
