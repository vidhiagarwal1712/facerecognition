import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from time import strftime
engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
#print(voices[1].id)
engine.setProperty("vioces",voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait() 
def wishMe():   
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Adarsh")
    elif(hour>=12 and hour<16):
        speak("Good Afternoon Adarsh")
    else:
        speak("Good Evening Adarsh")
    speak("HI I am Jarvis Helper! How may I help you today.")
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:     
        print("Listning..")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language="en-in")
        print("user said"+query)
        return query
    except Exception as e :
        print("say that again please")
        return "None"

if(__name__ == "__main__"):
    wishMe()
    while True:
        query=takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "the time" in query:
            t=datetime.datetime.now().strftime("%H %M %S")
            speak(f"the time is {t}")   


