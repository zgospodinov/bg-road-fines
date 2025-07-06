import os
import smtplib
import ssl
from dotenv import load_dotenv
from email.message import EmailMessage


load_dotenv()

EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_FROM = os.getenv("EMAIL_FROM")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
E_USLUGI_MVR_URL = os.getenv("E_USLUGI_MVR")


def send_email(subject, body):
    print("Sending email notification...")
    
    content = f"""
    {body}

    <h2>За плащане, при наличие на глоби, посетете:</h2>
    <a href="{E_USLUGI_MVR_URL}">Портал за електронни административни услуги на МВР</a>
    """

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_FROM
    msg['To'] = EMAIL_TO
    msg.add_alternative(content, subtype="html")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as email_server:
        email_server.login(SMTP_USER, SMTP_PASS)
        email_server.send_message(msg)
    
    print("Email notification sent")