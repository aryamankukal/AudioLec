# from os import path
# from pydub import AudioSegment
# import sys
# import os
#
# # files
# src = "/Users/gkukal/Downloads/Thu, 31 Dec 2020 18_13_56 GMT (online-audio-converter.com).mp3"  # output file
# dst = "/Users/gkukal/Downloads/test.wav"''
# print(os.environ['PATH'])
#
#
# # convert wav to mp3
# # sound = AudioSegment.from_mp3(src)
# # sound.export(dst, format="wav")

from pydub import AudioSegment

src = "/Users/gkukal/Downloads/Thu, 31 Dec 2020 18_13_56 GMT (online-audio-converter.com).mp3"
dst = "/Users/gkukal/Downloads/convertedMP3.wav"

sound = AudioSegment.from_mp3(src)
sound.export(src, format="wav")