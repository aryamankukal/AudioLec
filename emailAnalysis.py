import smtplib

def send_email(subject, msg, RECIEVER_ADDRESS, PASSWORD, SENDER_ADDRESS, keywordsDict):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, PASSWORD)

        message = 'Subject: {} \n\n {} \n\n Hey there! \n\n We '.format(subject, msg)

        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message)
        return "Success: Email sent!"
    except:
        return "Email failed to send. Try checking your password"