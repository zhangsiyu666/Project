import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from datetime import timedelta
import time

#定义了七天之前的时间以及当前的时间
before_time =  ((date.today() - timedelta(7)).strftime("%Y-%m-%d"))
current_time = (time.strftime("%Y-%m-%d", time.localtime()))

#定义邮件的发送者、接受者、抄送对象
sender = 'casey.zhang@zenlayer.com'
to_receiver = 'saber.tang@zenlayer.com'
cc_receiver = 'luke.xi@zenlayer.com'
receiver = to_receiver + cc_receiver

#定义发送者的账户以及密码，邮件标题
username = 'casey.zhang@zenlayer.com'
password = 'gznlcxpvsgkttkmz'
mail_title = '%s-%s的测试工单汇总' % (before_time, time)

#自定义的邮箱格式文本
message = MIMEMultipart()
message['From'] = sender
message['To'] = to_receiver
message['Cc'] = cc_receiver
message['Subject'] = Header(mail_title, 'utf-8')

#邮箱内容正文
message.attach(MIMEText('您好！\n邮件为%s-%s测试工单汇总。\n请您查收附件，附件需要经过Office365安全检查，请等待1分钟。\n此邮件定时发送，有问题请联系我。\n\n\nBR,\nCasey' % (before_time, current_time), 'plain', 'utf-8'))

#定义要发送的附件
att1 = MIMEText(open('../Test/test job', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="%s~%s.txt"' % (before_time, time)
message.attach(att1)

#引用smtplib模块实现发送邮件功能
smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(username, password)
smtpObj.sendmail(sender, to_receiver.split(',') + cc_receiver.split(','), message.as_string())
smtpObj.quit()