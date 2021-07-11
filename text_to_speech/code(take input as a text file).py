# import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import os
from tkinter import filedialog
import time
from tkinter.ttk import Progressbar
from tkinter import ttk

#initial window

root = Tk()
root.geometry('600x600')
root.resizable(0,0)
root.config(bg = '#c6ffc1')
root.title('Text file to speech project')


#heading
Label(root, text = 'TEXT_TO_SPEECH' , font='Verdana 40 bold italic' , bg ='#c6ffc1').pack(pady=20)


#label
Label(root, text ='Upload the text file Text :', font ='Verdana 20 ', bg ='#c6ffc1').place(y=120,x=40)


Msg=StringVar()
Message=None
#function
def upload():
    input = filedialog.askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
    print(input)
    if input is not None:
        pb = Progressbar(
            root, 
            orient=HORIZONTAL, 
            length=400, 
            mode='determinate'
            )
        pb.place(x=100, y=295)
        for i in range(5):
            root.update_idletasks()
            pb['value'] += 20
            time.sleep(0.50)
        pb.destroy()
        Label(root, text='File Uploaded Successfully!',  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=50, y=305)
        global Message 
        Message=''
        for i in input:
            Message=Message+i

def Text_to_speech():
    global Message 
    speech = gTTS(text=Message)
    speech.save('texttomesssage.mp3')
    playsound('texttomesssage.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    Label(root, text=" ",  font='Verdana 25 bold italic' , bg ='#c6ffc1').place(x=50, y=305,width=600,height=50)
    os.remove('texttomesssage.mp3')

#upload file
Button(root, text ='Select a .txt file', font ='Verdana 20 ', command = lambda:upload()).place(x=100, y=200, height=60,width=400)
#Button

Button(root, text = "PLAY" , font = 'Verdana 20 bold', command = Text_to_speech).place(x=110, y=400, height=60,width=120)
Button(root, text = 'RESET', font='Verdana 20 bold', command = Reset).place(x=330 , y =400, height=60,width=120)

Button(root,text = 'EXIT',font = 'Verdana 20 bold' , command = Exit, bg = '#ffc478').place(x=220,y=490, height=60,width=120)


#infinite loop to run program
root.mainloop()
