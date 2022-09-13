# go to our gmail account and setup 2 factor authentication
# generate app password
# 3. create a funtion to send a email

from email.message import EmailMessage
import imp
from multiprocessing import context
import string
from data import email_pasword as password #<-- the genarate password is save in another file for security
import ssl
import smtplib

email_sender = 'locomaniacoooooo@gmail.com'
email_password = password

email_reciver = 'maestre-2001@hotmail.com'

email_subject = 'Python email test'

body = """ This is an email sent using a python app :) UwU"""

em = EmailMessage() # <--3.  <--instace of the email
em['From']= email_sender
em['To']= email_reciver
em['Subject']= email_subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',context=context) as smtp:  #<--log in in the email account and sent the email
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_reciver,em.as_string())