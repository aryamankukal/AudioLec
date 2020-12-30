from flask import Flask, render_template, request, url_for, redirect, session
import speech_recognition as sr

app = Flask(__name__)



@app.route('/')
def recordwav():
    return render_template('index.html')

@app.route('/recordwav', methods=['GET', 'POST'])
def index():
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

    return render_template('upload.html', transcript=transcript)




if __name__ == '__main__':
    app.run(debug=True)

# body {
#             position: absolute;
#             display: -webkit-box;
#             display: -webkit-flex;
#             display: -ms-flexbox;
#             display: flex;
#             -webkit-box-pack: center;
#             -webkit-justify-content: center;
#             -ms-flex-pack: center;
#             justify-content: center;
#             -webkit-box-align: center;
#             -webkit-align-items: center;
#             -ms-flex-align: center;
#             align-items: center;
#             height: 100%;
#             width: 100%;
#             margin: 0;
#         }