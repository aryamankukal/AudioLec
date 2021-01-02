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
    session.pop('transcript', None)
    session.pop('summary', None)
    session.pop('keywords', None)
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
    session['keywords'] = keywords
    return render_template('textanalysis.html', session=session, keywords=keywords)


@app.route('/youtubevids')
def youtubevids():
    videos = []
    if 'keywords' in session:
        for keyword in session['keywords']:
            videolist = getYT.searchVideoForKeyword(keyword)
            for indivvideo in videolist:
                videos.append(f'{indivvideo}: {keyword}')
        return render_template('videos.html', videos=videos)
    else:
        return f'go to /convertwav'


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
    sender_email = contactform['email']
    subject = contactform['subject'] + f" by: {sender_email}"
    msg = contactform['message']
    if email == "" or subject == "" or msg == "":
        session['valid'] = False
    else:
        email.send_email(subject, msg, 'audiolec4@gmail.com',
                         'hackathon2020', 'audiolec4@gmail.com')
        session['email_sent'] = True
        return redirect('/#footer')
    return redirect('/#footer')


@app.route('/generic')
def generic():
    return render_template('generic.html')


if __name__ == '__main__':
    app.run(debug=True)
