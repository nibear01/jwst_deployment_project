from gtts import gTTS
import os

# read the script you just downloaded
with open("jwst_script.txt", "r", encoding="utf-8") as f:
    text = f.read()

os.makedirs("assets/audio", exist_ok=True)    

tts = gTTS(text, lang="en")   # choose lang e.g. 'en'
tts.save("jwst_voice.mp3")    # output audio file
