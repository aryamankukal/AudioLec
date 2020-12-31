from flask import Flask, render_template, request, url_for, redirect, session
import speech_recognition as sr
import GoogleNLPAPI as api
# import summarizer as summ

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'


@app.route('/')
def index():
    return render_template('index.html')


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
    return render_template('textanalysis.html', session=session)


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
            keywords = api.sample_analyze_entities(transcript)
            session['keywords'] = keywords
            return redirect('/textanalysis')

    return render_template('convertwav.html', transcript=transcript)


if __name__ == '__main__':
    app.run(debug=True)
