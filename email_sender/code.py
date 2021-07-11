# create smtp server to send email
# # tls=transport layer security
#   google api to convert to text
# text to speech so that python can talk ie speaking engine->tts
# appy env or config for password
# to give subj in email need to import EmailMessage

from dotenv import load_dotenv
import os
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

load_dotenv()
listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1  #after we complete speaking gives 1 sec pause
        print('listening...')
        voice = r.listen(source)
        try:
            print('recognising...')
            info = r.recognize_google(voice,language='en-in')
            print(info)
            
        except Exception as e:
            print("Please say that again")
            get_info()
    return info.lower()

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login(os.environ.get("email"),os.environ.get("passw"))
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'twinkle':'twinklegupta861@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('Tell me the text in your email')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Your email is sent.Thankyou')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()