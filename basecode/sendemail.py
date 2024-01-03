import smtplib
from email.message import EmailMessage

def send_email(remail, rsubject, rcontent):
    email = EmailMessage()
    # 发件人邮箱
    email['from'] = '569061700@qq.com'
    # 收件人邮箱
    email['to'] = remail
    # 主题
    email['subject'] = rsubject
    # 内容
    email.set_content(rcontent)
    with smtplib.SMTP(host='smtp.qq.com',port=25)as smtp:
        smtp.ehlo()
        smtp.starttls()
        # 授权码登录
        smtp.login('569061700@qq.com',"qppjnvmztttlbfgi")
        smtp.send_message(email)
        print("email send to ",remail)

if __name__ == '__main__':
    send_email('qqshen@betawm.com','test','test')