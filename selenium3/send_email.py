import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart


class Send_email:

    def make_msg(self, file_name, now_time=None):
        """构造邮件"""
        # 发送邮件主题

        subject = "python auto test " + now_time

        # 发送的附件

        with open(file_name, 'r+', encoding='utf-8') as file:
            send_att = file.read()
        att = MIMEText(send_att, 'text', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = f'attachment;filename="{now_time}.html"'

        msg = MIMEMultipart()
        msg['FROM'] = "test66@yeah.net"
        msg['TO'] = "1185776486@qq.com"
        msg['Subject'] = subject
        msg.attach(att)

        return msg

        # 编写html类型邮件正文
        # msg = MIMEText('<html><h1>你好！</h1></html>', 'html', 'utf-8')
        # msg['FROM'] = "test66@yeah.net"
        # msg['TO'] = "1185776486@qq.com"
        # msg['Subject'] = Header(subject, 'utf-8')

    def send_msg(self, file_name, now_time=None):

        # 发送邮件
        msg = self.make_msg(file_name, now_time)

        smtp = smtplib.SMTP()
        smtp.connect("smtp.yeah.net")
        smtp.login("test66@yeah.net", "ZDGMZQFBWICEHVQM")
        smtp.sendmail("test66@yeah.net", "1185776486@qq.com", msg.as_string())
        smtp.quit()
        print("send success")


