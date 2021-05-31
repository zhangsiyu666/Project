import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date
from datetime import timedelta
import time

before_time =  ((date.today() - timedelta(7)).strftime("%Y-%m-%d"))
time = (time.strftime("%Y-%m-%d", time.localtime()))
sender = 'luke.xi@zenlayer.com'
to_receiver = 'fairy.wen@zenlayer.com, jaycee.hu@zenlayer.com, helson.du@zenlayer.com, jun.luo@zenlayer.com, kris.li@zenlayer.com, saber.tang@zenlayer.com, yif.jiang@zenlayer.com'
cc_receiver = 'jintao@zenlayer.com, luke.xi@zenlayer.com'
receiver = to_receiver + cc_receiver

username = 'luke.xi@zenlayer.com'
password = 'XiwangXW.1995'
mail_title = '%s~%s测试工单汇总' % (before_time, time)

message = MIMEMultipart()
message['From'] = sender
message['To'] = to_receiver
message['Cc'] = cc_receiver
message['Subject'] = Header(mail_title, 'utf-8')

message.attach(MIMEText('你好,\n邮件内容为%s~%s测试工单汇总。\n请您查收附件，附件需要经过Office365安全检查，请等待1分钟。\n此邮件为自动发送，有问题请联系我。\n\n--------------\nBR,\nLuke' % (before_time, time), 'plain', 'utf-8'))

att1 = MIMEText(open('/opt/report/%s~%s.xls' % (before_time, time), 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="%s~%s.xls"' % (before_time, time)
message.attach(att1)

smtpObj = smtplib.SMTP('smtp.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(username, password)
smtpObj.sendmail(sender, to_receiver.split(',') + cc_receiver.split(','), message.as_string())
smtpObj.quit()