import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'en'
output_lang ='fr'
text = ''

try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    print("Try again")

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('translated.mp3')
playsound.playsound('translated.mp3')
# print(googletrans.LANGUAGES)