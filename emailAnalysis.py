import smtplib


def send_email(subject, msg, RECIEVER_ADDRESS, PASSWORD, SENDER_ADDRESS, links, keywords):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(SENDER_ADDRESS, PASSWORD)

        # message = 'Subject: {}\n\nHey there! Here is your simplified lecture analysis. \n\nPlease email us at audiolec4@gmail.com if you have any questions or concerns.\n\n "{}" \n\nSincerely,\nThe AudioLec Team'.format(
        #     subject, msg)

        videoString = ""
        for video in links:
            videoString = f'{videoString}{video}, '

        keywordsList = []
        for catergory, keyword in keywords.items():
            keywordsList.append(keyword)

        keywordsString = ""
        for the_keywords in keywordsList:
            for keyword in the_keywords:
                keywordsString = f'{keywordsString}{keyword}, '
        message = '''Subject: {}

        Hey there! Here is your simplified lecture analysis.

        Please email us at audiolec4@gmail.com if you have any questions or concerns.

        Your transcript:

        {}

        Important topics to pay attention to:

        {}

        Videos to help you study:

        {} 
        
        Sincerely,
        The AudioLec Team\t'''.format(
            subject, msg, keywordsString, videoString)

        server.sendmail(SENDER_ADDRESS, RECIEVER_ADDRESS, message)
        return "Success: Email sent!"
    except:
        return "Email failed to send. Try checking your password"
