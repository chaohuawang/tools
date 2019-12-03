#!/usr/bin/env python
#coding=utf-8

import sys,os,time,pycurl,datetime
import smtplib
#from email.mime.text import MIMEText
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
reload(sys)
sys.setdefaultencoding('utf-8')

now = time.strftime("%Y-%m-%d", time.localtime())
sender = '**<**@**.**>'
receiver = '**<**@**.**>'
subject =  sys.argv[1]
smtpserver = 'smtp.ym.163.com'
username = '***@**.**'
password = '******
msg = MIMEMultipart()
att2 = MIMEText(open(sys.argv[2], 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="%s"' % sys.argv[2]
msg.attach(att2)
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver
try:
        smtp = smtplib.SMTP_SSL()
        smtp.connect(smtpserver,'465')
        smtp.login(username, password)
        smtp.sendmail('***@**.**',['***@**.**','***@**.**'], msg.as_string())
        smtp.quit()
        print ("邮件发送成功！")
except Exception as e:
        print ("邮件发送失败"+str(e))
