from posixpath import split
from flask import Flask, render_template, request, url_for, redirect, session
import GoogleNLPAPI as api
import getYoutubeVideoLinks as getYT
import emailer as email
import speech_recognition as sr
from emailAnalysis import send_email
from pydub import AudioSegment
import math
import os
import glob

app = Flask(__name__)
app.secret_key = 'thisisasecretkey'

class SplitWavAudioMubin():
    def __init__(self, folder, file):
        # dirname = os.path.dirname(__file__)
        # self.folder = os.path.join(dirname, 'relative/path/to/file/you/want')
        self.folder = folder
        self.filename = "audio"
        self.filepath = file
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        split_audio.export(self.folder + '\\' + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            split_fn = str(i) + '_' + self.filename + ".wav"
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')


@app.route('/delallsessions')
def delallsessions():
    session.pop('transcript', None)
    session.pop('summary', None)
    session.pop('keywords', None)
    session.pop('email_sent', None)
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def index():
    # session.pop('transcript', None)
    # session.pop('summary', None)
    # session.pop('keywords', None)
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
    videos = []
    # people = []
    # places = []
    if 'transcript' in session:
        if request.method == 'POST':
            emailform = request.form
            reciever = emailform['email']
            subject = emailform['subject']
            send_email(f"{subject} - Your AudioLec Lecture", session['transcript'], reciever,
                       'hackathon2020', 'audiolec4@gmail.com', session['videos'], session['keywords'])
        keywords = api.sample_analyze_entities(session['transcript'])
        session['keywords'] = keywords
        if 'keywords' in session:
            for keyword in keywords:
                video = getYT.searchVideoForKeyword(keyword)
                for indivvideo in video:
                        #     if catergory == "people":
                        #         people.append(f'{indivvideo}')
                        #     elif catergory == "placesOrOrganizations":
                        #         places.append(f'{indivvideo}')
                    videos.append(f'{indivvideo}')
            session['videos'] = videos
            length_keywords = len(session['keywords'])
            return render_template('textanalysis.html', session=session, length_keywords=length_keywords)
        else:
            return redirect('/convertwav')

@app.route('/youtubevids')
def youtubevids():
    videos = []
    # people = []
    # places = []
    if 'keywords' in session:
        # for catergory, keywords in session['keywords'].items():
        #     for keyword in keywords:
        #         video = getYT.searchVideoForKeyword(keyword)
        #         for indivvideo in video:
        #             #     if catergory == "people":
        #             #         people.append(f'{indivvideo}')
        #             #     elif catergory == "placesOrOrganizations":
        #             #         places.append(f'{indivvideo}')
        #             videos.append(f'{indivvideo}')
        for keyword in session['keywords']:
            video = getYT.searchVideoForKeyword(keyword);
            for singlevid in video:
                videos.append(f'{singlevid}')

        return render_template('videos.html', videos=videos)
    else:
        return redirect('/convertwav')


@app.route('/convertwav', methods=['GET', 'POST'])
def convertwav():
    transcript = ""
    if request.method == "POST":
        if "myfiles[]" not in request.files:
            return redirect(request.url)

        file = request.files["myfiles[]"]
        if file.filename == "":
            return redirect(request.url)

        if file:
            # create recognizer object
            recognizer = sr.Recognizer()

            # split files
            split_wav = SplitWavAudioMubin(f"{os.path.dirname(__file__)}\\audiofiles", file)
            split_wav.multiple_split(min_per_split=1)

            # loop through split files
            session["transcript"] = ""
            for wavfile in glob.glob(f"audiofiles/*.wav"):
                audioFile = sr.AudioFile(wavfile)
                with audioFile as source:
                   recognizer.adjust_for_ambient_noise(source)
                   data = recognizer.record(source)
                   transcript = recognizer.recognize_google(data, key=None)
                   session["transcript"] += transcript

            filelist = [ f for f in os.listdir(f"audiofiles") if f.endswith(".wav")]
            for indivfile in filelist:
                os.remove(os.path.join(f"audiofiles", indivfile))

            # audioFile = sr.AudioFile(file)
            # with audioFile as source:
            #     recognizer.adjust_for_ambient_noise(source)
            #     data = recognizer.record(source)
            # transcript = recognizer.recognize_google(data, key=None)
            # session['transcript'] = transcript
            return redirect('/textanalysis')  # change in later/test

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



if __name__ == '__main__':
    app.run(host="localhost", port=5500, debug=True)
