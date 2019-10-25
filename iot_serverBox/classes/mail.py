import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#context = ssl.create_default_context()

def envoiMail(text):
    print("fonction")
    #my_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    try:
        my_smtp = smtplib.SMTP_SSL('smtp.googlemail.com',465)#,context=context)
        print("1")
        my_smtp.login('test@gmail.com','PASSWORD')
        print("2")
        my_smtp.sendmail('test@gmail.com','test@gmail.com',text)
        print("3")
        my_smtp.quit()
        print("4")
    except:
        print("error")

def envoiMail2():
    msg = MIMEMultipart()
    msg['From'] = 'test@gmail.com'
    msg['To'] = 'test@gmail.com'
    msg['Subject'] = 'Le sujet de mon mail' 
    message = 'Bonjour !'
    msg.attach(MIMEText(message))
    #mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver = smtplib.SMTP('smtp.gmail.com:587')
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('test@gmail.com', 'PASSWORD')
    mailserver.sendmail('test@gmail.com', 'test@gmail.com', msg.as_string())
    mailserver.quit()