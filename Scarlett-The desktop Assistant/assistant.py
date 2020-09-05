import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")
    
    speak("I am Scarlett sir. Please tell me how may I help you?")


def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")

    except Exception:
        print("Say that again please..")
        return "None"

    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender@gmail.com','your_password')
    server.sendmail('sender@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishMe()
    if 1:
    
       query=takeCommand().lower()

       if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2)
           speak("According to Wikipedia")
           speak(results)

       elif 'open google' in query:
            webbrowser.open("google.com")
       elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
       elif 'the time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The time is{strTime}")

       elif 'open code' in query:
           codePath="C:\\Users\\Anuranjan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(codePath)
       elif 'email to anuranjan' in query:
           try:
               speak("What should i say?")
               content=takeCommand()
               to="reciever@gmail.com"
               sendEmail(to,content)
               speak("Email has been sent")
           except Exception as e:
               print(e)
               speak("sorry ,mail not send!")

       elif 'play music' in query:
               music_dir = 'D:\\songs\\Favorite Songs2'
               songs = os.listdir(music_dir)
               print(songs)    
               os.startfile(os.path.join(music_dir, songs[0]))
