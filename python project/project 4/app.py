import os

import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes

# speech to text conversion
def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)
        try:
            print("Recognizing...")
            data=recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understanding")


# text to speech conversion
def speechtx(x):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',120)
    engine.say(x)
    engine.runAndWait()

if __name__=='__main__':

    # if sptext().lower()=="hey peter":
        data1=sptext()
        if "your name" in data1:
            name="my name is zara"
            speechtx(name)
        elif "old are you" in data1:
            age="i am 19 year old"
            speechtx(age)
        elif "time" in data1:
            time=datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "web" in data1:
            webbrowser.open("https://www.youtube.com/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            print(joke_1)
            speechtx(joke_1)
        elif "play song" in data1:
            add="E:\music"
            listsong=os.listdir(add)
            print(listsong)
            os.startfile(os.path.join(add,listsong[1]))



    # else:
    #     print("thanks")

