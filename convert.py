from os import path
from pydub import AudioSegment

# files
src = "test.mp3"  # output file
#dst = "add path to .wav file here"

# convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")
