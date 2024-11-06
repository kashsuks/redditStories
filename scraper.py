#Main file
import requests
from gtts import gTTS
import os

#Setup for TTS
sampleScript = """This is a sample script, please change this later for the actual script that is
being pulled from reddit"""
language = 'en' #'en' is english

#TTS object generation
myobj = gTTS(text = sampleScript, lang = language, slow = True)

#Run the files
myobj.save("welcome.mp3")
os.system("start welcome.mp3")

URL = "add link here"