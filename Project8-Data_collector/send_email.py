from email.mime.text import MIMEText
from mimetypes import MimeTypes
import smtplib

def send_email (email , height , average , count):
    from_email = "pythonbaki@gmail.com"
    from_password = "Baki654321"
    to_email = email

    subject = "Height Data"
    message = "Hey there,<br>Your height is <strong>%s</strong>.<br>The Average height from our data is <strong>%s</strong> and this calculated out of %s entries." % (height,average,count)

    msg = MIMEText(message , 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From'] = from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email , from_password)
    gmail.send_message(msg)