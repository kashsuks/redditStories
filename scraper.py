import requests
from gtts import gTTS
import os
import platform
import subprocess
from playsound import playsound

# Setup for TTS
sampleScript = """This is a sample script, please change this later for the actual script that is
being pulled from reddit"""
language = 'en'
accent = 'us'

# TTS object generation
myobj = gTTS(text=sampleScript, lang=language, slow=True, tld=accent)
myobj.save("welcome.mp3")

#Cross-platform i like my cheese drippy
def play_audio(file_path):
    if platform.system() == "Windows":
        os.system(f"start {file_path}")     
    elif platform.system() == "Darwin":
        subprocess.call(["afplay", file_path])
    elif platform.system() == "Linux":
        subprocess.call(["xdg-open", file_path])
    else:
        playsound(file_path)

#Play the audio
play_audio("welcome.mp3")
