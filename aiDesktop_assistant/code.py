#jarvis do this

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

file = open("email.txt","r")
y=[]
y= file.readlines()
file.close()
sender_email = y[0].rstrip()
password = y[1].rstrip()
reciever_email = y[2].rstrip()

engine = pyttsx3.init('sapi5')

#getting details of current voice
voices = engine.getProperty('voices') 
#print(voices[1].id)
engine.setProperty('voices', voices[1].id) #girls voice


def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(f"Listening to you {gender}.....")
        r.pause_threshold = 1  #after we complete speaking gives 1 sec pause
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print(f"{gender}, Please say that again.....")  
        speak(f"{gender}, Please say that again.....")
        query = "None"
    return query


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning {gender} !   ")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon  {gender} !   " )   

    else:
        speak(f"Good Evening  {gender}!   ")  

    speak(f"    I am your AI assitant {gender}   Please tell me how can I help you?")  

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, to, content)
    server.close()



if __name__=="__main__" :  #main func
    speak("please enter how will you like to be addressed:   Ma'am or      Sir or    Other")
    gender = input()
    wishme()   
    run = True
    while run:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Twinkle\\Music\\songs'
            songs = os.listdir(music_dir)
            x = random.randint(0,len(songs)-1)  
            os.startfile(os.path.join(music_dir, songs[x]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"{gender}, the time is {strTime}")
            print(f"{gender}, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Twinkle\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 

        elif 'email to twinkle' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = reciever_email    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(f"Sorry {gender} I am not able to send this email.Please try again.")     
        
        elif 'exit' in query:
            speak(f"Thankyou {gender}. Have a great day!")
            run = False

        elif(query!="none"):
            speak("This function is yet to be introduced  Please try something else.")