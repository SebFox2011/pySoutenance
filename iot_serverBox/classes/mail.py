import smtplib
import getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def envoiMail():
    print("fonction")
    my_smtp = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    print (my_smtp)
    print("1")
    my_smtp.login('test@gmail.com',getpass.getpass())
    print("2")
    my_smtp.sendmail('test@gmail.com','test@gmail.com',"text")
    print("3")
    my_smtp.quit()
    print("4")

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

def envoiMail3():
    message = MIMEText('Ceci est un test !')
    message['Subject'] = 'Objet du message'

    message['From'] = 'test@gmail.com'
    message['To'] = 'test@gmail.com'
    print(message)
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        print(server)
    except:
        print("error")
    server.starttls()
    server.login('test@gmail.com','PASSWORD')
    server.send_message(message)
    server.quit()

def envoiMail4():
    try:
        print("server connection")
        server = smtplib.SMTP('ns0.ovh.net', 5025)
        server.set_debuglevel(1)
        print("server login")
        server.login("lemail@ledomaine.com", "lepass")

        print("send mail")

        msg = r"gnng\nHello!" 
        server.sendmail("lemail@ledomaine.com", "destinataire", msg)
        server.quit()
    except :
        print("error")
