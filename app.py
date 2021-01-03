from flask import Flask, render_template, request, url_for, redirect, session
import GoogleNLPAPI as api
import getYoutubeVideoLinks as getYT
import emailer as email
import speechRecogNew as sp

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
    if 'transcript' in session:
        keywords = api.sample_analyze_entities(session['transcript'])
        session['keywords'] = keywords
        return render_template('textanalysis.html')
    else:
        return redirect('/convertwav')


@app.route('/youtubevids')
def youtubevids():
    videos = []
    if 'keywords' in session:
        for catergory, keywords in session['keywords'].items():
            for keyword in keywords:
                video = getYT.searchVideoForKeyword(keyword)
                for indivvideo in video:
                    videos.append(f'{indivvideo}')
        return render_template('videos.html', videos=videos)
    else:
        return redirect('/convertwav')


@app.route('/convertwav', methods=['GET', 'POST'])
def convertwav():
    transcript = ""
    if request.method == "POST":
        # print("FORM DATA RECEIVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            sp.silence_based_conversion(file)
            with open("speechRecognition.txt", "r") as myfile:
                data = myfile.read().splitlines()
            print(data)
            # recognizer = sr.Recognizer()
            # audioFile = sr.AudioFile(file)
            # with audioFile as source:
            #     recognizer.adjust_for_ambient_noise(source)
            #     data = recognizer.record(source)
            # transcript = recognizer.recognize_google(data, key=None)
            # session['transcript'] = transcript
            # print(transcript)
            return redirect('/textanalysis')





    return render_template('convertwav.html')


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
