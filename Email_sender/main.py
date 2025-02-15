from email.message import EmailMessage
import ssl
import smtplib
from app_vars import APP_PASSWORD
from app_vars import SENDER_EMAIL
from app_vars import RECEIVER_EMAIL

email_sender = SENDER_EMAIL
email_password = APP_PASSWORD

email_receiver = RECEIVER_EMAIL

subject = "Greetings"
body = """
Assalamualaikum I am Mashfiqur Rahman. I am a 2nd year undergrade student at AIUB.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login (email_sender, email_password)
    smtp.sendmail (email_sender, email_receiver, em.as_string())
