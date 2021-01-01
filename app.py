from flask import Flask, render_template, request, url_for, redirect, session
import speech_recognition as sr
import GoogleNLPAPI as api
import getYoutubeVideoLinks as getYT
import emailer as email

# import summarizer as summ

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'


@app.route('/delallsessions')
def delallsessions():
    session.pop('transcript', None)
    session.pop('summary', None)
    session.pop('keywords', None)
    session.pop('email_sent', None)
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', session=session)


@app.route('/record')
def record():
    return render_template('record.html')


@app.route('/delsession', methods=['GET', 'POST'])
def delscript():
    session.pop('transcript', None)
    session.pop('summary', None)
    session.pop('keywords', None)
    return redirect('/convertwav')


@app.route('/textanalysis', methods=['GET', 'POST'])
def textanalysis():
    keywords = api.sample_analyze_entities(session['transcript'])
    return render_template('textanalysis.html', session=session, keywords=keywords)


@app.route('/convertwav', methods=['GET', 'POST'])
def convertwav():
    transcript = ""
    if request.method == "POST":
        print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)
            session['transcript'] = transcript
            # summary = summ.summarizer(transcript)
            # session['summary'] = summary
            return redirect('/textanalysis')

    return render_template('convertwav.html', transcript=transcript)


@app.route('/contactform', methods=['GET', 'POST'])
def contactform():
    session['valid'] = True
    contactform = request.form
    SENDER_ADDRESS = contactform['email']
    subject = contactform['subject']
    msg = contactform['message']
    PASSWORD = contactform['password']
    if SENDER_ADDRESS == "" or subject == "" or msg == "" or PASSWORD == "":
        session['valid'] = False
    else:
        email.send_email(subject, msg, 'audiolec4@gmail.com',
                         PASSWORD, SENDER_ADDRESS)
        session['email_sent'] = True
        return redirect('/#footer')
    return redirect('/#footer')


if __name__ == '__main__':
    app.run(debug=True)
