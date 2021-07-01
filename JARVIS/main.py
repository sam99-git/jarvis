import pyttsx3
import speech_recognition as sr
import datetime 
import wikipedia
import webbrowser
import os
import smtplib

print("initializing jarvis")
MASTER = "Sameer Sir"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Initializing Jarvis")

def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("Good afternoon" + MASTER)  

    else:
        speak("Good Evening" + MASTER)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing....")
        query = r.recognize_google(audio , language = 'en- us')    
        print(f"user said: {query}\n ")

    except Exception as e:
        print("Say that again sir please")
        query = None

    return query        

speak("I am Jarvis , How may i help you?")
wishMe()
query = takeCommand()

if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia" , "")
    results = wikipedia.summary(query , sentences = 3)
    print(results)
    speak(results)
    
elif 'open youtube' in query.lower():

    url = "youtube.com"

    chrome_path =  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():

    url = "google.com"

    chrome_path =  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url) 

elif 'open instagram' in query.lower():

    url = "instagram.com"

    chrome_path =  'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "D:\\Songs"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir , songs[0]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H : %M : %S")
    speak(f"{MASTER} the time is {strTime}")



    
