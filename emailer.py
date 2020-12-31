import smtplib

SENDER_ADDRESS = "audiolec4@gmail.com"
RECIEVER_ADDRESS = "audiolec4@gmail.com"
PASSWORD = "hackathon2020"

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message)
        print("Success: Email sent!")
    except:
        print("Email failed to send.")

send_email("email from pycharm", "this is a test")