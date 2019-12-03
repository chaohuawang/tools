#!/usr/bin/env python
#coding=utf-8
#作者：王超华
#功能：邮件发送客户端，支持显示名称，接受，抄送，密送等功能，支持文本，网页，附件等
import smtplib,sys,base64,re
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication 
reload(sys)
sys.setdefaultencoding('utf-8') 
if __name__ == '__main__':
    smtpserver = 'smtp.ym.163.com'
    username = '******@**.com'
    password = '******'
    receiver = '**<******@**.comt>' #邮件接受者
    print('邮件主送对象:>>',receiver)
    cc = '**<******@**.com>' #邮件抄送者
    print('邮件抄送对象:>>',cc)
    bcc = '**<******@**.com>' #邮件密送者
    print('邮件密送对象:>>',bcc)
    allreceivers= '%s,%s,%s' %(receiver,cc,bcc) #合并所有接受者
    emiless = re.findall(r'[0-9a-zA-Z._]+@[0-9a-zA-Z._]+\.[0-9a-zA-Z._]+', allreceivers) #匹配邮箱
    emiles = set(emiless)   #去重
    #分割邮箱名和邮箱
    toaddrs = []
    for emile in emiles:
        for i in emile.split(','):
            toaddrs.append(i)
    print('邮件发送给:>>',toaddrs)
    m = MIMEMultipart()
    #邮件正文
    content = '这是正文部分。<a href="http://www.baidu.com">跳转页面</a>'
    # plain 文本
    # html  网页
    textApart = MIMEText(content,'html','utf-8')       
    m.attach(textApart)
    #邮件附件
    Files=['smail.py','这是PDF.pdf','这是压缩文件.zip','这是图片.png']
    print('邮件包含的附件:>>',Files)
    number = 0
    for f in Files:
        fnApart='Apart%s' %number
        print (fnApart)
        fnApart = MIMEApplication(open(f, 'rb').read())
        fnApart.add_header('Content-Disposition', 'attachment', filename= '=?utf-8?b?' + base64.b64encode(f.encode('UTF-8')) + '?=') #filename 加上特殊代码可以解决附件名乱码问题
        m.attach(fnApart)
        number = number + 1
    #以下为测试代码 ---------------------------------------------------
    #附件1 #图片
    #imageFile = '这是图片.png'
    #imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    #imageApart.add_header('Content-Disposition', 'attachment', filename= '=?utf-8?b?' + base64.b64encode(imageFile.encode('UTF-8')) + '?=')
        
    #附件2 #pdf
    #pdfFile = '这是PDF.pdf'
    #pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    #pdfApart.add_header('Content-Disposition', 'attachment', filename= '=?utf-8?b?' + base64.b64encode(pdfFile.encode('UTF-8')) + '?=')
    
    #附件3 #ZIP
    #zipFile = '这是压缩文件.zip'
    #zipApart = MIMEApplication(open(zipFile, 'rb').read())
    #zipApart.add_header('Content-Disposition', 'attachment', filename= '=?utf-8?b?' + base64.b64encode(zipFile.encode('UTF-8')) + '?=')
 
    #m = MIMEMultipart()
    #m.attach(textApart)
    #m.attach(imageApart)
    #m.attach(pdfApart)
    #m.attach(zipApart)
    #------------------------------------------------------------------
    m['Subject'] = '这是标题'  #邮件主题
    m['From'] = '系统通知<%s>' % username  #邮件发送者
    m['To'] = receiver #邮件接受者
    m['cc'] = cc #抄送

 
    try:
        #普通方式
        #server = smtplib.SMTP(smtpserver)
        #ssl方式开始
        server = smtplib.SMTP_SSL()
        server.connect(smtpserver,'465')
        #ssl方式结束
        server.login(username,password)
        server.sendmail(username, toaddrs, m.as_string())
        print('+邮件发送成功!!!')
        server.quit()
    except smtplib.SMTPException as e:
        print('-邮件发送失败!!!:',e) #打印错误
