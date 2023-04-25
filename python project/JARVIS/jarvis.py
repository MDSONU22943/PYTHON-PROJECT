import pyttsx3
import  datetime
import speech_recognition as sr
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good afternoon zara")
    else:
        speak("Good Evening")
    speak("I am Jarvis sir.Please tell me how may i help you")

def takeCommand():
    '''it takes microphone input from the user and returns a string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.lis
if __name__=="__main__":
    speak("zara is a good girl")
    wishMe()