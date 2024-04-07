# !/usr/bin/python3


'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

mail_host = "smtp.qq.com"
mail_user = '2307592032@qq.com'
mail_password = 'csipcafxoujyebhg'

# 发送者、接收者
sender = '2307592032@qq.com'
receivers = ['yongqianma@foxmail.com']

# 文本内容、文本格式、编码格式
message = MIMEText('邮件发送内容', 'plain', 'utf-8')
message['From'] = formataddr(mail_host, mail_user)
message['To'] = formataddr("q1", receivers)

subject = "邮件发送test"
message['Subject'] = Header(subject, 'utf-8')

try:
    server = smtplib.SMTP_SSL(mail_host, 465)
    server.login(mail_user, mail_password)
    server.sendmail(sender,[receivers],message.as_string())
    server.quit()
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 465)
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(sender, [receivers, ], message.as_string())
    print("邮件发送成功")
    smtpObj.quit()
except smtplib.SMTPException:
    print("Error:无法发送邮件")
    print("地址：" + mail_host)
except ConnectionRefusedError:
    print("无法连接")
'''
# !/usr/bin/python3
import logging
import smtplib
import traceback
from email.mime.text import MIMEText
from email.utils import formataddr

"""my_sender = '2307592032@qq.com'  # 发件人邮箱账号
my_pass = 'myq..1230'  # 发件人邮箱密码
my_user = '940757181@qq.com'  # 收件人邮箱账号"""

my_sender = input("请输入发件人邮箱：")
my_pass = input("请输入发件人邮箱授权验证码:")
my_user = input("请输入收件人邮箱账号:")
my_writing = input("请输入发送内容：")


def mail():
    ret = True
    try:
        msg = MIMEText(my_writing, 'plain', 'utf-8')  # 发送内容
        msg['From'] = formataddr([" ", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr([" ", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "发送邮件测试-主题"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print(e)  # 捕捉错误并打印异常信息
    """ logging.error(e)  # 记录异常日志
     traceback.print_exc()  # 打印完整的错误信息"""
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
