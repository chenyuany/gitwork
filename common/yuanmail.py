#-*- coding:utf-8 -*-
''' 
#文件名：
#作者：陈圆圆
#创建日期：2017/6/27
#模块描述：发送邮件
#历史修改记录
#修改人：
#修改日期：
#修改内容：
'''
import smtplib,datetime
from  email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
class sendMail(object):
	def send_mail(self):
		#设置服务器
		mail_host="smtp.163.com"
		#用户名
		mail_user="susuzhuan0321"
		#授权码
		mail_pass="susu321"
		#邮箱的后缀
		mail_postfix="163.com"
		#发送邮箱地址
		sender="susuzhuan0321@163.com"
		#接收邮件，可设置为你的QQ邮箱或者其他邮箱
		recedivers=["921510864@qq.com"]
		#创建一个带附件的实例
		message = MIMEMultipart()
		me=mail_user+"<"+mail_user+"@"+mail_postfix+">"
		message["From"]=me
		message["To"]=";".join(recedivers)
		message["Subject"]=Header('test(' + str(datetime.date.today()) + ')',"utf-8")
		message.attach(MIMEText('this is test', 'plain', 'utf-8'))
		att = MIMEText(open('\\testIsomp\\report\\testReport.html', 'rb').read(), 'base64', 'utf-8')
		att["Content-Type"] = 'application/octet-stream'
		# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
		att["Content-Disposition"] = 'attachment; filename="testReport.html"'
		message.attach(att)
		try:
			server=smtplib.SMTP_SSL(mail_host)
			server.login(mail_user,mail_pass)
			server.sendmail(sender,recedivers,message.as_string())
			server.close()
		except smtplib.SMTPException:
			print("send_mail fail")
#
# if __name__ == '__main__':
# 	sendMail().send_mail()