import smtplib

<<<<<<< HEAD
def send_email(subject, msg, RECIEVER_ADDRESS, PASSWORD, SENDER_ADDRESS, keywordsDict):
=======

def send_email(subject, msg, RECIEVER_ADDRESS, PASSWORD, SENDER_ADDRESS):
>>>>>>> 2cdadcf960d3a571c7766135c2cdeb9e2183df23
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, PASSWORD)
<<<<<<< HEAD

        message = 'Subject: {} \n\n {} \n\n Hey there! \n\n We '.format(subject, msg)

        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message)
=======
        message = 'Dear User, \n\n\tHere is your transcript\n\n{}'.format(msg)
        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message, subject)
>>>>>>> 2cdadcf960d3a571c7766135c2cdeb9e2183df23
        return "Success: Email sent!"
    except:
        return "Email failed to send. Try checking your password"
