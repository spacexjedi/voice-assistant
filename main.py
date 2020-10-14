import speech_recognition as sr #  speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time 
import webbrowser 
import yfinance as yf # api
import ssl
import certifi
import time
import os

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        if ask:
            carver_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
           carver_speak('Sorry, I did not get that')
        except sr.RequestError:
            carver_speak('Sorry, my speech service is down')
        return voice_data

def respond(voice_data):
    if ' what is your name' in voice_data:
        carver_speak('Mu name is Carver')
    if 'what time is it':
        carver_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        carver_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location')
        url = 'https://google.nl/maps/place' + location + '/&amp;'
        webbrowser.get().open(url)
        carver_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        exit()

def carver_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

time.sleep(1)
carver_speak('How Can I Help You?')
while 1:    
    voice_data = record_audio()
    respond(voice_data)
