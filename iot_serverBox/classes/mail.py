import smtplib
import getpass

class Mail:
    def __init__(self):
        my_smtp = smtplib.SMTP_SSL('smtp.gmail.com')
        my_smtp.login('test@gmail.com',getpass.getpass())

    def envoi(self,mailAdress):
        my_smtp.sendmail('test@gmail.com','test@gmail.com',"text")
        