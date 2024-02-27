from email.message import EmailMessage
import ssl
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

my_email = os.environ.get('MY_EMAIL')
my_pwd = os.environ.get('MY_PWD')
reciver = os.environ.get('RECIVER')


def send_email(body: str):
    subject = 'New Order'
    em = EmailMessage()
    em['From'] = my_email
    em['To'] = reciver
    em['Subject'] = subject

    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(my_email, my_pwd)
        smtp.sendmail(my_email, reciver, em.as_string())
