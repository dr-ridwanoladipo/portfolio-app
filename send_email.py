import smtplib, ssl
import os
from email.message import EmailMessage
from dotenv import load_dotenv
load_dotenv()

def send_email(subject, body):
    host = "smtp.gmail.com"
    port = 465
    username = os.getenv("EMAIL_USERNAME")
    password = os.getenv("PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    # Build proper email message
    msg = EmailMessage()
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.send_message(msg)
