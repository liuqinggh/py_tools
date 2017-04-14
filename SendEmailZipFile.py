# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 11:23:12 2016

@author: user
"""

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import MIMEMultipart

import email.MIMEBase

# 第三方 SMTP 服务
host="mail.XXX.com"  #设置服务器
user="XXX@XXX.com"  #用户名
passwd="PWD"   #口令 

sender = 'XXX@XXX.com'

message = MIMEMultipart.MIMEMultipart()  
#发件人
message['From'] = Header("BI 商务智能", 'utf-8')
#收件人
message['To'] =  Header("未显示", 'utf-8')

class Send_Email:
	def send(self, receivers, theme, emailbody):
		try:
                 message['Subject'] = Header(theme, 'utf-8')
                 message.attach(MIMEText(emailbody, 'plain', 'utf-8'))
                 smtpObj = smtplib.SMTP() 
                 smtpObj.connect(host, 25)    # 25 为 SMTP 端口号
                 smtpObj.starttls()
                 smtpObj.login(user, passwd)  
                 smtpObj.sendmail(sender, receivers, message.as_string())
                 print "邮件发送成功"
		except smtplib.SMTPException:
			print "Error: 无法发送邮件" 
		smtpObj.quit()
	
	def add_attach(self, path, fname):
             zf = open(path,'rb')
             contype = 'application/octet-stream'  
             maintype, subtype = contype.split('/', 1)  
             part = email.MIMEBase.MIMEBase(maintype, subtype)
             part.set_payload(zf.read())
             email.encoders.encode_base64(part)
             part.add_header('Content-Disposition', 'attachment', filename = fname)
             message.attach(part)
		
"""			
if __name__ == '__main__': 
    oper = Send_Email()
    oper.add_attach(attach_path, fname, message)
    oper.send(receivers, message)
"""