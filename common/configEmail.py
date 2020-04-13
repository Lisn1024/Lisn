'''
功能：
1.配置发送邮件属性
2.读取邮件位置
3.发送邮件
'''
import smtplib,os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from common.readConfig import ReadConfig
from email.header import Header
import time

class ConfigEmail():

    r = ReadConfig()
    mail_host = r.get_eamil("mail_host")  #smtp服务
    mail_user = r.get_eamil("mail_user")   #用户名
    mail_pass = r.get_eamil("mail_pass")  #口令
    sender = r.get_eamil("sender")   #发送者
    receivers = r.get_eamil("receiver")  #接收者
    content = r.get_eamil("content")    #发送内容
    print(content)

    msg = MIMEMultipart()

    def config_file(self):
        #配置附件属性
        file = self.find_file()
        print(file)
        mail_body = open(file,"rb").read()
        #设置附件名字
        self.title = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime())
        att = MIMEText(mail_body,"base64","utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = "attachment;filename={}".format(self.title)
        self.msg.attach(att)

        #邮件正文内容
        self.msg["from"] = self.sender
        self.msg["To"] = self.receivers
        self.msg["Subject"] = Header(self.content,"utf-8")
        self.msg.attach(MIMEText("这是接口自动化报告邮件，如果想查看详情请查收"))

    def find_file(self):
        #查找最新文件
        #current_path = os.path.dirname(os.path.abspath(__file__))
       # print("文件路径",current_path)
        #filePath = os.path.dirname(os.getcwd()) + "\\" + "testReport"
        filePath = os.getcwd() + "\\" + "testReport"

        print(filePath)

        #获取filepath路径下全部文件名称的列表
        fileList = os.listdir(filePath)

        fileDoct = {}
        fileTime = []

        for iName in fileList:
            #拼接文件路径-文件名
            filename = filePath + "\\" + iName
            #获取文件修改时间
            iTime = os.path.getatime(filename)
            fileTime.append(iTime)
            fileDoct[iTime] = iName
        sendfilekey = max(fileTime)
        sendfile = fileDoct[sendfilekey]
        sendfile = filePath + "\\" + sendfile
        return sendfile

    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            s.connect(self.mail_host,25)
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(self.sender,self.receivers,self.msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            print("Error:无法发送邮件")
if __name__ == '__main__':
    c = ConfigEmail()
    c.send_mail()













