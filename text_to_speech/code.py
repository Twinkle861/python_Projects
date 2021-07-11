# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os



#window

root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Typed Text to speech project')


#heading
Label(root, text = 'TEXT_TO_SPEECH' , font='Verdana 40 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Enter Text :', font ='Verdana 20 ', bg ='#c6ffc1').place(y=120,x=40)


#text variable
Msg = StringVar()


#Entry field
entry_field = Text(root,height=12.5,width=68, font ='Verdana 10',padx=3,pady = 3)
entry_field.place(x=15 , y=170)


#functions

def Text_to_speech():
    Message = entry_field.get("1.0",'end-1c')
    speech = gTTS(text = Message)
    speech.save('texttomesssage.mp3')
    playsound('texttomesssage.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    entry_field.delete("1.0", END)
    os.remove('texttomesssage.mp3')

#Button
Button(root, text = "PLAY" , font = 'Verdana 20 bold', command = Text_to_speech).place(x=90, y=400, height=60,width=120)
Button(root, text = 'RESET', font='Verdana 20 bold', command = Reset).place(x=310 , y =400, height=60,width=120)

Button(root,text = 'EXIT',font = 'Verdana 20 bold' , command = Exit, bg = '#ffc478').place(x=200,y=480, height=60,width=120)


#infinite loop to run program
root.mainloop()
