import unittest
from TestRunner import HTMLTestRunner
import time
import yagmail
from send_email import Send_email


# 定义测试目录为当前目录的test_case文件夹
test_dir = './test_case'
suits = unittest.defaultTestLoader.discover(test_dir, pattern="test_baidu.py")
now_time = time.strftime("%Y-%m-%d %H-%M-%S %p")


def send_yaemail(file_name=None):
    yag = yagmail.SMTP(user="test66@yeah.net", password="ZDGMZQFBWICEHVQM", host="smtp.yeah.net")
    subject = "python auto test " + now_time
    contents = "详情见附件"
    yag.send('1185776486@qq.com', subject, contents, attachments=file_name)


if __name__ == '__main__':
    report_name = './test_report/' + now_time + ' result.html'
    fb = open(report_name, 'wb')
    runner = HTMLTestRunner(stream=fb, title="测试百度搜索", description="WIN10 Chrome")
    runner.run(suits)
    fb.close()
    send_yaemail(report_name)