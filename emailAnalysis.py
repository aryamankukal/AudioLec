import smtplib


def send_email(subject, msg, RECIEVER_ADDRESS, PASSWORD, SENDER_ADDRESS):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\nHey there! We have emailed your lecture analysis as you requested. Please email audiolec4@gmail.com if you have any questions or concerns.\n\n{}\n\nSincerely,\nThe AudioLec Team'.format(
            subject, msg)

        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message)
        return "Success: Email sent!"
    except:
        return "Email failed to send. Try checking your password"
